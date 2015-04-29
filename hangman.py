# Game of Hangman.  First, get the logic.  Next, build a text
# file with a number of words that can be randomly chosen.

import sys

def guess_letter(word):
  letter = raw_input("Guess a letter!")
  data = []
  if letter in word:
    data[0] = True
  else:
    data[0] = False
  return

def draw_image(word):
  
  board = ['  ______', '  |    |', '  |', '  |', '  |', '  |', '  |',
    '  |', '__|__', '|___|']
  loserbrd = ['  |    O', '  |    |', '  |   ~|', '  |   ~|~', '  |    ^', 
    '  |   ~|~    YOU LOSE!']
  if num_wrong >= 1:
    board[2] = loserbrd[0]
  if num_wrong >= 2:
    board[3] = loserbrd[1]
  if num_wrong >= 3:
    board[3] = loserbrd[2]
  if num_wrong >= 4:
    board[3] = loserbrd[3]
  if num_wrong >= 5:
    board[4] = loserbrd[4]
    board[3] = loserbrd[5]
    game_over=True
  
  print '\n\n\n\n'
  for n in range(len(word)):
    sys.stdout.write('_ ')
  print '\n\n'
  for n in range(10):
    print board[n]
    
  guess_letter(word)
  

def pick_word():
  return raw_input("Please enter a word:")

def main():
  word = pick_word()
  draw_image(word)
  
  
  
  

if __name__ == '__main__':
  main()
