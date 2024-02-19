"""
the design was made for the replit console so sorry if it looks worse here

a lot of the code is kinda sloppy ngl so feel free to change it if you know a better way to do it :D
"""

import random

possible_words = ["hangman", "lazy"]
game_end = False

# choose word
word = random.choice(possible_words)
display_word = ["_"]*len(word)

# set lives
lives = "X X X X X X"
# set wrong letters
wrong_letters = ""

# loops for each turn
while game_end != True:
  # top bar
  print("Lives: " + lives + "        Wrong Letters: " + wrong_letters + "\n")
  display_word_string = ""
  for i in range(len(display_word)):
    display_word_string += display_word[i] + " "

  print(display_word_string + "\n")

  guess = input("Guess a letter: ")
  guess = guess.lower()
  if ord(guess) < 97 or ord(guess) > 122:
    print("Not Valid Option")
  else:
    # check if guess is in word
    if guess in word:
      display_word[word.index(guess)] = guess
    else:
      lives = lives[0:len(lives)-2]
      if len(wrong_letters) >= 1:
        wrong_letters += ", " + guess
      else:
        wrong_letters += guess

    # separation border
    print("\n" + ("-"*56) + "\n")
    
    if "X" not in lives:
      print("\nGame Over. The word was " + word)
      game_end = True
  
    if "_" not in display_word:
      print("\nYou win! The word was " + word)
      game_end = True
