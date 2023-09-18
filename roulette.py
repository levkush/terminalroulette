# Define lists for different categories of roulette numbers

import os
import random
import time

import colorama
from colorama import Back

types = {
    "red": {
        "payout": 2,
        "numbers": [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    },
    "black": {
        "payout": 2,
        "numbers": [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    },
    "odd": {
        "payout": 2,
        "numbers": [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    },
    "even": {
        "payout": 2,
        "numbers": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    },
    "single": {
        "payout": 35,
        "numbers": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    }
}

blacks = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
zero = [0]

roulette_wheel = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]

money = 1000

bets = []

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def print_numbers():
    top_column = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
                                         
    print("┌───────────────────────────  Terminal Roulette v1.0  ───────────────────────────┐")
    print("│ ", end="")

    print(Back.GREEN + "      ", end="")

    for number in top_column:
        number_formatted = f'  {number}  '
        if number < 10:
            number_formatted = f'  0{number}  '

        if number in reds:
            print(Back.RED + number_formatted, end="")
        elif number in blacks:
            print(Back.BLACK + number_formatted, end="")
        elif number in zero:
            print(Back.GREEN + number_formatted, end="")

    print(colorama.Back.RESET + " │")

    middle_column = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    print("│ ", end="")
    print(Back.GREEN + "  00  ", end="")

    for number in middle_column:
        number_formatted = f'  {number}  '
        if number < 10:
            number_formatted = f'  0{number}  '

        if number in reds:
            print(Back.RED + number_formatted, end="")
        elif number in blacks:
            print(Back.BLACK + number_formatted, end="")
        elif number in zero:
            print(Back.GREEN + number_formatted, end="")

    print(colorama.Back.RESET + " │")

    bottom_column = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]

    print("│ ", end="")

    print(Back.GREEN + "      ", end="")

    for number in bottom_column:
        number_formatted = f'  {number}  '
        if number < 10:
            number_formatted = f'  0{number}  '

        if number in reds:
            print(Back.RED + number_formatted, end="")
        elif number in blacks:
            print(Back.BLACK + number_formatted, end="")
        elif number in zero:
            print(Back.GREEN + number_formatted, end="")

    print(colorama.Back.RESET + " │")
    print("└────────────────────────────────────────────────────────────────────────────────┘")

def print_wheel(amount, margin_left = 3):
    print("    " * margin_left, "┌────────────────────────────────────────────┐")
    print("    " * margin_left, "│ ", end="")
    current_numbers = []
    #print("│", end="")
    for number in range(0, amount):
        roulette_number = roulette_wheel[number - 3]
        number_formatted = f'  {roulette_number}  '
        if roulette_number < 10:
            number_formatted = f'  0{roulette_number}  '

        if roulette_number in reds:
            print(Back.RED + number_formatted, end="")
        elif roulette_number in blacks:
            print(Back.BLACK + number_formatted, end="")
        elif roulette_number in zero:
            print(Back.GREEN + number_formatted, end="")
        current_numbers.append(roulette_number)

    print(colorama.Back.RESET, "│")
    print("    " * margin_left, "└────────────────────────────────────────────┘")
    global roulette_item
    roulette_item = current_numbers[4]

def roll():
    global money
    global status
    global bets

    roll = 0
    amount_of_rolls = random.randint(11, 36)

    while roll < amount_of_rolls:
        roll += 1

        clear()
        print_numbers()
        print_wheel(7)
        print("                                    ▲")
        print(f'\nMONEY: {money}$')
        time.sleep(0.2)
        first_number = roulette_wheel.pop(0)
        roulette_wheel.append(first_number)

    total_win = 0
    total_loss = 0

    for bet in bets:
        bet_type = bet.get("type")
        type_numbers = types[bet_type]["numbers"]
        amount = bet.get("amount")

        if bet_type == "single":
            if roulette_item == bet.get("number"):
                money += amount * types[bet_type]["payout"]
                total_win += amount * types[bet_type]["payout"]
            else:
                total_loss += amount
                
        elif roulette_item in type_numbers:
            money += amount * types[bet_type]["payout"]
            total_win += amount * types[bet_type]["payout"]

        else:
            total_loss += amount
    bets = []

    total = total_win - total_loss

    if total > 0:
        status = f'YOU WON {total}$\n'

    elif total < 0:
        status = f'YOU LOST {-total}$\n'

status = f'MONEY: {money}$\n'

while True:
    clear()
    print_numbers()
    print_wheel(7)
    print("                                    ▲")
    print(status)
    #time.sleep(0.3)
    command = input("TerminalRoulette > ")

    args = command.split(' ')
    action = args.pop(0)
    args_amount = len(args)

    if action == "start" or action == "roll":
        if bets == []:
            status = "You have to place at least one bet!\n"
            continue
        roll()

    elif action == "bet":
        try:
            int(args[0])
        except:
            status = "Usage is bet [amount] [type]. \nTypes: red, black, odd, even or number less than 36, like 12."
            continue

        if money < int(args[0]):
            status = "You don't have enough money for this bet!\n"
            continue

        if int(args[0]) < 0:
            status = "Usage is bet [amount] [type]. \nTypes: red, black, odd, even or number less than 36, like 12."
            continue

        if args_amount < 2 or args_amount > 3:
            status = "Usage is bet [amount] [type]. \nTypes: red, black, odd, even or number less than 36, like 12."
            continue

        if args[1] not in ['red', 'black', 'odd', 'even']:
            if args[1].isdigit():
                if int(args[1]) > 36:
                    status = "Usage is bet [amount] [type]. \nTypes: red, black, odd, even or number less than 36, like 12."
                    continue
                try:
                    args[2] = args[1]
                except Exception:
                    args.append(args[1])
                    
                args[1] = "single"
                pass
            else:
                status = "Usage is bet [amount] [type]. \nTypes: red, black, odd, even or number less than 36, like 12."
                continue

        if args_amount >= 3 and args[1] == "single":
            bets.append({
                'type': 'single',
                'amount': int(args[0]),
                'number': int(args[2])
            })

        else:
            bets.append({
                'type': args[1],
                'amount': int(args[0])
            })

        amount = int(args[0])
        money -= int(args[0])

        type = args[1]

        if args[1] == "single":
            number = int(args[2])

            status = f'Successfully bet {amount}$ on {number}!\n'
        else:
            status = f'Successfully bet {amount}$ on {type}!\n'

    elif action == "help":
        if args_amount < 1:    
            status = "Type help [command] to see help. \nCommands: bet, start, clearbets, money, exit"
        else:
            if args[0] == "bet":
                status = "Add a new bet. Usage is bet [amount] [type]. \nTypes: red, black, odd, even or number less than 36, like 12."
            elif args[0] == "start":
                status = "Starts the game. Usage is: start."
            elif args[0] == "clearbets":
                status = "Clear all bets. Usage is: clearbets."
            elif args[0] == "money":
                status = "Prints your balance. Usage is: money."

    elif action == "money":
        status = f'MONEY: {money}$\n'
        continue

    elif action == "clearbets":
        for bet in bets:
            money += bet.get("amount")

        bets = []
        
        status = "Cleared all bets.\n"

    elif action == "exit":
        clear()
        print("Exiting...")
        break
    else:
        status = "Unknown command. Type help for help.\n"