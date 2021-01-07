"""Word Finder: finds random words from a dictionary."""
import random
from wordfinder import WordFinder


class RandomWordFinder(WordFinder):
    def __init__(self, list):
        super().__init__(read_file, txt_list, parse_list)
        print(f'{len(self.txt_list)} words read')
        print(f'{self.txt_list}')

    def parse_list(self, txt):
        for line in txt:
            line = line.strip()
            self.txt_list.append(line)

    def random(self):
        return random.choice(self.txt_list)
