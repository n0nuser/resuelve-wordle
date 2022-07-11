from os import listdir
from os.path import isfile, join


def get_words(directory: str, max_letters: int) -> set:
    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    onlyfiles.sort()

    words = set()

    for file in onlyfiles:
        with open(directory + file, "r") as f:
            for line in f:
                word = line.strip()
                if len(word) == max_letters:
                    word = word.replace("á", "a")
                    word = word.replace("é", "e")
                    word = word.replace("í", "i")
                    word = word.replace("ó", "o")
                    word = word.replace("ú", "u")
                    words.add(word)

    return words


if __name__ == "__main__":
    MAX_LETTERS = 5
    DIRECTORY = "./words/"
    get_words(DIRECTORY, MAX_LETTERS)
