import random

def LoadWordList(fileName):
    """
    Carrega a lista de palavras a partir de um txt.
    :param fileName: Nome do arquivo de palavras presente no repositório.
    :return: Lista de palavras.
    """
    with open(fileName, 'r') as file:
        wordList = [line.strip().lower() for line in file]
    return wordList

def ChooseWord(wordList):
    """
    Escolhe uma palavra aleatória da lista.
    :param wordList: Lista de palavras.
    :return: Palavra escolhida aleatoriamente.
    """
    return random.choice(wordList)

def DisplayWord(word, guesses):
    """
    Exibe a palavra com letras adivinhadas nas posições corretas e "_" para letras não adivinhadas.
    :param word: Palavra a ser adivinhada.
    :param guesses: Letras adivinhadas.
    :return: Texto representando a palavra.
    """
    display = ''
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += '_'
    return display

def main():
    wordList = LoadWordList('lista_palavras.txt')
    wordGuess = ChooseWord(wordList)
    guessedLetters = []
    attempts = 6

    print("Bem-vindo ao Jogo inspirado no Term.ooo!")

    while attempts > 0:
        print(f"\nPalavra a ser adivinhada: {wordGuess}")
        displayedWord = DisplayWord(wordGuess, guessedLetters)
        print(displayedWord)
        print(f"Tentativas restantes: {attempts}")
        guess = input(f"Digite uma palavra de {len(wordGuess)} letras: ").lower()

        if len(guess) != len(wordGuess):
            print(f"Palavra incorreta. Deve ter {len(wordGuess)} letras.")
            continue

        if sorted(guess) == sorted(wordGuess):
            print(f"Acertou! A palavra era: {wordGuess}")
            break
        else:
            print("Palavra errada. Tente novamente.")
            attempts -= 1

        # Atualiza as letras corretas adivinhadas
        for letter in guess:
            if letter in wordGuess and letter not in guessedLetters:
                guessedLetters.append(letter)

    if attempts == 0:
        print(f"Você perdeu! A palavra era: {wordGuess}")

if __name__ == "__main__":
    main()
