# cli-games
Fun little games that can be played entirely on the command line!

## Hangman
Play Hangman on the command line with multiple difficulties!

##### Difficulties
-Easy: Get 6 tries to get the full word
-Medium: Get 4 tries to get the full word
-Hard: Get 4 tries to get the full word but there's no incorrect letter bank

##### Words
By default it uses default.txt you can supply another one of our lists (countries.txt and states.txt) or provide a list of your own!
The words file should be one word per line, supply it when calling the command as follows: `python3 hangman.py -f file.txt`
-default.txt: 10000 most common english words (US spelling), with some not nice words removed
-countries.txt: 193 UN member states + 2 UN non-member observer states
-states.txt: 50 states of the US

## Tic Tac Toe
A game of tic-tac-toe where you play against the code. Warning: you can't win.