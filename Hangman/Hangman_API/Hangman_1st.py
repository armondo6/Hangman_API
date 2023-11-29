import random
import requests
import json
import string

# word -> hanged -> isWordGuessed -> getAvailable -> getWordGuessed -> hangman

# Function to pull a random word from a list of words using API

def word():

   url = "https://wordsapiv1.p.rapidapi.com/words/"

   querystring = {"random" : "true"}

   headers = {
         'X-RapidAPI-Key' : 'c6a7192fc9msh4931c462d8c53c4p1ced90jsn45cd3d660151',
         'X-RapidAPI-Host' : 'wordsapiv1.p.rapidapi.com'
      }
   response = requests.get(
            url,
            headers=headers,
            params = querystring
      )
   word = json.loads(response.text)["word"]
   pass
   return word
# Game graphics
def hanged(man):
    graphic = [
    '''
       +------+
       |
       |
       |
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |      |
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|-
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|-
       |     /
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|-
       |     / \\
       |
    ==============
    '''
    ]
    return graphic[man]


# -----------------------------------

def isWordGuessed(secretWord, lettersGuessed):
    
   count = 1
    # Add code here
   for i in lettersGuessed:
      if i in secretWord:     
         count += 1 
   if count == len(secretWord):
      return True
   else:
      return False
print(isWordGuessed("baboon","abobno"))


def getGuessedWord(secretWord, lettersGuessed):
    
   correctGuesses = []
   for i in lettersGuessed:
      if i in secretWord:
         correctGuesses.append(i)
   outputString = ''
   for i in secretWord:
      if i in correctGuesses:
         outputString += i
      else: 
         outputString += "_"
   return outputString


  
def getAvailableLetters(lettersGuessed):
     
     # FIXME - lettersGuessed: list, what letters have been guessed so far
               #Returns: string, comprised of letters that represents what letters have not
                 #yet been guessed.
    

    alphabet=list(string.ascii_lowercase)
    for i in lettersGuessed:
       alphabet.remove(i)
    return ''.join(alphabet)

def hangman(secretWord):
   print("there are" + str(len(secretWord)) + "letters in the secretword")  
     #FIXME - Takes one parameter - secretWord: string, the secret word to guess.

 #    Starts up an interactive game of Hangman.

 #    (1) At the start of the game, let the user know how many
 #     letters the secretWord contains.

 #    (2) Ask the user to supply one guess (i.e. letter) per round.

 #    (3) The user should receive feedback immediately after each guess
 #     about whether their guess appears in the computers word.

#     (4) After each round, you should also display to the user the
#       partially guessed word so far, as well as letters that the
#       user has not yet guessed.

#     Follows the other limitations detailed in the problem write-up.
#     '''
   print("Welcome to the game, Hangman!")

#     # FIXME - Write your print statement according to the explanation (1)

   global lettersGuessed
   mistakeMade=0
   lettersGuessed=[]
   letters = "abcdefghijklmnopqrstuvwxyz"
   while 6 - mistakeMade > 0:
      if isWordGuessed(secretWord,lettersGuessed):
         print("-------------")
         print("Congradulations!!! You won the game :).")
         break
        # FIXME - Create an if statement to check if the player has won the game.
#             print("-------------")
#             print("Congratulations, you won!")
#             # FIXME - Break the loop.

      else:
            print("-------------")
            print("You have", 6-mistakeMade, "guesses left.")
            print("You have" + getAvailableLetters(lettersGuessed) + "left")
             
            print(hanged(mistakeMade))
            
            
            guess = str(input("input your guess here")).lower()
            if not len(guess) == 1:
                  print("input ONE letter you silly baca")
            if guess in lettersGuessed:
               print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed))
            elif guess in secretWord and guess not in lettersGuessed:
               lettersGuessed.append(guess)
               print("your letter is in the word :)" + getGuessedWord(secretWord, lettersGuessed))
            else:
               lettersGuessed.append(guess)
               mistakeMade += 1
               print( getGuessedWord(secretWord, lettersGuessed) + "That is  wrong. im disappointed in you")
               
                              
                    
             
#             # FIXME - If the user input is more than one letter, tell them to guess again with only one letter.

#             # FIXME - Create an if statement to check if the player already guessed a letter.
#               # FIXME - Create a print statement to tell the player that they have already guessed that letter.

#             # FIXME - Create an elif statement to check if the guessedletter is in the word and has not been guessed before.
#               # FIXME - Append that letter to the lettersGuessed list.
#               # FIXME - Create a print statement to tell the player that it was a good guess, including the guessed word.

#            else:
#                 # FIXME - Append to letter to the lettersGuessed list.
 #                # FIXME - Increment mistakeMade by 1.
#               # FIXME - Create a print statement to tell the player that the guessed word is not in the word, including the guessed word.

#     print("-------------")
#     print(hanged(6))
 #    print("Sorry, you ran out of guesses. The word was:",secretWord)

secretWord = word()
hangman(secretWord)
