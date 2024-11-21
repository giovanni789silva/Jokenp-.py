player1 = str(input("Escolha Pedra, papel ou tesoura: ")).upper()
player2 = str(input("Escolha pedra, papel ou tesoura: ")).upper()

if (player1 == "pedra" and player2 == "tesoura") or (player1 == "tesoura" and player2 == "papel") or (player1 == "papel" and player2 == "pedra"):
    print("Player 1 ganhou!")

elif (player2 == "pedra" and player1 == "tesoura") or (player2 == "tesoura" and player1 == "pedra") or (player2 == "papel" and player2 == "pedra"):
    print("Player 2 ganhou!")

elif player1 == player2:
    print("Empate!")

else:
    print("Digite uma condição válida!")