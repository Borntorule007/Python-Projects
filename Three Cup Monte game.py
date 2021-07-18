mylist = [' ','O',' ']

def shuffle_list(mylist):
  from random import shuffle
    # Take in list, and returned shuffle versioned
    shuffle(mylist)
    return mylist
  
shuffle_list(mylist)

def player_guess():
    
  guess = ''
    
  while guess not in ['0','1','2']:      
  # Recall input() returns a string
    guess = input("Pick a number: 0, 1, or 2:  ")
    
  return int(guess)  
  
def check_guess(mylist,guess):
  if mylist[guess] == 'O':
      print('Correct Guess!')
  else:
      print('Wrong! Better luck next time')
      print(mylist)
        
# Initial List
mylist = [' ','O',' ']

# Shuffle It
mixedup_list = shuffle_list(mylist)

# Get User's Guess
guess = player_guess()

# Check User's Guess
check_guess(mixedup_list,guess)
