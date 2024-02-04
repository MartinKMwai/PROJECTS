#we are going to creste a slot machine game, minus the interface, of course

def deposit():
    while True:
        amount = input ("How much money fo you want to deposit? $  ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please input an amount greater than 0. ")
        
        else:
            print("Please input amount in number format. ")

    return amount

