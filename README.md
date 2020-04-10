# Sorting-list-by-pair-of-nums
Sorting number list by pair of nums
```
Массив из 6 элементов, состоящий из уникальных цифр от 1 до 6 расположенных случайным образом  
Т.е.:  
    `1,2,4,6,5,3`  
или  
    `2,6,4,1,3,5`  
или  
    `5,6,4,1,3,2`  
И т.д.  
```

Нужно отсортировать этот массив, чтобы получилось `1,2,3,4,5,6`  
Но при сортировке можно переставлять элементы парами,  например:  
со 2 и 3 позиции на 4 и 5 
или 
с 3 и 4 на 5 и 6 , при этом менять порядок внутри пары нельзя 
Т.е. пример такой сортировки парной перестановкой:  
    `1,6,3,2,5,4  ->   1,2,5,6,3,4  ->  1,2,3,4,5,6`  
На входе несортированный массив например  
    `541632`  
На выходе массив, что с чем меняем следующей строкой полученный массив и т.п.:  
    `541632 41<->63`  
    `563412 56<->12`  
    `123456`  
    
---
Если массив не удалось отсортировать, то на выходе сообщаем, что массив не сортируется.  
