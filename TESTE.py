
import random
import time
import json
# import winsound
# winsound.PlaySound('Pokemon Sound Effect.mp3', winsound.SND_FILENAME)
def mostra_ipmon(ipmon):
    print("Inspermon : {0}".format(ipmon["nome"]))
    print("poder = {0}".format(ipmon["poder"]))
    print("vida = {0}".format(ipmon["vida"]))
    print("defesa = {0}".format(ipmon["defesa"]))
    print("Inspercash = {0}\n".format(ipmon["Inspercash"]))

with open('inspermonscommon.json') as arquivo:
    inspermons = json.load(arquivo)
    # for ipmon in inspermons:
    #     mostra_ipmon(ipmon)

import random
#If escolha==passear:
sorte = random.randint(1, len(inspermons)-1)
def main():
    """DAR BOAS VINDAS AO JOGADOR"""

    Nome_jogador=str(input("Selecione o nome do seu personagem  "))
    print("\n\nOla, {0}".format(Nome_jogador))
    if input()=="":
        print("\nBem vindo ao inspermon!! ")
    if input()=="":
        print("Antes de adentrar o Insper, voce deve estar ciente das regras do jogo ")
    if input()=="":
        print("Funciona assim cada dia de insper voce podera escolher oque voce gostaria de fazer \r Por exemplo ir estudar\n Ou ir relxar um pouco")
    if input()=="":
        print("Logico cada ponto tem suas vantagens.\r Se voce escolher estudar, voce melhora suas capacidades")
    if input()=="":
        print("Porem o jogo nao e tao facil assim!!\r Ao caminhar pelo Insper voce podera se deparar com outros Inspermons e tera de batalhar com eles.")
    if input()=="":
        print("Voce esta preparado??")
    time.sleep(3)

    play_again = True
    # Loop do jogador na primeira linha 
    while play_again:
        sorte = random.randint(1, len(inspermons)-1)
        print("Prepare-se! Você acabou de encontrar o jogador %s! É hora de batalhar!" %(inspermons[sorte]['nome']))
        if input()=="":
            winner = None
            player_health = inspermons[0]['vida']
            computer_health = inspermons[sorte]['vida']

        # determina quem joga segunda linha
        turn = random.randint(1,2) # 50%
        if turn == 1:
            player_turn = True
            computer_turn = False
            print("\nVoce ataca primeiro.")
            time.sleep(1)
        else:
            player_turn = False
            computer_turn = True
            print("\nTurno do computador.")
            time.sleep(1)


        print("\nSua vida: ", player_health, "Vida do computador: ", computer_health)

    
        while (player_health != 0 or computer_health != 0):

            heal_up = False 
            miss = False

            # dicionario
            moves_player = {"Soco": inspermons[0]['poder'],
                     "Soco Mais forte": inspermons[0]['Soco Mais forte'],
                     "Recuperar vida": random.randint(20, 25)}
            moves_computer = {"Soco": inspermons[sorte]['poder'],
                     "Soco Mais forte": inspermons[sorte]['Soco Mais forte'],
                     "Recuperar vida": random.randint(20, 25)}

            if player_turn:
                print("\nSelecione seu movimento :\n1. Soco (damage equivalente a seu poder)\n2. Soco Mais Forte (equivalente a seu poder + 5 de dano)\n3. Recuperar Vida (Voce pode recuperar de 20 ate 25 de vida)\n")

                player_move = input("> ").lower()

                move_miss = random.randint(1,5) # 20%
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    player_move = 0 # player misses 
                    print("Errou!")
                    time.sleep(1)
                else:
                    if player_move in ("1", "Soco"):
                        player_move = moves_player["Soco"]
                        print("\nSOCO NA CARA ", player_move, " damage.")
                        time.sleep(1)
                    elif player_move in ("2", "Soco Mais forte"):
                        player_move = moves_player["Soco Mais forte"]
                        print("\nMEGA SOCO NA CARA", player_move, " damage.")
                        time.sleep(1)
                    elif player_move in ("3", "Recuperar vida"):
                        heal_up = True
                        player_move = moves_player["Recuperar vida"]
                        print("\nRECUPEROU VIDA", player_move, " Recuperar vida.")
                        time.sleep(1)
                    else:
                        print("\nTente novamente")
                        time.sleep(1)
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
                    time.sleep(1.5)
                else:
                    if computer_health > 30: 
                        if player_health > 75:
                            computer_move = moves_computer["Soco"]
                            print("\n O computador usou SOCO NA CARA ", computer_move, " damage.")
                            time.sleep(1.5)
                        elif player_health > 35 and player_health <= 75: 
                            imoves = ["Soco", "Soco Mais forte"]
                            imoves = random.choice(imoves)
                            computer_move = moves_computer[imoves]
                            print("\nO computador deu Soco Mais forte ", imoves, ". It dealt ", computer_move, " damage.")
                            time.sleep(1.5)
                        elif player_health <= 35:
                            computer_move = moves_computer["Soco Mais forte"]
                            print("\nO computador deu um Soco Mais forte ", computer_move, " damage.")                       
                            time.sleep(1.5)
                    else:#se tiver com pouca vida 50% de recuperar vida
                        heal_or_fight = random.randint(1,2) 
                        if heal_or_fight == 1:
                            heal_up = True
                            computer_move = moves_computer["Recuperar vida"]
                            print("\nO computador utilizou Recuperar vida. ", computer_move, " health.")
                            time.sleep(1.5)
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
                    if player_health > 100:
                        player_health = 100 #vida nao passa de 100
                else:
                    computer_health += computer_move
                    if computer_health > 100:
                        computer_health = 100
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
            time.sleep(1)       
        else:
            print("\nPlayer health: ", player_health, "Computer health: ", computer_health)
            print("\nSEUS OPONENTE GANHOU!! MAIS SORTE DA PROXIMA VEZ!!.")
            time.sleep(1)

        print("\nVOCE QUER CONTINUAR CAMINHANDO?")

        answer = input("> ").lower()
        if answer not in ("Sim", "s","sim","S"):
            play_again = False

main()