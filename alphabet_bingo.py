import random
import time

ABC = [ chr(x) for x in range(91) if 64 < x < 91 ]


def bingo(L):
    """
    plays bingo by giving out random items from the provided list (L)
    in my example, L is a list of every capital letter of the alphabet
    """
    print ' '
    user = raw_input('Do you want to play? (y/n, lowercase)')
    print ' '
    if L == []:
      print 'Blackout!'
    elif user == 'y':
        choice = random.choice(L)
        print choice
        L = remove(choice, L)
        time.sleep(5.0)
        return bingo(L)
    else:
        print 'See you next time!'


def ind(e, L):
  """ input: e is a single element
      L is a string or other list
      output: the index at which e is first found in L
      if is is not an element of L, output is just the length of L
  """
  if e not in L:
    return len(L)
  elif e == L[0]:
    return 0
  else:
    return 1 + ind(e, L[1:])
    
    

def remove(e, L):
    """
    e is an element that resides in list L
    removes e from L and returns the updated list
    """
    index = ind(e, L)
    return L[:index] + L[index+1:]
    

bingo(ABC)
