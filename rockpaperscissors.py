import random

def get_computer():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user = input("\nChoose rock, paper, or scissors: ").lower()
        if user not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer = get_computer()
        winner = determine_winner(user, computer)
        display_result(user, computer, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScores: You {user_score} - Computer {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("\nThank you for playing!")

play_game()
