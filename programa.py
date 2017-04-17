# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 10:39:43 2017

@author: nielton
"""

    
import json
import tkinter as menu
import time
import random


    


class Inspermon:
    def __init__(self):
        def mostra_ipmon(ipmon):
            print("Inspermon : {0}".format(ipmon["nome"]))
            print("categoria : {0}".format(ipmon["categoria"]))
            print("poder = {0}".format(ipmon["poder"]))
            print("soco mais forte = {0}".format(ipmon["Soco Mais forte"]))
            print("vida = {0}".format(ipmon["vida"]))
            print("defesa = {0}\n".format(ipmon["defesa"]))

        def mostra_jogadorprincipal(jog_principal):
            print("Inspermon : {0}".format(jog_principal["nome"]))
            print("categoria : {0}".format(jog_principal["categoria"]))
            print("poder = {0}".format(jog_principal["poder"]))
            print("soco mais forte = {0}".format(jog_principal["Soco Mais forte"]))
            print("vida = {0}".format(jog_principal["vida"]))
            print("defesa = {0}".format(jog_principal["defesa"]))
            print("Inspercash = {0}\n".format(jog_principal["Inspercash"]))


        with open('principal.json') as arquivo:
            Inspermon_principal = json.load(arquivo)
            for jog_principal in Inspermon_principal:
                mostra_jogadorprincipal(jog_principal)

        with open('inspermons_listacompleta.json') as arquivo:
            inspermons = json.load(arquivo)
            for ipmon in inspermons:
                mostra_ipmon(ipmon)

        with open('inspèrdex.json') as arquivo:
            Inspèrdex = json.load(arquivo)
            for ipmon in Inspèrdex:
                mostra_ipmon(ipmon)

        def save():
            with open('principal.json', 'w') as arquivo:
                for linha in range(len(Inspermon_principal)):
                    arquivo.write("%s\n" %Inspermon_principal[linha])
            with open('inspèrdex.py','w') as arquivo:
                for linha in range(len(Inspèrdex)):
                    arquivo.write("%s\n" %Inspèrdex[linha])
            return None

        def mostra_insperStore():
            insperstore = {'Café Mega Power' : 15, 'Energético' : 10, 'Exercício milimetralmente bem feito' : 45, 'Prova impecável' : 100, 'Noite de sono de mais de 8h' : 30}
            print(insperstore)

        def regenera_vida()
                ''

        def dormir():
            print("Sua vida esta regenerando!")
            print("...")
            time.sleep(2)
            
            time.sleep(3)
            return Inspermon_principal['vida']

        def escolher_andar():
            andar = input("Para qual andar deseja ir?\nDigite 0 para permanecer no térreo\n1 para 1º andar\n2 para 2º andar\n3 para 3º andar\n4 para 4º andar\n5 para 5º andar")
            time.sleep(3)
            if andar==0:
                print("Você está no térreo")
            elif andar==1 or andar==2 or andar==3 or andar==4 or andar==5:
                print("Você está no %dº andar" %andar)
            else:
                print("Andar não identificado, por favor digite um número de 0 a 5 para escolher o andar desejado")

        def batalha():
            winner = None
            player_health = inspermons[0]['vida']
            computer_health = inspermons[oponente]['vida']

        # determina quem joga segunda linha
            turn = random.randint(1,2) # 50%
            if turn == 1:
                player_turn = True
                computer_turn = False
                print("\nVoce ataca primeiro.")
                time.sleep(2)
            else:
                player_turn = False
                computer_turn = True
                print("\nTurno do computador.")
                time.sleep(2)


            print("\nSua vida: ", player_health, "Vida do computador: ", computer_health)
    
            while (player_health != 0 or computer_health != 0):
                heal_up = False 
                miss = False

            # dicionario
            moves_player = {"Soco": Inspermon_principal['poder'] - Inspermon_principal[oponente]['defesa'],
                     "Soco Mais forte": Inspermon_principal[0]['Soco Mais forte'] - Inspermon_principal[oponente]['defesa'],
                     "Recuperar vida": random.randint(Inspermon_principal[0]['vida']*0.1,Inspermon_principal[0]['vida']*0.15 ),
                     "Fugir da Batalha": winner==None}
            moves_computer = {"Soco": inspermons[oponente]['poder'] - inspermons[0]['defesa'],
                     "Soco Mais forte": inspermons[oponente]['Soco Mais forte'] - inspermons[0]['defesa'],
                     "Recuperar vida": random.randint(inspermons[0]['vida']*0.1,inspermons[0]['vida']*0.15)}             
            if player_turn:
                print("\nSelecione seu movimento :\n1. Soco (damage equivalente a seu poder)\n2. Soco Mais Forte (equivalente a seu poder + 5 de dano)\n3. Recuperar Vida (Voce pode recuperar de 10 a 15 de sua vida)\n4. Fugir da Batalha (20% de chance de fuga)\n")

                player_move = input("> ").lower()

                move_miss = random.randint(1,5) # 20%
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    player_move = 0 # player misses 
                    print("Errou!")
                    time.sleep(2)
                else:
                    if player_move in ("1", "Soco"):
                        player_move = moves_player["Soco"]
                        print("\nSOCO NA CARA ", player_move, " damage.")
                        time.sleep(2)
                    elif player_move in ("2", "Soco Mais forte"):
                        player_move = moves_player["Soco Mais forte"]
                        print("\nMEGA SOCO NA CARA", player_move, " damage.")
                        time.sleep(2)
                    elif player_move in ("3", "Recuperar vida"):
                        heal_up = True
                        player_move = moves_player["Recuperar vida"]
                        print("\nRECUPEROU VIDA", player_move, " Recuperar vida.")
                        time.sleep(2)
                    elif player_move in ("4", "Fugir da Batalha"):
                        player_move= moves_player["Fugir da Batalha"]
                        print("\nVoce Conseguiu ", " Fugir da Batalha.")
                        time.sleep(2)
                        break
                        
                    else:
                        print("\nTente novamente")
                        time.sleep(2)
                        continue

            else: # Computador

                move_miss = random.randint(1,5)
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    computer_move = 0 # erroou
                    print("O computador Errouu!")
                    time.sleep(2.5)
                else:
                    if computer_health > 30: 
                        if player_health > 75:
                            computer_move = moves_computer["Soco"]
                            print("\n O computador usou SOCO NA CARA ", computer_move, " damage.")
                            time.sleep(2.5)
                        elif player_health > 35 and player_health <= 75: 
                            imoves = ["Soco", "Soco Mais forte"]
                            imoves = random.choice(imoves)
                            computer_move = moves_computer[imoves]
                            print("\nO computador deu Soco Mais forte ", imoves, ". It dealt ", computer_move, " damage.")
                            time.sleep(2.5)
                        elif player_health <= 35:
                            computer_move = moves_computer["Soco Mais forte"]
                            print("\nO computador deu um Soco Mais forte ", computer_move, " damage.")                       
                            time.sleep(2.5)
                    else:#se tiver com pouca vida 50% de recuperar vida
                        heal_or_fight = random.randint(1,2) 
                        if heal_or_fight == 1:
                            heal_up = True
                            computer_move = moves_computer["Recuperar vida"]
                            print("\nO computador utilizou Recuperar vida. ", computer_move, " health.")
                            time.sleep(2.5)
                        else:
                            if player_health > 75:
                                computer_move = moves_computer["Soco"]
                                print("\nO computador utilizou Soco.", computer_move, " damage.")
                                time.sleep(2.5)
                            elif player_health > 35 and player_health <= 75:
                                imoves = ["Soco", "Soco Mais forte"]
                                imoves = random.choice(imoves)
                                computer_move = moves_computer[imoves]
                                print("\nO computador utilizou Soco Mais forte", imoves, ". It dealt ", computer_move, " damage.")
                                time.sleep(2.5)
                            elif player_health <= 35:
                                computer_move = moves_computer["Soco Mais forte"]
                                print("\nO computador utulizou Soco Mais forte. Para finalizar ", computer_move, " damage.")
                                time.sleep(2.5)
            if heal_up:
                if player_turn:
                    player_health += player_move
                    if player_health > Inspermon_principal[0]['vida']:
                        player_health = Inspermon_principal[0]['vida'] #vida nao passa do maximo
                else:
                    computer_health += computer_move
                    if computer_health > inspermons[oponente]['vida']:
                        computer_health = inspermons[oponente]['vida']
            else:
                if player_turn:
                    computer_health -= player_move
                    if computer_health < 0:
                        computer_health = 0 # sem vida negativa
                        winner = "Player"
                        break
                else:
                    player_health -= computer_move
                    if player_health < 0:
                        player_health = 0
                        winner = "Computer"
                        break

            print("\nPlayer health: ", player_health, "Computer health: ", computer_health)

            
            player_turn = not player_turn
            computer_turn = not computer_turn

        # quando acabar printar vencedor

        if winner == "Player":
            print("\nPlayer health: ", player_health, "Computer health: ", computer_health)
            print("\nVOCE GANHOU!!! VOCE REALMENTE E DEMAIS!!")
                  
        else:
            print("\nPlayer health: ", player_health, "Computer health: ", computer_health)
            print("\nSEUS OPONENTE GANHOU!! MAIS SORTE DA PROXIMA VEZ!!.")
        

        print("\nVOCE QUER CONTINUAR CAMINHANDO?")

        answer = input("> ").lower()
        if answer not in ("Sim", "s","sim","S"):
            play_again = False
            print("Ok!!")
            print("Selecione o que voce deseja fazer:\n1.Ir dormir(recupera a vida do seu Inspermon)\n2.Acessar a InsperStore\n3.Salvar e sair do jogo")
            answer2 = input(">")
            if answer2 == "1":
                dormir()
                print ("Deseja voltar a passear?")
                answer = input("> ").lower()
                if answer in ("Sim", "s","sim","S"):
                    play_again = True
                continue
            if answer2 == "2":
                mostra_insperStore()
            if answer2 == "3":
                save()
            else:
                print("Tente novamente")
                continue
            

        def sorte():
            encontra_jogador = random.randint(1,2)
            oponente = random.randint(1, len(inspermons)-1)
            if encontra_jogador == 1:
                print("Você está caminhando pelos mágicos corredores do Insper! O que será que está por vir?")
                time.sleep(2)
                print("...")
                time.sleep(3)
                print("Prepare-se! Você acabou de encontrar o jogador %s! É hora de batalhar! Pressione enter para avançar!" %(inspermons[sorte]['nome']))
                if input()=="":
                    batalha()
            else:
                print("Você está caminhando pelos mágicos corredores do Insper! O que será que está por vir?")
                print("...")
                time.sleep(3)
                print("UFA! Nenhum Inspermon à vista! O que deseja fazer agora? Digite 1 para continuar caminhando, 2 para pegar o elevador e ir para outro andar, 3 para acessar a InsperStore ou 4 para sair do jogo!")
                if input()=="1":
                    sorte()
                elif input()=="2":
                    escolher_andar()
                elif input()=="3":
                    mostra_insperStore()
                elif input()=="4":
                    save()
                else:
                    print("Opção não reconhecida! Por favor, digite um número de 1 a 4")

        def ganha_experiencia():
            while True:


        
        
        self.window = menu.Tk()
        self.passear = menu.Button(self.window)
        self.passear.configure(text='Passear')
        self.passear.configure(command=sorte)
        self.passear.grid()
        self.dormir = menu.Button(self.window)
        self.dormir.configure(text='Dormir')
        self.dormir.configure(command=dormir)
        self.dormir.grid()
        self.conhecer_insperStore = menu.Button(self.window)
        self.conhecer_insperStore.configure(text='Conhecer InsperStore')
        self.conhecer_insperStore.configure(command=mostra_insperStore)
        self.conhecer_insperStore.grid()
        self.salvar = menu.Button(self.window)
        self.salvar.configure(text='Salvar e Sair do Jogo')
        self.salvar.configure(command=save)
        self.salvar.grid()

        self.window.mainloop()



        def

            self.personagens = inspermons






inicia_jogo = Inspermon()










                  




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



    
    



    



    