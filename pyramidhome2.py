# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:23:57 2024

@author: Admin
"""

rows=int(input("enter no of rows"))
k=0
for i in range(1,rows+1):
    for space in range(1,(rows-i)+1):
        print(end=" ")
    while k!=(2*i-1):
        print("* ",end="")
        k+=1
    k=0
    print()
        