# Game of Hangman.  First, get the logic.  Next, build a text
# file with a number of words that can be randomly chosen.
# a bit of nothing here to change the file.

word = '' # secret word
display_word = '' # word to display
num_wrong = 0 # number of wrong guesses
guessed = [] # list of guessed letters
board = ['  ______', '  |    |', '  |', '  |', '  |',
          '  |', '  |', '  |', '__|__', '|___|']
loserbrd = ['  |    O', '  |    |', '  |   ~|', '  |   ~|~',
          '  |    ^',  '  |   ~|~    YOU LOSE!']
game_over = False

def guess_letter():
  global game_over
  global guessed
  global num_wrong

  letter = raw_input("Guess a letter! ")

  if letter in guessed:
    print "you already guessed that!"

  elif len(letter) != 1:
    print "that's not a letter"

  else:
    guessed.append(letter[0])

    updateDisplayWord()

    if letter in word:
      print "guessed right!"

    else:
      num_wrong = num_wrong + 1
      if num_wrong >= 5:
        game_over = True

def updateDisplayWord():
  global display_word
  display_word = ''

  for letter in word:
    if letter in guessed:
      display_word += letter
    else:
      display_word += '_'

def draw_image():
  global board
  global loserbrd

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

  for n in range(10):
    print board[n]

  global display_word
  print display_word

def pick_word():
  return raw_input("Please enter a word: ")

def main():
  global word
  word = pick_word()
  while game_over == False:
    guess_letter()
    draw_image()

if __name__ == '__main__':
  main()
