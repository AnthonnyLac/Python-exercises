"""
Exercício 2 - Jogo da Velha nxn

Estratégia:
- É perguntado em que tamanho o usuario deseja construir seu tabuleiro (tableSize)
- É iniciado um tabuleiro vazio tableSizextableSize.
- Varia as jogadas entre os jogadores 'X' e 'O'.
- É solicitado a entrada do usuario para linha e coluna que deseja preencher.
-É verificado se o movimento é permitido e em seguida atualiza o tabuleiro.
- Verifica se algum jogador venceu ou se teve velha.
- ocorre um while true até que o jogo termine.

Estruturas usadas:
- Lista de listas para representar o tabuleiro.
"""

def BuildTable(tableSize):
    """
    Inicializa uma tabela vazia para o jogo da velha.
    """
    board = [[' ' for _ in range(tableSize)] for _ in range(tableSize)]
    return board

def PrintTable(board):
    """
    Imprime a tabela atual do jogo.
    """
    for row in board:
        print(' | '.join(row))
        print('-' * (4 * len(row) - 1))

def CheckVictory(board, player):
    """
    Verifica se o "x" ou "o" venceu o jogo.
    """
    
    def CheckLines(line):
        return all(cell == player for cell in line)
    
    # Verificação de colunas
    for col in range(len(board[0])):
        if CheckLines([board[row][col] for row in range(len(board))]):
            return True
        
    # Verificação de linhas
    for row in board:
        if CheckLines(row):
            return True


    # Verificação na transversal
    if CheckLines([board[i][i] for i in range(len(board))]) or CheckLines([board[i][len(board) - 1 - i] for i in range(len(board))]):
        return True

    return False

def main():
    tableSize = int(input("Digite o tamanho desejado para um tabuleiro quadrado : "))
    board = BuildTable(tableSize)
    player = 'X'

    print(f"Bem-vindo ao Jogo da Velha {tableSize}x{tableSize}!")
    
    while True:
        PrintTable(board)
        lineColumSize = len(board) - 1
        
        row = int(input(f'O {player}, escolha a linha (0-{lineColumSize}): '))
        col = int(input(f'O {player}, escolha a coluna (0-{lineColumSize}): '))

        if 0 <= row < tableSize and 0 <= col < tableSize and board[row][col] == ' ':
            board[row][col] = player
        else:
            print("Movimento não permitido, tente novamente!")
            continue

        if CheckVictory(board, player):
            PrintTable(board)
            print(f"O Jogador {player} venceu!")
            break

        if ' ' not in [cell for row in board for cell in row]:
            CheckVictory(board)
            print("Velha!")
            break

        if player == 'X':
            player = 'O'
        else:
            player = 'X'

if __name__ == "__main__":
    main()
