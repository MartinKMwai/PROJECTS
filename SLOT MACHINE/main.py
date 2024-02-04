#we are going to creste a slot machine game, minus the interface, of course


MAX_LINES = 3



def deposit():
    while True:
        amount = input ("How much money fo you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please input an amount greater than 0. ")
        
        else:
            print("Please input amount in number format. ")

    return amount


def get_number_of_betting_lines(amount):
    while True:
        lines = input ("How many lines do you want to bet on? ")
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <= MAX_LINES:
                break
            else:
                print ("Please input lines between one and " + str(MAX_LINES) + " inclusive. ")
        else:
            print ("Please input your number of lines in number format. ")

    return lines



   
def main():
    balance = deposit()




main()

