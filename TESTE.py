
import random
import time
import json
# import winsound
# winsound.PlaySound('Pokemon Sound Effect.mp3', winsound.SND_FILENAME)
#window size= 80-width   15-height
with open('inspermonscommon.json') as arquivo:
    inspermons = json.load(arquivo)
    # for ipmon in inspermons:
    #     mostra_ipmon(ipmon)
def dormir():
    print("Sua vida esta regenerando!")
    print("....")
    time.sleep(2)
    print( "\n {0}".format(mostra_ipmon(inspermons)))
    time.sleep(3)
    return inspermons[0]['vida']
def mostra_ipmon(inspermons):
    print("Inspermon : {0}".format(inspermons[0]["nome"]))
    print("poder = {0}".format(inspermons[0]["poder"]))
    print("vida = {0}".format(inspermons[0]["vida"]))
    print("defesa = {0}".format(inspermons[0]["defesa"]))
    print("Inspercash = {0}\n".format(inspermons[0]["Inspercash"]))
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
        print("Funciona assim cada dia de insper voce podera escolher \noque voce gostaria de fazer: \n   Por exemplo passear \n   Ou ir dormir um pouco")
    if input()=="":
        print("Logico cada ponto tem suas vantagens.\n Se voce escolher passear, voce melhora suas capacidades.\n Ja se voce decidir domir voce recupera sua vida.")
    if input()=="":
        print("Porem o jogo nao e tao facil assim!!\n Ao caminhar pelo Insper voce podera se deparar com outros Inspermons e tera de batalhar com eles.")
    if input()=="":
        print("Voce esta preparado??")
    if input()=="":

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
            moves_player = {"Soco": inspermons[0]['poder'] - inspermons[sorte]['defesa'],
                     "Soco Mais forte": inspermons[0]['Soco Mais forte'] - inspermons[sorte]['defesa'],
                     "Recuperar vida": random.randint(inspermons[0]['vida']*0.1,inspermons[0]['vida']*0.15 ),
                     "Fugir da Batalha": winner==None}
            moves_computer = {"Soco": inspermons[sorte]['poder'] - inspermons[0]['defesa'],
                     "Soco Mais forte": inspermons[sorte]['Soco Mais forte'] - inspermons[0]['defesa'],
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
                    if player_health > inspermons[0]['vida']:
                        player_health = inspermons[0]['vida'] #vida nao passa do maximo
                else:
                    computer_health += computer_move
                    if computer_health > inspermons[sorte]['vida']:
                        computer_health = inspermons[sorte]['vida']
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
            print("Selecione oque voce deseja fazer:\n1.Ir dormir(recupera a vida do seu inspermon)\n2.Salvar o jogo\n3.Parar de jogar")
            answer2 = input(">")
            if answer2 == "1":
                dormir()
                print ("Deseja voltar a passear?")
                answer = input("> ").lower()
                if answer in ("Sim", "s","sim","S"):
                    play_again = True
                continue
            if answer2 == "2":
                salvarjogo()
            if answer2 == "3":
                break
            else:
                print("tente denovo")
                continue


main()