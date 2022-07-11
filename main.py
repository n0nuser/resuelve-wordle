from limit_word import get_words

WORDS_DIRECTORY = "./words/"
MAX_LETTERS = 5
RETRIES = 6


def main():
    existent_letters = set()
    inexistent_letters = set()
    word_text = "\nIntroduce la palabra que has intentado. e.g: 'vocal': "
    good_positions_text = "Introduce las posiciones de las letras correctas, separadas por una coma. e.g: '1,4': "
    incorrect_positions_text = (
        "Introduce las posiciones de las letras correctas pero en otra posición, separadas por una coma. e.g: '2,5': "
    )
    while True:
        words = get_words(WORDS_DIRECTORY, MAX_LETTERS)

        input_word = input(word_text).lower()

        good_positions = input(good_positions_text)
        good_positions = {(int(i) - 1) for i in good_positions.split(",") if good_positions}
        good_positions_letters = {input_word[i] for i in good_positions}

        incorrect_positions = input(incorrect_positions_text)
        incorrect_positions = {(int(i) - 1) for i in incorrect_positions.split(",") if incorrect_positions}
        incorrect_positions_letters = {input_word[i] for i in incorrect_positions}

        existent_letters = existent_letters.union(good_positions_letters.union(incorrect_positions_letters))
        inexistent_letters = inexistent_letters.union(set(input_word).difference(existent_letters))

        print(f"Letras existentes: {existent_letters}")
        print(f"Letras inexistentes: {inexistent_letters}")

        # Remove word from the list as it was used
        words.discard(input_word)

        # Filter words with good positions
        for i in good_positions:
            words = {word for word in words if word[i] == input_word[i]}

        # Filter words with incorrect positions
        for i in incorrect_positions:
            words = {word for word in words if input_word[i] in word}

        # Remove words with letters that doesn't exist
        for letter in inexistent_letters:
            words = {word for word in words if letter not in word}

        print(f"\nPosibles palabras:\n{words}")
        if input("\n¿Has ganado? (y/n): ").lower() == "y":
            break


if __name__ == "__main__":
    main()
