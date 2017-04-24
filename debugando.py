import json
import tkinter as menu
import time
import random
import math


    


class Inspermon():
    
    def __init__(self):
       
        
        def mostra_jogadorprincipal(jog_principal):
            print("Inspermon : {0}".format(jog_principal["nome"]))
            time.sleep(1)
            print("categoria : {0}".format(jog_principal["categoria"]))
            time.sleep(1)
            print("poder = {0}".format(jog_principal["poder"]))
            time.sleep(1)
            print("soco mais forte = {0}".format(jog_principal["Soco Mais forte"]))
            time.sleep(1)
            print("vida = {0}".format(jog_principal["vida"]))
            time.sleep(1)
            print("defesa = {0}".format(jog_principal["defesa"]))
            time.sleep(1)
            print("nível = {0}".format(jog_principal["nivel"]))
            time.sleep(1)
            print("Inspercash = {0}\n".format(jog_principal["Inspercash"]))



        def mostra_ipmon(ipmon):
            print("Inspermon : {0}".format(ipmon["nome"]))
            print("categoria : {0}".format(ipmon["categoria"]))
            print("poder = {0}".format(ipmon["poder"]))
            print("soco mais forte = {0}".format(ipmon["Soco Mais forte"]))
            print("vida = {0}".format(ipmon["vida"]))
            print("defesa = {0}\n".format(ipmon["defesa"]))
            time.sleep(3)


        def visualiza_Insperdex(dex):
            print("Inspermon : {0}".format(dex["nome"]))
            print("categoria : {0}".format(dex["categoria"]))
            print("poder = {0}".format(dex["poder"]))
            print("soco mais forte = {0}".format(dex["Soco Mais forte"]))
            print("vida = {0}".format(dex["vida"]))
            print("defesa = {0}".format(dex["defesa"]))
            print("Situacao : {0}\n".format(dex["Situacao"]))
            
        
   
        with open('inspermons_listacompleta.json') as arquivo:
            inspermons = json.load(arquivo)


        def personagens():
            for ipmon in inspermons:
                mostra_ipmon(ipmon)
        

    
        with open('principal.json') as arquivo:
            Inspermon_principal = json.load(arquivo)


        def jogador_principal():
            for jog_principal in Inspermon_principal:
                mostra_jogadorprincipal(jog_principal)


        
        with open('inspèrdex.json') as arquivo:
            Inspèrdex = json.load(arquivo)
            

        def mostra_insperdex():
            for dex in self.Inspèrdex:
                visualiza_Insperdex(dex)


        def main():
            """DAR BOAS VINDAS AO JOGADOR"""

            Nome_jogador=str(input("Selecione o nome do seu personagem  "))
            print("\n\nOla, {0}".format(Nome_jogador))
            if input()=="":
                print("\nBem vindo ao inspermon!! ")
            if input()=="":
                print("Antes de adentrar o Insper, voce deve estar ciente das regras do jogo ")
            if input()=="":
                print("Funciona assim cada dia de insper voce podera escolher \noque voce gostaria de fazer: \n   Por exemplo passear \n   Ou ir dormir um pouco")
            if input()=="":
                print("Logico cada ponto tem suas vantagens.\n Se voce escolher passear, voce melhora suas capacidades.\n Ja se voce decidir domir voce recupera sua vida.")
            if input()=="":
                print("Porem o jogo nao e tao facil assim!!\n Ao caminhar pelo Insper voce podera se deparar com outros Inspermons e tera de batalhar com eles.")
            if input()=="":
                print("Voce esta preparado?? Se sim, digite 1 para se aventurar nessa arriscada jornada pelo majestoso império Insper!")


        add_Inspèrdex = {}



        def save():
            with open('principal.json', 'w') as arquivo1:
                json.dump(Inspermon_principal, arquivo1)
            with open('inspèrdex.json','w') as arquivo2:
                Inspèrdex.append(add_Inspèrdex)
                json.dump(Inspèrdex, arquivo2)
            print("Programa Salvo!")
            self.window.destroy()

        
        def mostra_insperStore():
            insperstore = {'Café Mega Power' : 15, 'Energético' : 10, 'Exercício milimetralmente bem feito' : 45, 'Prova impecável' : 100, 'Noite de sono de mais de 8h' : 30}
            print(insperstore)

        #def regenera_vida()
            

        def dormir():
            print("Sua vida esta regenerando!")
            print("...")
            time.sleep(2)
            vida_completa = 200
            if Inspermon_principal[0]['vida']==vida_completa:
                print("Vida completamente carregada! Você está pronto para outra!")
            else:
                while Inspermon_principal[0]['vida']<vida_completa:
                    time.sleep(2)
                    Inspermon_principal[0]['vida'] = Inspermon_principal[0]['vida'] + 1
                    print(Inspermon_principal[0]['vida'])
            

            

        def escolher_andar():
            andar = input("Para qual andar deseja ir?\nDigite 0 para permanecer no térreo\n1 para 1º andar\n2 para 2º andar\n3 para 3º andar\n4 para 4º andar\n5 para 5º andar\n")
            time.sleep(3)
            while True:
                if andar=="0":
                    print("Você está no térreo")
                    sorte()
                elif andar=="1" or andar=="2" or andar=="3" or andar=="4" or andar=="5":
                    print("Você está no %sº andar" %andar)
                    sorte()
                else:
                    andar = input("Andar não identificado, por favor digite um número de 0 a 5 para escolher o andar desejado\n")


        self.oponente = random.randint(1, len(inspermons)-1)



        def mostra_insperdex():
            print(Inspèrdex)
        
        
        def batalha():
            winner = None
            player_health = Inspermon_principal[0]['vida']
            computer_health = inspermons[self.oponente]['vida']

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
                moves_player = {"Soco": Inspermon_principal[0]['poder'] - inspermons[self.oponente]['defesa'],
                     "Soco Mais forte": Inspermon_principal[0]['Soco Mais forte'] - inspermons[self.oponente]['defesa'],
                     "Recuperar vida": random.uniform(Inspermon_principal[0]['vida']*0.1,Inspermon_principal[0]['vida']*0.15 ),
                     "Fugir da Batalha": winner==None}
                moves_computer = {"Soco": inspermons[self.oponente]['poder'] - Inspermon_principal[0]['defesa'],
                     "Soco Mais forte": inspermons[self.oponente]['Soco Mais forte'] - Inspermon_principal[0]['defesa'],
                     "Recuperar vida": random.uniform(Inspermon_principal[0]['vida']*0.1,Inspermon_principal[0]['vida']*0.15)}             
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
                        if computer_health > inspermons[self.oponente]['vida']:
                            computer_health = inspermons[self.oponente]['vida']
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
                dict_linha1 = {"Inspermon" : "{0}".format(inspermons[self.oponente]['nome']),} 
                dict_linha2 = {"categoria" : "{0}".format(inspermons[self.oponente]["categoria"]),}
                dict_linha3 = {"poder" : "{0}".format(inspermons[self.oponente]["poder"]),}
                dict_linha4 = {"soco mais forte" : "{0}".format(inspermons[self.oponente]["Soco Mais forte"]),}
                dict_linha5 = {"vida" : "{0}".format(inspermons[self.oponente]["vida"]),} 
                dict_linha6 = {"defesa" : "{0}".format(inspermons[self.oponente]["defesa"]),}
                dict_linha7 = {"Situacao" : "DERROTADO"}
                add_Inspèrdex.update(dict_linha1)
                add_Inspèrdex.update(dict_linha2)
                add_Inspèrdex.update(dict_linha3)
                add_Inspèrdex.update(dict_linha4)
                add_Inspèrdex.update(dict_linha5)
                add_Inspèrdex.update(dict_linha6)
                add_Inspèrdex.update(dict_linha7)
                print("\nPlayer health: ", player_health, "Computer health: ", computer_health)
                print("\nVOCE GANHOU!!! VOCE REALMENTE E DEMAIS!!")
                  
            else:
                dict2_linha1 = {"Inspermon" : "{0}".format(inspermons[self.oponente]['nome']),} 
                dict2_linha2 = {"categoria" : "{0}".format(inspermons[self.oponente]["categoria"]),}
                dict2_linha3 = {"poder" : "{0}".format(inspermons[self.oponente]["poder"]),}
                dict2_linha4 = {"soco mais forte" : "{0}".format(inspermons[self.oponente]["Soco Mais forte"]),}
                dict2_linha5 = {"vida" : "{0}".format(inspermons[self.oponente]["vida"]),} 
                dict2_linha6 = {"defesa" : "{0}".format(inspermons[self.oponente]["defesa"]),}
                dict2_linha7 = {"Situacao" : "DERROTADO"}
                add_Inspèrdex.update(dict2_linha1)
                add_Inspèrdex.update(dict2_linha2)
                add_Inspèrdex.update(dict2_linha3)
                add_Inspèrdex.update(dict2_linha4)
                add_Inspèrdex.update(dict2_linha5)
                add_Inspèrdex.update(dict2_linha6)
                add_Inspèrdex.update(dict2_linha7)
                print("\nPlayer health: ", player_health, "Computer health: ", computer_health)
                print("\nSEU OPONENTE GANHOU!! MAIS SORTE DA PROXIMA VEZ!!.")


            Inspermon_principal[0]['vida']=player_health
            

            entrada = input("\nVOCE QUER CONTINUAR CAMINHANDO? SE SIM, PRESSIONE ENTER! CASO QUEIRA SALVAR O SEU ESTÁGIO ATUAL E SAIR DO JOGO, DIGITE 1!")
            if entrada=="":
                sorte()
            elif entrada=="1":
                save()


        
        def sorte():
            encontra_jogador = random.randint(1,2)
            print("Você está caminhando pelos mágicos corredores do Insper! O que será que está por vir?")
            time.sleep(2)
            print("...")
            time.sleep(3)
            if encontra_jogador == 2:
                print("Prepare-se! Você acabou de encontrar o jogador %s! É hora de batalhar!" %(inspermons[self.oponente]['nome']))
                time.sleep(5)
                batalha()
                return self.oponente
            else:
                print("UFA! Nenhum Inspermon à vista! O que deseja fazer agora? Digite 1 para continuar caminhando, 2 para pegar o elevador e ir para outro andar, 3 para acessar a InsperStore ou 4 para sair do jogo!")
                while True:
                    escolha = input()
                    if escolha=="1":
                        time.sleep(3)
                        sorte()
                    elif escolha=="2":
                        time.sleep(3)
                        escolher_andar()
                    elif escolha=="3":
                        time.sleep(3)
                        mostra_insperStore()
                    elif escolha=="4":
                        save()
                    else:
                        escolha = input("Opção não reconhecida! Por favor, digite um número de 1 a 4! ")
                return escolha
        

        def exponencial():
            nivel_maximo = 51
            lista_numeros = list(range(2,53))   
            sobe_nivel = []
            for i in range(1, nivel_maximo):
                sobe_nivel.append(i+lista_numeros[i])
            return sobe_nivel

        condicao_sobenivel = exponencial()

        def descobre_qtde():
            qtde_aparicoes = []
            for i in range(len(Inspèrdex)):
                if Inspèrdex[i]["Situacao"] == "DERROTADO":
                    qtde_aparicoes.append(i)
            return qtde_aparicoes


        aparicoes = descobre_qtde()
        
        def evoluir_a_cada():
            multiples = []
            for i in range(1,26):
                multiples.append(i*2)
            return multiples

        multiples = evoluir_a_cada()


        for i in range(2,len(condicao_sobenivel)+2):
            if aparicoes==sorted(aparicoes) and aparicoes==condicao_sobenivel[i-2]:
                Inspermon_principal[0]['nivel']==i
                print("PARABÉNS, VOCÊ SUBIU DE NÍVEL! AGORA VOCÊ FAZ PARTE DO SELETO GRUPO DE INSPERMONS QUE JÁ CONSEGUIRAM CHEGAR AO %dº NÍVEL!!!" %(i))
                if i in multiples:
                    Inspermon_principal[0]['poder']==Inspermon_principal[0]['poder']+100
                    Inspermon_principal[0]['Soco Mais forte']==Inspermon_principal[0]['Soco Mais forte']+105
                    Inspermon_principal[0]['defesa']==Inspermon_principal[0]['defesa']+50
                if i==(len(condicao_sobenivel)+2):
                    print("ORRA! REALMENTE ESTAMOS DIANTE DE UM(A) GRANDE GUERREIRO(A)!")
                    time.sleep(2)
                    print("A TUA GARRA E A TUA CORAGEM LHE TROUXERAM UMA GRANDE VITÓRIA:")
                    time.sleep(5)
                    print("VOCÊ ACABA DE VENCER O JOGO!")
                    time.sleep(3)
                    print("COMO PRÊMIO, VOCÊ ESTÁ SENDO COROADO(A) COMO O(A) MAIS NOVO(A) IMPERADOR(A) DO INSPER!!!")
                    time.sleep(2)
                    print("APROVEITE!")
                    time.sleep(1)
                    print("E ATÉ A PRÓXIMA!")
                



        self.window = menu.Tk()
        self.main = menu.Button(self.window)
        self.main.configure(text='Apresentação')
        self.main.configure(command=main)
        self.main.grid()
        self.passear = menu.Button(self.window)
        self.passear.configure(text='Passear')
        self.passear.configure(command=sorte)
        self.passear.grid()
        self.dormir = menu.Button(self.window)
        self.dormir.configure(text='Dormir')
        self.dormir.configure(command=dormir)
        self.dormir.grid()
        self.jogadorprincipal = menu.Button(self.window)
        self.jogadorprincipal.configure(text='Verificar meu Inspermon')
        self.jogadorprincipal.configure(command=jogador_principal)
        self.jogadorprincipal.grid()
        self.ver_personagens = menu.Button(self.window)
        self.ver_personagens.configure(text='Personagens')
        self.ver_personagens.configure(command=personagens)
        self.ver_personagens.grid()
        self.ver_insperdex = menu.Button(self.window)
        self.ver_insperdex.configure(text='Inspèrdex')
        self.ver_insperdex.configure(command=mostra_insperdex)
        self.ver_insperdex.grid()
        self.conhecer_insperStore = menu.Button(self.window)
        self.conhecer_insperStore.configure(text='Conhecer InsperStore')
        self.conhecer_insperStore.configure(command=mostra_insperStore)
        self.conhecer_insperStore.grid()
        self.salvar = menu.Button(self.window)
        self.salvar.configure(text='Salvar e Sair do Jogo')
        self.salvar.configure(command=save)
        self.salvar.grid()

        self.window.mainloop()
        


inicia_jogo = Inspermon()