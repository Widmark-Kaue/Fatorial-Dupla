# -*- coding: utf-8 -*-

"""
Created on 

@author:Widmark Kauê

"""


def dfact (n):
    
    #Verificando se o valor introduzido segue restrições para o cálculo da fatorial dupla.
    assert n>-2,"dfact: Fatorial Dupla só pode ser calculada para números >= -1"
    assert type(n)== int, "dfact: Fatorial Dupla só pode ser calculada para números inteiros"
     
    #Criação de um auxiliar
    a=1
    
    if (n%2==0) and (n>0): #Verifica se o valor é par e maior que zero.
        
        for i in range (n,0,-2): #Faz um regresão para números pares da fatorial dupla e executa as multiplicações.
            a=a*i                
            
    elif (n>0): #Não sendo par, o valor é impar. Basta verificar se o mesmo é maior que zero.
        
        for i in range(n,-1,-2): #Faz um regressão para número impares da fatorial dupla e executa as multiplicações.
            a=a*i
            
    #Não atendendo a nehuma das condições acima o valor de n é obrigatoriamente -1 e por definição o resultado também é -1. 
    else: 
        a=-1 
    
    #Retorna o valor da fatorial dupla.
    return a


    
