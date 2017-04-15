# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 10:39:43 2017

@author: nielton
"""

    
import json
import tkinter as menu
import random
import shelve

    



window = menu.Tk()
passear = menu.Button(window)
passear.configure(text='Passear')
passear.grid()
salvar = menu.Button(window)
salvar.configure(text='Salvar e Sair do Jogo')
salvar.configure(command=save)
salvar.grid()
salvar.bind("<Button-1>", save)
dormir = menu.Button(window)
dormir.configure(text='Dormir')
dormir.grid()

window.mainloop()

class Inspermon:
    def __init__(self):
        def mostra_ipmon(ipmon):
            print("Inspermon : {0}".format(ipmon["nome"]))
            print("categoria : {0}".format(ipmon["categoria"]))
            print("poder = {0}".format(ipmon["poder"]))
            print("soco mais forte = {0}".format(ipmon["Soco Mais forte"]))
            print("vida = {0}".format(ipmon["vida"]))
            print("defesa = {0}".format(ipmon["defesa"]))
            print("Inspercash = {0}\n".format(ipmon["Inspercash"]))

        with open('inspermons_listacompleta.json') as arquivo:
            inspermons = json.load(arquivo)
            for ipmon in inspermons:
                mostra_ipmon(ipmon)

        self.personagens = inspermons
        
inicia_jogo = Inspermon()


    def sorte()

class InsperStore:
    def __init__(self):
        self.products = {'Café Mega Power' : 15, 'Energético' : 10, 'Exercício milimetralmente bem feito' : 45, 'Prova impecável' : 100, 'Noite de sono de mais de 8h' : 30}

Produtos = InsperStore()
print(Produtos.products)



# lista de produtos (InsperStore)
# Café Mega Power (15)
# Energético (10)
# Exercício milimetralmente bem feito (45)
# Prova impecável (100)
# Noite de sono de mais de 8h (30)


#with open('inspermonprincipal.json') as arquivo:
    #inspermon_principal = json.load(arquivo)
    #for ipmonprincipal in inspermon_principal:
        #mostra_ipmon(ipmonprincipal)







print(inspermon_principal)
        
"""def carrega_jogo(salvar_jogo):
    print("Inspermon : {0}".format(salvar_jogo["nome"]))
    print("poder = {0}".format(salvar_jogo["poder"]))
    print("vida = {0}".format(salvar_jogo["vida"]))
    print("defesa = {0}".format(salvar_jogo["defesa"]))
    print("Inspercash = {0}\n".format(salvar_jogo["Inspercash"]))
    
#with open('Save Inspermons.txt', "rw") as carregajogo:"""
    


print(inspermons[0]['vida'])

def save(inspermons, Inspérdex):
    with open('inspermonprincipal.json') as arquivo:
        arquivo.write(inspermon_principal)
        arquivo.write(Inspèrdex)



    




                  




#inserindo música

    
#valores = inspermons.values()
#if 'Jogador Principal' in valores:
     #= str(input("Qual é o seu nome?"))""" #Tentativa de trocar o "Jogador Principal" pelo nome do jogador
     
#Desenvolvendo o jogo:
    
#ideia: inserir janela com as opções de passear, dormir e alguma outra que se queira inserir

#If escolha==passear:
sorte = random.randint(1, len(inspermons)-1)
print("Prepare-se! Você acabou de encontrar o jogador %s! É hora de batalhar!" %(inspermons[sorte]['nome']))




def batalha(inspermons):
    while inspermons[0]['vida']>0 and inspermons[sorte]['vida']>0:
        inspermons[sorte]['vida'] = inspermons[sorte]['vida']-inspermons[0]['poder']-inspermons[sorte]['defesa']
        if inspermons[sorte]['defesa']<=0:
            print("Boa! Você venceu! Agora já pode prosseguir o jogo")
        inspermons[0]['vida'] = inspermons[0]['vida']-inspermons[sorte]['poder']-inspermons[0]['defesa']
        if inspermons[0]['vida']<=0:
            print("Iiiiiih! Parece que deu ruim! Você perdeu!\n GAME OVER")

            



jogador_encontrado = inspermons[sorte]
Inspèrdex = [inspermons[sorte]]

#evoluindo Inspermóns
#fazer algo para sair do loop assim que subir de nível
if inspermons[0]['vida']>300:
    for sobe_nivel in range(1001):
        print("Parabéns! Você subiu de nível! Agora, você faz parte do seleto grupo de inspermons que conseguem alcançar o %dº nível! Boa sorte!" %(sobe_nivel))


# salvar jogo

#def salvar_jogo():"""



    
    



    



    