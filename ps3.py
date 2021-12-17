# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string
import os
os.chdir('C:\\Users\\User\\Desktop\\дкр 2.0.13.12')

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    sum=0
    word=str(word)
    lst_word=list(word.lower())
    for i in lst_word:
        if i!='*':
            sum+= SCRABBLE_LETTER_VALUES[i]
    a1=1
    mark=0
    a2=7*len(word)-3*(n-len(word))
    if a1>a2:
        mark=sum*a1
    else:
        mark=sum*a2
    return  mark

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    vail_w=[]
    for letter in hand.keys():
        for j in range(hand[letter]):
            vail_w.append(letter)
    vail_w_hand=' '.join(vail_w)
    return vail_w_hand
    

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))-1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n-1):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    hand['*']=1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    k={}
    h=hand.copy()
    lst1=h.keys()
    word=str(word.lower())
    lst2=list(set(word))
    hand={}
    for i in h:
        for j in word:
            if i==j:
                h[i]=h[i]-word.count(i)
                if h[i]>0:
                    hand[i]=h[i]
                    
            elif i!=j:
                lst3=lst1-lst2
                for d in lst3:
                    k[d]=h[d]

    hand.update(k)         
    return hand
       

    # pass  # TO DO... Remove this line when you implement this function

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    
    word = word.lower()
    l=[]
    lw=[]
    h=hand.copy()
    if '*' not in word:
        if word in word_list :
            for i in word:
                lw.append(i)
                if i in list(hand.keys()):
                    if word.count(i)<=hand[i]:
                        l.append(i)
            if set(lw)==set(l):
                return True
            else:
                return False
        elif word not in word_list:
            return False
    for i in VOWELS:
        h[i] = h.get(i, 0) + 1
        if is_valid_word(word.replace('*', i), h, word_list)==True  :
            return True
    return False
    
    
    # pass  # TO DO... Remove this line when you implement this function

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    count_el=0
    for i in hand:
        count_el+=int(hand.get(i,0))
    return count_el


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    ok=False
    score=0
    while not ok:
        if calculate_handlen(hand) != 0:
            print('-------------------------------------')
            print('Current Hand: ', display_hand( hand ) )
            word = str(input('Enter word, or “!!” to indicate that you are finished: '))
                         
            if word=='!!' :
                ok=True
            else:
                if is_valid_word(word, hand, word_list)==True :
                    score+=get_word_score(word,calculate_handlen(hand))
                    print(f"{word} earned {get_word_score(word,calculate_handlen(hand))} points. Total: {score} points")   
                else:
                    print('This is not a valid word. Please choose another word.')
                hand=update_hand(hand, word)
        else:
            print(f"Ran out of letters. Total score: {score} points")
            ok=True
    print(f"Total score for this hand: {score}")
    print('-------------------------------------')
    return score
 
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is two exclamation points:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    h=hand.copy()
    n=hand[letter]
    h.pop(letter,n)
    l=list(VOWELS+CONSONANTS)
    for i in hand.keys():
        if i!='*':
            l.remove(i)
    le=''.join(l)
    x = random.choice(le)
    h[x] = n
    return h

       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    total_score=0
    x='number'
    ll='letter'
    ok=False
    def check(x):
        x1=input(f'Enter total {x} of hands: ')
        try :
            x1=int(x1)
            if x1>0:
                return x1
            else:
                print(f'Error. {x} > 0.')
                return check(x)
        except:
            print('Error.')
            return check(x)
    def check2(x):
        x1=str(input(f"{x} Enter yes or no - "))
        try :
            x1=x1.lower()
            if x1=='yes'or x1=='no':
                return x1
            else:
                print('Invalid response. You need to answer again')
                return check2(x)
        except:
            print('Invalid response. You need to answer again')
            return check2(x)
    def check3(x):
                x1=str(input('Which letter would you like to replace: ' ))
                if x1 in hand.keys():
                    if x1!='*':
                        return x1
                    else:
                        print('Error. You can not choose * ')
                        return check3(x)
                else:
                    print('Error')
                    return check3(x)
    while not ok:
        print('-------------------------------------')
        number=check(x)
        hand= deal_hand(number)             
        print('Current Hand: ', display_hand( hand ) )
        print('-------------------------------------')
        c='Would you like to substitute a letter?'
        withs=check2(c)
        a='Would you like to replay the hand? '
        if withs =='no':
            total_score+=play_hand(hand, word_list)
            again=check2(a)
            if again=='yes':
                ok=False
            else:
                ok=True
        else:
            letter=check3(ll)
            hand=substitute_hand(hand, letter)
            total_score+=play_hand(hand, word_list)
            again=check2(a)
            if again=='yes':
                ok=False
            else:
                ok=True
    print(f'Total score over all hands: {total_score}')
           

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
