def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("-------------------------------------------------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

def display_score(correct_guesses, guesses):
    print("--------------------------------------")
    print("RESULTS")
    print("--------------------------------------")
    
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False

questions = {
    "What is the name of the final course of all Mario Kart video games?: ": "B",
    "Who owns PlayStation?: ": "D",
    "Solid Snake is the hero of the famous video game franchise?: ": "A",
    "In the Pac-Man video game, what is the name of the orange ghost?: ": "B"
}

options = [["A. Koopa Troopa Beach", "B. Rainbow Road", "C. Electrodome", "D. Coconut Mall"],
["A. Micrsoft", "B. Atari", "C. Nintendo", "D. Sony"],
["A. Metal Gear Solid", "B. Dungeons and Dragons", "C. Spyro", "D. Mario Kart"],
["A. Joe", "B. Clyde", "C. Orange", "D. Blinky"]]

new_game()

while play_again():
    new_game()

print("Bye")
