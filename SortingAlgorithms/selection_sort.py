"""
0 1 2 3 4 5 6 7 8 9 time
--------------------X index
4 1 1 1 1 1 1 1 1 1 | 0
5 5 2 2 2 2 2 2 2 2 | 1
7 7 7 3 3 3 3 3 3 3 | 2
1 4 4 4 4 4 4 4 4 4 | 3
3 3 3 7 7 5 5 5 5 5 | 4
2 2 5 5 5 7 6 6 6 6 | 5
9 9 9 9 9 9 9 7 7 7 | 6
8 8 8 8 8 8 8 8 8 8 | 7
6 6 6 6 6 6 7 9 9 9 | 8
"""

def selectionSort(array):
    for x in range(len(array)):
        minElem = x

        for y in range(x, len(array)):
            if array[y] < array[minElem]:
                minElem = y

        array[x], array[minElem] = array[minElem], array[x]

    return array

selectionSort([4, 5, 7, 1, 3, 2, 9, 8, 6])
selectionSort([8, 1, 6, 4, 8, 2, -9, 6, 2, 8, 7, 4, 2, 6, 7])
