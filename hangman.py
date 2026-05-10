import random 

#step-1:List of words
words =["apple","tiger","house","robot","green"]

#step-2: Choose random words
word = random.choice(words)

#step-3: Variables
guesses_letters = []
wrong_gusses = 0
max_wrong_gusses = 6

print("Welcome to HANGMAN!")

#step-4: Game Loop
while wrong_gusses < max_wrong_gusses:

    #display the words with blanks
    display_word = " "
    for letter in word:
        if letter in guesses_letters:
            display_word += letter +" "
        else: 
            display_word += "__"
    print("\n Word:" , display_word)
    print("Wrong guesses left:",max_wrong_gusses - wrong_gusses)
    print("Guessed letter:"," ".join(guesses_letters))
    # Check if players has guesses the whole word
    if all(letter in guesses_letters for letter in word):
        print("Congratulation!! You guessed the word:",word)
        break
    
    #Show remaining guesses
    print("Incorrect gusses left:", max_wrong_gusses - wrong_gusses)


    # Get player input
    guess = input("enter a letter:").lower()
    
    #Validate input
    if len(guess) != 1:
        print("please enter only one letter.")
    elif guess in guesses_letters:
        print("You already guessed that letter.")
    else:
        guesses_letters.append(guess)

        #Check if guess is correct
        if guess in word:
            print("Correct guess!!")
        else:
            print("Wrong guess!!")
            wrong_gusses += 1
    if wrong_gusses == max_wrong_gusses:
       print("\n GAME OVER!!")
       print("The world was:",word)
