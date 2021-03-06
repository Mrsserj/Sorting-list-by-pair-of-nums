# coding: utf-8

"""
Модуль использует алгоритм поиска в ширину [1] для поиска возможных перестановок.

[1] https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA_%D0%B2_%D1%88%D0%B8%D1%80%D0%B8%D0%BD%D1%83

"""


class Solver:
    """
    Класс подбора перестановок
    """

    def __init__(self, s=None, do_reverse=False):

        self.matrix = {}
        self.deep = 0
        self._orig = ''
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

        nums = list(nums_str)

        for g_1 in range(len(nums)-2):
            for g_2 in range(g_1+2, len(nums)-1):
                buf = nums[g_1:g_1+2]
                nums[g_1:g_1+2] = nums[g_2:g_2+2]
                nums[g_2:g_2+2] = buf

                if ''.join(nums) not in self._used_codes:
                    self._used_codes.add(''.join(nums))
                    yield ''.join(nums), (g_1, g_2)
                nums = list(nums_str)

    def bfs(self, seq, do_reverse=False):
        """
        Поиск в ширину.
        :param seq: входящая последовательность, строка из 5-9 цифр без разделителей
        :param do_reverse: прямая или обратная сортировка
        :return: Возможность сортировки
        """

        self._orig = ''.join(sorted(seq, reverse=do_reverse))
        self.chain = [(self._orig, (0, 0))]
        self.matrix = {seq: None}
        self._used_codes = set(seq)
        if self. _orig == seq:
            self.deep = 0
            return True
        i = 1
        frontier = [seq]
        while frontier:
            next_ = []
            for u in frontier:
                for v, t in self.commut(u):
                    if v not in self.matrix:
                        self.matrix[v] = (u, t)
                        next_.append(v)
                    if self._orig == v:
                        self.deep, self.check = i, True
                        return True
            frontier, i = next_, i+1
        return False

    def __str__(self):
        if not self.matrix:
            return 'Массив не найден.'
        if not self.check:
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

    REVERSE = False
    if len(sys.argv) > 2 and sys.argv[2] == 'REVERSE':
        REVERSE = True

    if len(sys.argv) > 1 and re.fullmatch('[0-9]{5,9}', sys.argv[1]):
        INP = sys.argv[1]
    else:
        print("Use:")
        print(" >python transistive4.py XXXXXX [REVERSE]")
        sys.exit()

    print(Solver(INP, do_reverse=REVERSE))
