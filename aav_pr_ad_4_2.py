# -*- coding: utf-8 -*-
"""aav_pr_ad_4_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18TR0d1p9yDn9ec9MS9NQaWtByIAxTKTD
"""

def mn(N):
    k = 2
    x = []
    if N == 0:
        return [0]
    else:
        for i in range(1, N + 1):
            if N % i == 0:
                x.append(i)
    return x

mn(9999)