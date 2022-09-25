import random


class Hangman:
    def __init__(self, list_words):
        self._list_words = list_words
        self.word = None

    def _menu(self):
        try:
            difficulty = int(input("""
1. Noob: Infinity chance.
2. Mid: Five chance.
3. Pro: Three chance.

>>"""))
            match difficulty:
                case 1:
                    return self.levels(difficulty)
                case 2:
                    return self.levels(difficulty)
                case 3:
                    return '3'

        except Exception as e:
            return e

    def _getwords(self):
        self.word = [i for i in random.choices(self._list_words)]

        for record in self.word:
            size_word = len(record)
            first_letter = record[0]
            last_letter = record[-1]

        return f'Size:{size_word}. First Letter:{first_letter}. Last Letter:{last_letter}.'

    def levels(self, case):
        if case == 1:
            complete_word = input(f'{self._getwords()}\nComplete the word: ')
            word = []
            for record in self.word:
                w = record
                letter = list(record)
                while True:
                    next_letter = [rec for rec in letter if rec == complete_word]
                    if next_letter:
                        for i in next_letter:
                            word.append(i)
                            letter.remove(i)
                        if len(letter) == 0:
                            return f'Correct word: {w}'
                        else:
                            complete_word = input(f'Correct letter: {word}\nComplete the word: ')
                    else:
                        complete_word = input('Complete the word: ')
        if case == 2:
            complete_word = input(f'{self._getwords()}\nComplete the word: ')
            word = []
            for record in self.word:
                w = record
                letter = list(record)
                i = 1
                while i < 5:
                    next_letter = [rec for rec in letter if rec == complete_word]
                    if next_letter:
                        for rec in next_letter:
                            word.append(rec)
                            letter.remove(rec)
                        if len(letter) == 0:
                            return f'Correct word: {w}'
                        else:
                            complete_word = input(f'Correct letter: {word}\nComplete the word: ')
                    else:
                        i += 1
                        complete_word = input('Complete the word: ')
                else:
                    return 'You lose'
        if case == 3:
            complete_word = input(f'''{self._getwords()}\nComplete the word: ''')
            word = []
            for record in self.word:
                w = record
                letter = list(record)
                i = 1
                while i < 3:
                    next_letter = [rec for rec in letter if rec == complete_word]
                    if next_letter:
                        for rec in next_letter:
                            word.append(rec)
                            letter.remove(rec)
                        if len(letter) == 0:
                            return f'Correct word: {w}'
                        else:
                            complete_word = input(f'Correct letter: {word}\nComplete the word: ')
                    else:
                        i += 1
                        complete_word = input('Complete the word: ')
                else:
                    return 'You lose'


if __name__ == '__main__':
    a = ['watch', 'theory', 'strategy', 'remember']
    run = Hangman(a)
    print(run._menu())
    # print(test._getwords())


