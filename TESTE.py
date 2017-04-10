
import random
import time

def main():
    """Main function that will welcome the player to the game."""

    Nome_jogador=str(input("Selecione o nome do seu personagem  "))
    print("\n\nOla, {0}".format(Nome_jogador))
    if input()=="":
        print("\nBem vindo ao inspermon!! ")
    time.sleep(1.5)
    if input()=="":
        print("Antes de adentrar o Insper, voce deve estar ciente das regras do jogo ")
    time.sleep(3)
    if input()=="":
        print("Funciona assim cada dia de insper voce podera escolher oque voce gostaria de fazer \r Por exemplo ir estudar\n Ou ir relxar um pouco")
    time.sleep(3)
    if input()=="":
        print("Logico cada ponto tem suas vantagens.\r Se voce escolher estudar, voce melhora suas capacidades")
    time.sleep(3)
    if input()=="":
        print("Porem o jogo nao e tao facil assim!!\r Ao caminhar pelo Insper voce podera se deparar com outros Inspermons e tera de batalhar com eles.")
    time.sleep(3)
    play_again = True
    # Set up the play again loop
    while play_again:
        winner = None
        player_health = 100
        computer_health = 100

        # determine whose turn it is
        turn = random.randint(1,2) # heads or tails
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

        # set up the main game loop
        while (player_health != 0 or computer_health != 0):

            heal_up = False # determine if heal has been used by the player. Resets false each loop.
            miss = False # determine if the chosen move will miss.

            # create a dictionary of the possible moves and randomly select the damage it does when selected
            moves = {"Soco": random.randint(18, 25),
                     "Soco Mais forte": random.randint(10, 35),
                     "Recuperar vida": random.randint(20, 25)}

            if player_turn:
                print("\nSelecione seu movimento :\n1. Soco (damage between 18-25)\n2. Soco Mais Forte (damage between 10-35)\n3. Recuperar Vida (between 20-25 health)\n")

                player_move = input("> ").lower()

                move_miss = random.randint(1,5) # 20% of missing
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    player_move = 0 # player misses and deals no damage
                    print("Errou!")
                    time.sleep(1)
                else:
                    if player_move in ("1", "Soco"):
                        player_move = moves["Soco"]
                        print("\nSOCO NA CARA ", player_move, " damage.")
                        time.sleep(1)
                    elif player_move in ("2", "Soco Mais forte"):
                        player_move = moves["Soco Mais forte"]
                        print("\nMEGA SOCO NA CARA", player_move, " damage.")
                        time.sleep(1)
                    elif player_move in ("3", "Recuperar vida"):
                        heal_up = True # heal activated
                        player_move = moves["Recuperar vida"]
                        print("\nRECUPEROU VIDA", player_move, " Recuperar vida.")
                        time.sleep(1)
                    else:
                        print("\nTente novamente")
                        time.sleep(1)
                        continue

            else: # computer turn

                move_miss = random.randint(1,5)
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    computer_move = 0 # the computer misses and deals no damage
                    print("O computador Errouu!")
                    time.sleep(1.5)
                else:
                    if computer_health > 30: 
                        if player_health > 75:
                            computer_move = moves["Soco"]
                            print("\n O computador usou SOCO NA CARA ", computer_move, " damage.")
                            time.sleep(1.5)
                        elif player_health > 35 and player_health <= 75: # computer decides whether to go big or play it safe
                            imoves = ["Soco", "Soco Mais forte"]
                            imoves = random.choice(imoves)
                            computer_move = moves[imoves]
                            print("\nO computador deu Soco Mais forte ", imoves, ". It dealt ", computer_move, " damage.")
                            time.sleep(1.5)
                        elif player_health <= 35:
                            computer_move = moves["Soco Mais forte"] # FINISH HIM!
                            print("\nO computador deu um Soco Mais forte ", computer_move, " damage.")                       
                            time.sleep(1.5)
                    else: # if the computer has less than 30 health, there is a 50% chance they will heal
                        heal_or_fight = random.randint(1,2) 
                        if heal_or_fight == 1:
                            heal_up = True
                            computer_move = moves["Recuperar vida"]
                            print("\nO computador utilizou Recuperar vida. ", computer_move, " health.")
                            time.sleep(1.5)
                        else:
                            if player_health > 75:
                                computer_move = moves["Soco"]
                                print("\nO computador utilizou Soco.", computer_move, " damage.")
                                time.sleep(2.5)
                            elif player_health > 35 and player_health <= 75:
                                imoves = ["Soco", "Soco Mais forte"]
                                imoves = random.choice(imoves)
                                computer_move = moves[imoves]
                                print("\nO computador utilizou Soco Mais forte", imoves, ". It dealt ", computer_move, " damage.")
                                time.sleep(2.5)
                            elif player_health <= 35:
                                computer_move = moves["Soco Mais forte"] # FINISH HIM!
                                print("\nO computador utulizou Soco Mais forte. Para finalizar ", computer_move, " damage.")
                                time.sleep(2.5)
            if heal_up:
                if player_turn:
                    player_health += player_move
                    if player_health > 100:
                        player_health = 100 # cap max health at 100. No over healing!
                else:
                    computer_health += computer_move
                    if computer_health > 100:
                        computer_health = 100
            else:
                if player_turn:
                    computer_health -= player_move
                    if computer_health < 0:
                        computer_health = 0 # cap minimum health at 0
                        winner = "Player"
                        break
                else:
                    player_health -= computer_move
                    if player_health < 0:
                        player_health = 0
                        winner = "Computer"
                        break

            print("\nPlayer health: ", player_health, "Computer health: ", computer_health)

            # switch turns
            player_turn = not player_turn
            computer_turn = not computer_turn

        # once main game while loop breaks, determine winner and congratulate

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