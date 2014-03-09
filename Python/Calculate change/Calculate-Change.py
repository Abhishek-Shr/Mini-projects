# FUNCTIONS
def calculate_dollars(money):
    DOLLAR_BILLS = [100, 50, 20, 10, 5, 2, 1]
    output_dictionary = {}

    for dollar in DOLLAR_BILLS:
        dollars_needed = money // dollar
        output_dictionary[dollar] = dollars_needed
        money -= dollar * dollars_needed

    return output_dictionary


def calculate_coins(money, dollars):
    money_in_coins = round(abs(money - dollars) * 100, 2)
    COINS = [50, 25, 10, 5, 2, 1]
    output_dictionary = {}

    for coin in COINS:
        coins_needed = money_in_coins // coin
        if coins_needed >= 1:
            output_dictionary[coin] = coins_needed
            money_in_coins -= coin * coins_needed

    return output_dictionary


def print_dictionary(money, string):
    for key in money.items():
        if key[1] != 0:
            print("%.1s x %s %s" % (key[1], key[0], string))


# main
def main():
    cash_given = float(input("Enter the cash you have given (Ex: 1.54): "))
    item_price = float(input("Enter the item price (Ex: 1.23): "))

    change = cash_given - item_price
    if change < 0:
        exit("Item price exceeds cash given!")

    dollars = int(change)
    coins = calculate_coins(change, dollars)
    dollars = calculate_dollars(dollars)

    print("---Return---")
    print("-Dollars:")
    print_dictionary(dollars, "dollars")
    print("-Coins:")
    print_dictionary(coins, "cents")


# PROGRAM RUN
if __name__ == "__main__":
    main()
