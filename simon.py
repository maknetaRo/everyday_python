from random import choice

print("Let's play Simon says. Repeat after me (rewrite or hit enter).")

while True:
    lost_games = 0
    one = ['turn around',
           'clap your hands',
           'stamp your feet',
           'jump',
           'run',
           'sit down',
           'close your eyes',
           'touch your nose',
           'stand up',
           'say: Hello!']
    computer_choice = ["simon_says", "no"]
    game = 0
    while lost_games < 3:
        computer = choice(computer_choice)
        if computer == "simon_says":
            computers_turn = choice(one)
            prompt = f"Simon says: {computers_turn}"
            print(prompt)
            player = input(">>>")
            if player == computers_turn:
                print("Well done")
            else:
                print("You should have repeated my words")
                lost_games +=1
        else:
            computers_turn = choice(one)
            prompt = f"{computers_turn}"
            print(prompt)

            player = input(">>>")
            if player == prompt:
                print("You shouldn't have repeated anything.")
                lost_games += 1

            else:
                print("Well done!")
        game += 1
        print(f"You've made {lost_games} mistake(s).")
    once_again = input("Do you want to play again? y/n ")
    if once_again == 'y':
        computer = choice(computer_choice)
    else:
        print("Thank you. Goodbye!")
        break
