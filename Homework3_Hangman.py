import random
import string

name = input("Please enter your name:")
print("Welcome",name,".Time to play hangman!")

words = ["banana","apple","cherry","watermelon","peach","pear","pineapple","lemon","melon","strawberry"]


def get_word(words):

    word = random.choice(words)
    while '-' in word:
        word = random.choice(words)

    return word.upper()

def hangman():

    word = get_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    trys = 7

    while len(word_letters) > 0 and trys > 0 :

        print('You have',trys,'trys left and you used these letters: ',' '.join(used_letters))

        word_list = [ letter if letter in used_letters else '-' for letter in word]

        print('Chosen word: ',' '.join(word_list))


        entered_letter = input('Enter a letter: ').upper()

        if entered_letter in alphabet - used_letters:
            used_letters.add(entered_letter)

            if entered_letter in word_letters:
                word_letters.remove(entered_letter)
                print('')

            else:
                trys = trys -1
                print(entered_letter,'is not in this word.')

        elif entered_letter in used_letters:
            print("\nYou tryed that letter before. Try another one.")

        else:
            print("That is not a letter.")


    if trys == 0 :
        print("GAME OVER!!!")

    else:
        print("CONGRATULATIONS!!! You won :)")

if __name__ == '__main__':
    hangman()
                  

            



