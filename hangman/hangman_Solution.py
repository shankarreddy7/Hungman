'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        # 1. "The mystery word has {len(self.word)} characters" (The number of letters is NOT the UNIQUE number of letters)
        # 2. {word_guessed}
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        print(f'The mystery word has {len(self.word)} characters')
        self.word_guessed= []
        for letters in (self.word):
            self.word_guessed.append('_')
            print(self.word_guessed)
            self.num_letters = len(set(self.word))
            self.list_letters = []
    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        inputs= self.ask_letter()
        self.list_letters.append(inputs)
        for i, l in enumerate(self.word):
            if inputs.lower() ==1:
                self.word_guessed[i] =1
                self.num_letters -=1
                print(f'Nice! {letter} is in the word!')
                print('_'.join(self.word_guessed))
            elif inputs  not in self.word:
                print(f'Sorry, {letter} is not in the word.')
                self.list_letters.append(inputs)
                self.num_lives -= 1
                print(f'You have {num_lives} lives left.')
                break
            if '_' not in self.word_guessed:
                print("congratulations! You've won.")
                break
            if self.num_lives == 0:
                print(f'you ran out of lives, the word was {self.word}')

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        while True:
            self.letter = input("Enter a single letter : ")
            if len(self.letter) > 1:
                print("please, enter just one charecter")
            elif self.letter in self.List_letters :
                    print(f'{self.letter} was already tried')
        return self.letter

def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    while game.num_lives > 0 and game.num_letters > 0:
        game.check_letter()
    
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations, you won!"
    # If the user runs out of lives, print "You ran out of lives. The word was {word}"


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
