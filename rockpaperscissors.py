import random
import tkinter as tk

#NOTE: A function that determines whether the user wins or not
#      Passes the user's choice (based on what button they click)to the parameter
def get_winner(user):

    # Access variables declared after the function so that the variables can be changed inside of the function
    global wins, win, output

    # 1. Create random integer 1-3 to use as computer's play
    randInt = random.randint(1, 3)
    # 2. Using if-statements, assign the computer to a choice (rock, paper, scissors) using the random integer generated
    choice = ""
    if randInt == 1:
        choice = "rock"
        print(1)
    elif randInt == 2:
        choice == "paper"
        print(2)
    elif randInt == 3:
        choice == "scissors"
        print(3)

    # 3. Determine the winner based on what the user chose and what the computer chose
    if (user == "rock" and choice == "scissors") or (user == "scissors" and choice == "paper") or (user == "paper" and choice == "rock"):
        win += 1
        winsLabel["text"] = "Number of Wins: " + str(win)
        resultLabel["text"] = "Result: win"
        resultLabel["bg"] = "#329F5B"
    elif choice == user:
        resultLabel["text"] = "Result: tie"
        resultLabel["bg"] = "#329F5B"
    else:
        resultLabel["text"] = "Result: loss"
        resultLabel["bg"] = "#DB7F8E"
    #   Rock beats Scissors, Paper beats Rock, Scissors beats Paper
    #   It's a tie if the computer and user chose the same object
    #   If the user wins, increase win by 1
    #   Use the output label to write what the computer did and what the result was (win, loss, tie)

# Use these functions as "command" for each button
def pass_s():
    get_winner("scissors")
def pass_r():
    get_winner("rock")
def pass_p():
    get_winner("paper")

window = tk.Tk()
window.configure(bg="#FEFAE0")
#Variable to count the number of wins the user gets
win = 0
output = ""
#START CODING HERE
# 1. Create 3 buttons for each option (rock, paper, scissors)
rockButton = tk.Button(text="Rock", padx=10, pady=10, command=pass_r, bg="#A8D6F0")
paperButton = tk.Button(text="Paper", padx=10, pady=10, command=pass_p, bg="#5FBFF9")
scissorsButton = tk.Button(text="Scissors", padx=10, pady=10, command=pass_s, bg="#254E70")
buttons = [rockButton, paperButton, scissorsButton]
# 2. Create 2 labels for the result and the number of wins
resultLabel = tk.Label(text= "Result: ", bg="#FEFAE0")
winsLabel = tk.Label(text= "Number of Wins: "+ str(win), bg="#FEFAE0")

# 3. Arrange the buttons and labels using grid
window.rowconfigure(0, minsize=50, weight=1)
for i in range(3):
    window.columnconfigure(i, minsize=100, weight=1)
    frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
    frame.grid(row=0, column=i, padx=5, pady=5)
    button = buttons[i]
    button.grid(row=0, column=i)

window.rowconfigure(1, minsize=50, weight=1)
frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame.grid(row=1, column=0)
resultLabel.grid(row=1, column=0)

window.rowconfigure(2, minsize=50, weight=1)
frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame.grid(row=2, column=0)
winsLabel.grid(row=2, column=0)

window.mainloop()
