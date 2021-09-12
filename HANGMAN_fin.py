from random import randint
from animal_list import guess_list

#Alright, here's the material we need to play the game:

#"Guess_list" variable is in its own module, as seen in imports above^.\
# There's 94 animals on there; I figured I'd separate them for neatness.

blanks = []         #This will hold our "_" letters to guess
previous_words = [] #Words you've already guessed will be put here.
previous_guesses = []
word_index = 0
random_choice = ""
guess = ""
correct = False
ttl = 7  #heh
answer = ""
new_word = False

def exit():
    if guess == "quit":
        print("Ok, thanks for playing!")
        return True


#OKAY. Let's get going!

#Choosing a word to guess from the list.....
word_index = randint(0, (len(guess_list)-1))    #Having a random index separate allows me to pop easier, vs random.choice
random_choice = guess_list[word_index]

#Generating our blank letter spaces:
for letter in random_choice:
    blanks.append("_")

#print(f"Psst, the animal is: {random_choice}")    #<-This was to assist debugs :)

print("Welcome to hangman! Guess the word one letter at a time, and quit at any point by typing 'quit'. \nHere's your word to guess:")
print(blanks)

while guess != "quit":
    guess = input("\nYour guess: ").lower().strip()
    if exit():
        break
    correct = False #Gotta reset result of your last answer
    answer = "" #Also resetting 'answer' in case this isn't your first loop
    previous_guesses.append(guess)

#Time to check out your guess
    for index, letter in enumerate(random_choice):
        if guess == letter:
            blanks[index] = guess
            correct = True
        else:
            if correct == True:   #passing allows multiple iterations of same letter to be found at once.
                pass
            else:
                correct = False

    if correct:
        print("\nCorrect!\n")
    else:
        ttl = ttl -1
        if ttl != 0:
            print(f"\nNope! \n{ttl} guesses left\n")    
        else:
            print(f"Sorry, you're out of guesses! The word was {random_choice}. \nBetter luck next time!")
            answer = input("Would you like to try again? y/n: ").lower().strip()

    #Have you won? 
    if "_" not in blanks:
        print(f"Congratulations, you got it! :D The answer was indeed {random_choice}")
        #The word has been guessed successfully, let's take it off the list \
        #In case you want to play another round.
        last_word = guess_list.pop(word_index)
        previous_words.append(last_word)

        #Ok, we're prepped. Let's ask:
        answer = input("Would you like to try again? y/n: ").lower().strip()
    else:
        pass


    #Are we playing again?
    if answer == "y" and len(guess_list) == 0:
        print("You've exhausted our word list! You're the animal champion! \nThanks for playing :)")
        break

    elif answer == "y" or answer == "yes":
        #Time to reset some elements, then:
        blanks = []
        previous_guesses = []
        answer = ""
        ttl = 7

        #Brand new animal let's go:
        word_index = randint(0, (len(guess_list)-1))
        random_choice = guess_list[word_index]

        #Generate blank letterspaces:
        for letter in random_choice:
            blanks.append("_")
        print("Here's your new word:")

    elif answer == "n" or answer == "no" or answer == "q" or answer == "quit":
        print("Thanks for playing!")
        break
    else:
        pass

    print(blanks) #Blanks to be printed each loop so we see where we're at :)
    print(f"\nPrevious guesses: \n{previous_guesses}")