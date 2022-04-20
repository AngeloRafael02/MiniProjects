import random as rng
def game():
    while True:
        print("Game until you Win!\n")
        userChoice = str(input("Rock, Paper, Scissors - Shoot!: "))
        list1 = ["rock","paper","scissors"]
        AIChoice = str(rng.choice(list1))
        try:
            if userChoice.lower() == "scissors" and AIChoice.lower() == "rock"\
                or userChoice.lower() == "paper" and AIChoice.lower() == "scissors"\
                or userChoice.lower() == "rock" and AIChoice.lower() == "paper" :
                print("\tRNG picks " + AIChoice + ", You Lose!")
                continue
            elif userChoice.lower() == AIChoice.lower():
                print("\tRNG picks " + AIChoice + ", Tie!")
            elif userChoice.lower() == "rock" and AIChoice.lower() == "scissors"\
                or userChoice.lower() == "scissors" and AIChoice.lower() == "paper"\
                or userChoice.lower() == "paper" and AIChoice.lower() == "rock" :
                print("\tRNG picks " + AIChoice + ", You Win!")
                break
        except Exception as error: 
            print(error)
def main():
    print("How many rounds until you win?")
    game()
main()