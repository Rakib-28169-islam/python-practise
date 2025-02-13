import numpy as np

a = np.array([1,2,100,4,5])
b=  np.array([1,2,3,4,5])
c = np.linspace(1,3,10)
iden = np.identity(3)
print(a)
print(2*a)
print(a+b)
print(a-b)
print(a/b)
print(sum(a))
print(min(a))
print(max(a))
print(np.mean(a))
print(np.median(a))
print(c)
print(iden)
arr = np.arange(99)
print(arr)
print(arr.reshape(3,33))
print(arr.nbytes)

"""
[  1   2 100   4   5]
[  2   4 200   8  10]
[  2   4 103   8  10]
[ 0  0 97  0  0]
[ 1.          1.         33.33333333  1.          1.        ]
112
1
100
22.4
4.0
[1.         1.22222222 1.44444444 1.66666667 1.88888889 2.11111111
 2.33333333 2.55555556 2.77777778 3.        ]
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95
 96 97 98]
[[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
  24 25 26 27 28 29 30 31 32]
 [33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56
  57 58 59 60 61 62 63 64 65]
 [66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89
  90 91 92 93 94 95 96 97 98]]
792
"""
