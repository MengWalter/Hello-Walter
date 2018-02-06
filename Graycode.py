#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 15:54:39 2018

@author: williammeng
"""
    
def Graycode(n):
    if n==0:
        return [0]
    if n==1:
        return [0,1]
    
    result = Graycode(n-1)
    s = pow(2,n-1)
    for i in range(s-1,-1,-1):
        result.append(result[i]+s)
    return result

def dec2bin(num):
    l = []
    if num < 0:
        return '-' + dec2bin(abs(num))
    while True:
        num, remainder = divmod(num, 2)
        l.append(str(remainder))
        if num == 0:
            return ''.join(l[::-1])
        

def main():
    x = input()
    l = range(x)
    for i in range(0,x):
        l[i] = input()
    for i in range(0,x):
        output = Graycode(l[i])
        for j in range(0,len(output)):
            result = dec2bin(int(output[j]))
            print result.zfill(l[i])
        print('\n')    
    

if __name__ == '__main__':
    main()













