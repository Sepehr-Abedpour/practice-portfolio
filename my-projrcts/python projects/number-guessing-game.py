import random

def play_game():

    name = input('hello , whats your name ?')
    print (f"hi {name}, let's play a game.")
    print (" i'll pick a number between 1 and 50, and you have to guess it.")

    secret_number = random.randint(1,50)
    attempts = 0

    while True:
        guess = int(input("enter your guess(or 0 to quit):"))
        attempts += 1
        
        

        if guess == 0 :
            print(f" thanks for playing,{name}! the number was {secret_number}.")
            break
        
        if guess ==  secret_number : 
            print(f" congrats {name}! you guessed it in {attempts} attempts! ")
            break
        elif guess < secret_number :
            print(" too low! try a higher number.")
        else :
            print (" too high! try a lower number.")
            
if __name__ == "__main__":
    play_game()

