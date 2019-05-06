#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:39:31 2019

@author: isleimar
"""

consoantes=['b','c','d','f','g','h','j','l','m','n','p','q','r','s','t','v','x','z','k','y']
vogais=['a','e','i','o','u']
limAfa=[len(consoantes)-1,len(vogais) -1]
limNum=[7,7]

palavra=[[0,0],[0,0],[0,0],[0,0]]

def incSilaba(m,n):
    if(m[1]<n[1]):
        m[1] = m[1] +1
    else:
        m[1] = 0
        if(m[0]<n[0]):
            m[0] = m[0] +1
        else:
            m[0] = 0
            return 1
    return 0

def incPalavra(g):
    if (g <= 2 ):
        if(incSilaba(palavra[g],limAfa)==1):               
            return incPalavra(g+1)
    else:
        return 0
            
def saidaSilaba(s):
    return consoantes[s[0]] + vogais[s[1]]
        
def saidaPalavra(p):
    r = ''
    for j in range(3):
        r = r + saidaSilaba(p[j])        
    r = r +  str(p[3][0]) + str(p[3][1])
    return r
cont = True
while cont:
    print(saidaPalavra(palavra))
    if (incPalavra(0) == 0):
        cont = False;

    

