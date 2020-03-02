# coding: utf-8

"""
Модуль использует алгоритм поиска в ширину [1] для поиска возможных перестановок.

[1] https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA_%D0%B2_%D1%88%D0%B8%D1%80%D0%B8%D0%BD%D1%83

"""


class Solver(object):

    def __init__(self, s=None, do_reverse=False):

        self.matrix = {}
        self.deep = 0
        self._ORIG = ''
        self._used_codes = set()
        self.chain = []

        if s:
            self.check = self.bfs(s, do_reverse)
        else:
            self.check = False

    def commut(self, nums_str):
        """
        Генератор перестановок..
        :param nums_str: строка из 5-9 цифр без разделителей
        """

        nums = [i for i in nums_str]

        for g1 in range(len(nums)-2):
            for g2 in range(g1+2, len(nums)-1):
                buf = nums[g1:g1+2]
                nums[g1:g1+2] = nums[g2:g2+2]
                nums[g2:g2+2] = buf

                if ''.join(nums) not in self._used_codes:
                    self._used_codes.add(''.join(nums))
                    yield ''.join(nums), (g1, g2)
                nums = [i for i in nums_str]

    def bfs(self, s, do_reverse=False):
        """
        Поиск в ширину. s - входящая последовательность, строка из 5-9 цифр без разделителей.
        :param s: входящая последовательность, строка из 5-9 цифр без разделителей
        :param do_reverse: прямая или обратная сортировка
        :return: Возможность сортировки
        """

        self._ORIG = ''.join(sorted(s, reverse=do_reverse))
        self.chain = [(self._ORIG, (0, 0))]
        self.matrix = {s: None}
        self._used_codes = set(s)
        if self. _ORIG == s:
            self.deep = 0
            return True
        i = 1
        frontier = [s]
        while frontier:
            next_ = []
            for u in frontier:
                for v, t in self.commut(u):
                    if v not in self.matrix:
                        self.matrix[v] = (u, t)
                        next_.append(v)
                    if self._ORIG == v:
                        self.deep, self.check = i, True
                        return True
            frontier, i = next_, i+1
        return False

    def __str__(self):
        if not self.matrix:
            return 'Массив не найден.'
        elif not self.check:
            return 'Массив не сортируется :('
        for i in range(self.deep):
            self.chain.append(self.matrix[self.chain[-1][0]])
        self.chain = self.chain[::-1]
        txt = []

        for i in self.chain[:-1]:
            txt.append("{0} {1}{2}<->{3}{4}".format(i[0], i[0][i[1][0]],
                                                    i[0][i[1][0]+1],
                                                    i[0][i[1][1]],
                                                    i[0][i[1][1]+1]))
        txt.append(self.chain[-1][0])
        return '\n'.join(txt)

if __name__ == '__main__':
    import sys
    import re

    reverse = False
    if len(sys.argv) > 2 and sys.argv[2] == 'reverse':
        reverse = True

    if len(sys.argv) > 1 and re.fullmatch('[0-9]{5,9}', sys.argv[1]):
        inp = sys.argv[1]
    else:
        print("Use:")
        print(" >python transistive4.py XXXXXX [reverse]")
        sys.exit()

    print(Solver(inp, do_reverse=reverse))
