# --------------- START ---------------

"""Quiz Game"""

# def run_quiz():

#     """this is quiz game"""

#     questions = (
#         "Which is the largest planet in our solar system?",
#         "Who is known as the “Father of the Computer”?",
#         "Which country has the highest population in the world (as of recent data)?",
#         "What is the chemical symbol for Gold?",
#         "Which continent is the Sahara Desert located in?"
#         )
#     options = (
#         ("A) Earth", "B) Saturn", "C) Jupiter", "D) Mars"),
#         ("A) Alan Turing", "B) Charles Babbage", "C) Bill Gates", "D) Steve Jobs"),
#         ("A) USA", "B) China", "C) India", "D) Russia"),
#         ("A) Go", "B) Gd", "C) Au", "D) Ag"),
#         ("A) Asia", "B) Australia", "C) Africa", "D) South America")
#         )

#     answers = ("C", "B", "C", "C", "C")
#     guesses = []
#     question_num = 0
#     total_score = 0

#     for question in questions:
#         print("----------------------------------------")
#         print(question)
#         for option in options[question_num]:
#             print(option)

#         guess = input("Enter the correct option: ").upper()

#         if guess == answers[question_num]:
#             print("Your answer is CORRECT!")
#             guesses.append(guess)
#             total_score += 1
#         else:
#             print("Your answer is INCORRECT!")
#             print(f"{answers[question_num]} is the correct answer")

#         question_num += 1

#     result = int((total_score / len(questions)) * 100)

#     print("------------------------------")
#     print("            RESULT            ")
#     print("------------------------------")

#     print("answers: ", end=" ")
#     for answer in answers:
#         print(answer, end=",")
#     print()

#     print("guesses: ", end=" ")
#     for guess in guesses:
#         print(guess, end=",")
#     print()

#     print(f"Your Result is: {result}%")

# if __name__ == "__main__":
#     run_quiz()

# --------------- END -----------------


# --------------- START ---------------

# def run_concession_stand_program():

#     """ This is Concession Stand Program """

#     menu = {
#         "Popcorn": 3.00,
#         "Pizza": 5.99,
#         "Pretzel": 2.75,
#         "Chips": 1.25,
#         "Soda": 2.99,
#         "Lemonade": 1.75
#     }

#     cart = []
#     total_price = 0

#     print("--------------- MENU ---------------")
#     for key, value in menu.items():
#         print(f"{key:10}: ${value:.2f}")
#     print("------------------------------------")

#     while True:
#         food = input("Select an Item (q to quit): ").capitalize()
#         if menu.get(food) is not None:
#             print(f"{food} is added in the cart")
#             cart.append(food)
#         elif food.upper() == "Q":
#             break
#         elif menu.get(food) is None:
#             print(f"{food} is not in the menu")

#     print()

#     print("------------------------------------")
#     print("Your order is: ", end=" ")
#     for food in cart:
#         print(f"{food}", end=" ")

#     print()

#     print("------------------------------------")
#     for food in cart:
#         total_price += menu[food]

#     print(f"Your total price is: ${total_price:.2f}")
#     print("------------------------------------")

# if __name__ == "__main__":
#     run_concession_stand_program()

# --------------- END -----------------


# --------------- START ---------------

# import random

# def run_dice_program():

#     """ This is Dice Program """

#     def greetings():
#         message = "Welcome"
#         border = "*" * 10
#         print(border)
#         print(message.center(30))
#         print(border)

#     def dice_art(num):
#         if num == 1:
#             print("┌─────────┐")
#             print("│         │")
#             print("│    ●    │")
#             print("│         │")
#             print("└─────────┘")
#         elif num == 2:
#             print("┌─────────┐")
#             print("│  ●      │")
#             print("│         │")
#             print("│      ●  │")
#             print("└─────────┘")
#         elif num == 3:
#             print("┌─────────┐")
#             print("│  ●      │")
#             print("│    ●    │")
#             print("│      ●  │")
#             print("└─────────┘")
#         elif num == 4:
#             print("┌─────────┐")
#             print("│  ●   ●  │")
#             print("│         │")
#             print("│  ●   ●  │")
#             print("└─────────┘")
#         elif num == 5:
#             print("┌─────────┐")
#             print("│  ●   ●  │")
#             print("│    ●    │")
#             print("│  ●   ●  │")
#             print("└─────────┘")
#         elif num == 6:
#             print("┌─────────┐")
#             print("│  ●   ●  │")
#             print("│  ●   ●  │")
#             print("│  ●   ●  │")
#             print("└─────────┘")

#     count = 0

#     while True:
#         players = ["Fawad", "Ubaid", "Mamoon", "Furqan"]

#         for index in range(4):
#             number = random.randint(1, 6)
#             input(f"{players[index]}'s turn (Press Enter): ")
#             dice_art(number)
#             while number == 6:
#                 count += 1
#                 if count == 3:
#                     print("--------------------------------------------------")
#                     print("Oops! Three consecutive 6s rolled. Turn forfeited!")
#                     print("--------------------------------------------------")
#                     count = 0
#                     break
#                 number = random.randint(1, 6)
#                 input(f"{players[index]}'s turn (Press Enter): ")
#                 dice_art(number)
#             index += 1

# if __name__ == "__main__":
#     run_dice_program()

# --------------- END -----------------


# --------------- START ---------------

# import random

# def run_rock_paper_scissors_program():

#     """ This is rock paper scissors game """

#     options = ("rock", "paper", "scissors")

#     while True:
#         player = None
#         computer = random.choice(options)
#         player = input("Enter option (rock, paper, scissors) (q to quit): ")

#         if player.upper() == "Q":
#             break

#         while player not in options:
#             player = input("Invalid Option! Choose (rock, paper, scissors) (q to quit): ")

#         print(f"Player: {player}    Computer: {computer}")

#         if player == "rock" and computer == 'scissors':
#             print("You Win!")
#         elif player == "paper" and computer == 'rock':
#             print("You Win!")
#         elif player == "scissors" and computer == 'paper':
#             print("You Win!")
#         elif player == computer:
#             print("It's a Tie!")
#         else:
#             print("You Lose!")

# if __name__ == "__main__":
#     run_rock_paper_scissors_program()

# --------------- END -----------------


# --------------- START ---------------
