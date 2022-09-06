# Hangman 

> A Hangman Game that asks the user for a letter and checks if it is in the word. It starts with a default number of lives and a random word from the word_list. we used python program language to develop this project.

## Milestone 1

- we have setup github repository dedicated to the project in this Milestone.

## Milestone 2
- we have written the code in order to ask input from the user.
```python
""" def ask_letter(self) :
        '''
        while True:
            self.letter = input("Enter a single letter: ")
            if len(self.letter) > 1:
                print("Please, enter just one character")
            elif self.letter.isalpha() is False:
                print('Only alphabets please')
            elif self.letter in self.list_letters:
                print(f"{self.letter} was already tried, choose again")
            elif len(self.letter) == 1:
                break  
            else:
                print('Please, enter a chracter')
        return self.letter"""
```

## Milestone 3

- we have defined initializer in this milestone.
```python
""" def __init__(self, word_list, num_lives=5):
        # 1. "The mystery word has {len(self.word)} characters" (The number of letters is NOT the UNIQUE number of letters)
        # 2. {word_guessed}
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        print(f"The mystery word has {len(self.word)} characters")
        self.word_guessed= []
        for letters in (self.word):
            self.word_guessed.append('_')
        print(self.word_guessed)
        self.num_letters = len(set(self.word))
        self.list_letters = []
"""
```
## Milestone 4
- we have to check that user has given a valid input. which can be done by the following code.
```python 
""" while True:
            self.letter = input("Enter a single letter: ")
            if len(self.letter) > 1:
                print("Please, enter just one character")
            elif self.letter.isalpha() is False:
                print('Only alphabets please')
            elif self.letter in self.list_letters:
                print(f"{self.letter} was already tried, choose again")
            elif len(self.letter) == 1:
                break  
            else:
                print('Please, enter a chracter')
        return self.letter
"""
```
- finally, the working of the finished project's game play output can be seen below,
```
The mystery word has 5 characters
['_', '_', '_', '_', '_']
Enter a single letter: p
Enter a single letter: w
Sorry, w is not in the word.
You have 4 lives left.
Enter a single letter: l
Enter a single letter: k
Sorry, k is not in the word.
You have 3 lives left.
Enter a single letter: o
Sorry, o is not in the word.
You have 2 lives left.
Enter a single letter: 0
Only alphabets please
Enter a single letter: pp
Please, enter just one character
Enter a single letter: i
Sorry, i is not in the word.
You have 1 lives left.
Enter a single letter: d
Sorry, d is not in the word.
You have 0 lives left.
you ran out of lives, the word was apple
```
## Conclusions

- we can improve the project by adding additonal functionalities to the code and minimising the runtime simultaniously.
- thank you for going through my project.
