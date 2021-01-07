import random


class WordFinder:
    """Word Finder: finds random words from a dictionary.

    1. Example text file contains: horse, snake, monkey
    2. parse_list will create a list of the elements in the text file
    3. WordFinder.random() returns a random animal in list [horse, snake, monkey]

    """

    def __init__(self, list):
        self.read_file = open(list)
        self.txt_list = []
        self.parse_list(self.read_file)
        print(f'{len(self.txt_list)} words read')
        print(f'{self.txt_list}')

    def __repr__(self):
        return f"WordFinder list={self.txt_list}"

    def parse_list(self, txt):
        for line in txt:
            line = line.strip()
            self.txt_list.append(line)

    def random(self):
        return random.choice(self.txt_list)


class AdvancedWordFinder(WordFinder):
    """Word Finder: finds random words from a dictionary.

    1. Example text file contains: horse, snake, monkey, , #reptile, #canine
    2. parse_list will create a list of the elements in the text file
        a. this method will also remove any empty strings and words that contain "#"
    3. WordFinder.random() returns a random animal in list [horse, snake, monkey]

    """

    def __repr__(self):
        return f"AdvancedWordFinder list={self.txt_list}"

    def parse_list(self, txt):
        for line in txt:
            line = line.strip()
            if '#' not in line and line:
                self.txt_list.append(line)
