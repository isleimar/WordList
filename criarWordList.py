#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:39:31 2019

@author: isleimar
"""

import random

#Lista de caracteres possíveis
consoantes=['b','c','d','f','g','h','j','l','m','n','p','q','r','s','t','v','x','z','k','y']
vogais=['a','e','i','o','u']
limAfa=[len(consoantes)-1,len(vogais) -1]
limNum=[7,7]
wordlist = []

#Configuração da palavra
palavra=[[0,0],[0,0],[0,0],[0,0]]
limites=[limAfa,limAfa,limAfa,limNum]


      
#Função para montar a saída da sílaba      
def saidaSilaba(s):
    return consoantes[s[0]] + vogais[s[1]]
        
#Função para montar a saída da palavra
def saidaPalavra(p):
    tamPalavra = len(palavra)-1
    r = ''
    for j in range(tamPalavra):
        r = r + saidaSilaba(p[j])        
    r = r +  str(p[tamPalavra][0]) + str(p[tamPalavra][1])
    return r

def aletSilaba(m,n):
    m[0]= random.randint(0,n[0])
    m[1]= random.randint(0,n[1])
    
def aleatorio():
    tamPalavra = len(palavra)
    for j in range(tamPalavra):
        aletSilaba(palavra[j],limites[j])
        
def existe(p):
    for j in wordlist:
        if j == p:
            print(p)
            return True
    return False

cont = True
while len(wordlist) < 10000:
    aleatorio()
    s = saidaPalavra(palavra)
    while (existe(s)):
        aleatorio()
        s = saidaPalavra(palavra)
        
    wordlist.append(s)

arquivo = open('wordlist.txt','w')  
for j in wordlist:
    arquivo.writelines(j+'\n')    
arquivo.close
print('Fim')

