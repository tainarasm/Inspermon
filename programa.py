# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 10:39:43 2017

@author: nielton
"""

import json

def mostra_ipmon(ipmon):
    print("Inspermon : {0}".format(ipmon["nome"]))
    print("poder = {0}".format(ipmon["poder"]))
    print("vida = {0}".format(ipmon["vida"]))
    print("defesa = {0}".format(ipmon["defesa"]))
    print("Inspercash = {0}\n".format(ipmon["Inspercash"]))

with open('inspermonscommon.json') as arquivo:
    inspermons = json.load(arquivo)
    for ipmon in inspermons:
        mostra_ipmon(ipmon)
    
#valores = inspermons.values()
#if 'Jogador Principal' in valores:
     #= str(input("Qual é o seu nome?"))""" #Tentativa de trocar o "Jogador Principal" pelo nome do jogador
     
#Desenvolvendo o jogo:
    
import random
#If escolha==passear:
sorte = random.randint(1, len(inspermons))
print("Prepare-se! Você acabou de encontrar o jogador %s! É hora de batalhar!" %(inspermons[sorte]['nome']))

Inspèrdex = dict()
jogador_encontrado = inspermons[sorte]
Inspèrdex = [inspermons[sorte]]



    



    
    