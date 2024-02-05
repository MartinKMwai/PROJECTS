#we are going to creste a slot machine game, minus the interface, of course


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1



def deposit():
    while True:
        amount = input ("How much money do you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please input an amount greater than 0. ")
        
        else:
            print("Please input amount in number format. ")

    return amount


def get_number_of_betting_lines():
    while True:
        lines = input ("How many lines do you want to bet on? ")
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <= MAX_LINES:
                break
            else:
                print ("Please input lines between 1 and " + str(MAX_LINES) + " inclusive. ")
        else:
            print ("Please input your number of lines in number format. ")

    return lines

def amount_per_line(lines, amount):
    while True:
        bet_per_line = input ("How much would you like to bet per line? $")
        if bet_per_line.isdigit():
            bet_per_line  = int(bet_per_line )
            if bet_per_line  >= MIN_BET and bet_per_line  <= MAX_BET:
                betting_amount = bet_per_line  *lines
                if betting_amount <= amount:
                    print ("Your total betting amount is $" + str(betting_amount))
                    break
                else:
                    print ("Your betting balance is " + str(amount) + " and you want to bet $" + str(betting_amount))
                    print ("You do not have money for that bet, bet lesser money per line")
            else:
                print ("Please input a betting amount between $" + str(MIN_BET) + " and $" + str(MAX_BET) + "." ) 
        else:
            print ("Please input the bet that you want to mske in number format.")
    return bet_per_line, betting_amount

   
def main():
    amount = deposit()
    lines = get_number_of_betting_lines()
    bet_per_line, betting_amount = amount_per_line(lines, amount)
    print (amount, lines)
    print (f"Your balance is {amount}")
    print (f"Number of lines : {lines}")
    print (f"Your bet per line: ${bet_per_line}")
    print (f"Your total betting amount is ${betting_amount} ")




main()

