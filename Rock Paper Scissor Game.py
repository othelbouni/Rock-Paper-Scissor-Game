import random
u = 0
c = 0
print("Let's play Rock, Paper, scissors !")
while True:
    while True:
        answer = input("Play or Exit ? ")
        try:
            if answer.lower() not in ["play", "exit"]:
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid choice. Please try again.")
    if answer.lower() == "play":
        while True:
            # r > s, p > r, s > p
            try:
                user = input("Enter 'r' for Rock, 'p' for Paper, 's' for scissor: \n".lower())
                if user not in ['r', 'p', 's']:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Invalid choice. Please try again.")
                continue
        computer = random.choice(['r', 'p', 's'])
        if computer == user:
            print("It's a tie! haha!")
            continue
        if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
            print(f"User chose: {user}")
            print(f"Computer chose: {computer}")
            print("user win !")
            u += 1
        else:
            print(f"You chose: {user}")
            print(f"Computer chose: {computer}")
            print("Computer win !")
            c += 1
    else:
        break
print("You win {} times".format(u))
print("The computer win {} times".format(c))



