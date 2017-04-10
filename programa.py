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


print(inspermons[0]['vida'])

"""import tkinter as tk

window = tk.Tk()
salvar = tk.Button(window)
salvar.configure(text='Salvar')
salvar.grid()
window.mainloop()"""

    
#valores = inspermons.values()
#if 'Jogador Principal' in valores:
     #= str(input("Qual é o seu nome?"))""" #Tentativa de trocar o "Jogador Principal" pelo nome do jogador
     
#Desenvolvendo o jogo:
    
#ideia: inserir janela com as opções de passear, dormir e alguma outra que se queira inserir

import random
#If escolha==passear:
sorte = random.randint(1, len(inspermons)-1)
print("Prepare-se! Você acabou de encontrar o jogador %s! É hora de batalhar!" %(inspermons[sorte]['nome']))




"""def batalha(inspermons):
    while inspermons[0]['vida']>0 and inspermons[sorte]['vida']>0:
        inspermons[sorte]['vida'] = inspermons[sorte]['vida']-inspermons[0]['poder']-inspermons[sorte]['defesa']
        if inspermons[sorte]['defesa']<=0:
            print("Boa! Você venceu! Agora já pode prosseguir o jogo")
        inspermons[0]['vida'] = inspermons[0]['vida']-inspermons[sorte]['poder']-inspermons[0]['defesa']
        if inspermons[0]['vida']<=0:
            print("Iiiiiih! Parece que deu ruim! Você perdeu!\n GAME OVER")

            



Inspèrdex = dict()
jogador_encontrado = inspermons[sorte]
Inspèrdex = [inspermons[sorte]]

#evoluindo Inspermóns
#fazer algo para sair do loop assim que subir de nível
if inspermons[0]['vida']>300:
    for sobe_nivel in range(1001):
        print("Parabéns! Você subiu de nível! Agora, você faz parte do seleto grupo de inspermons que conseguem alcançar o %dº nível! Boa sorte!" %(sobe_nivel))


# salvar jogo

#def salvar_jogo():"""



    
    



    



    