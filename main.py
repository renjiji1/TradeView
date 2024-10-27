from TradeView import WatchPrice, AtLow, AtHigh, IntervalIncrease, IntervalDecrease

def main():
    menu()

watch_stocks = []
low_stocks = []
high_stocks = []
increase_stocks = []

def menu():
    print()
    print("TradeView:")
    print("---------------------")
    print("1. Watch Stock")
    print("2. Stock Interval Increase")
    print("3. Stock Interval Decrease")
    print("4. Exit")
    print()

    while True:
        option = input("Select a Number: ")
        try:
            option = int(option)
            if option >= 1 and option <= 4:
                break
        except:
            print("Invalid Input: please input one of the numbers from the menu")

    if option == 1:
        watch()
    elif option == 2:
        low_interval()
    elif option == 3:
        high_interval()
    else:
        return 1

def watch():
    if len(watch_stocks) != 0:
        print("")
        print("Watch-List:")
        i = 1
        for stock in watch_stocks:
            print(str(i) + " - " + stock["ticker"] + ", Current Price: $" + str(stock["curPrice"]) + ", " + stock["watch"])
            i += 1
    print("")
    print("1. Delete Stock")
    print("2. Add Stock")
    print("3. Menu")
    print("")

    while True:
        option = input("Select a Number: ")
        try:
            option = int(option)
            if option >= 1 and option <= 3:
                break
        except:
            print("Invalid Input: please input one of the numbers from the menu")

    if option == 1:
        option = input("Select the Index of Stock to Delete: ")
        try:
            option = int(option)
            if option <= len(watch_stocks):
                watch_stocks.pop(option - 1)
            else:
                print("Invalid Input: index out of range")
        except:
            print("Invalid Input: non-number was enter, please enter a number")
        watch()
    elif option == 2:
        ticker = input("Enter the Desired Stock's Ticker Symbol: ")
        low = round(float(input("Enter the Lower Limit of the Stock Price: ")), 2)
        high = round(float(input("Enter the Higher Limit of the Stock Price: ")), 2)
        #WatchPrice returns a dictionary of {"ticker", "output", "curPrice"}
        watch_info = WatchPrice(ticker, low, high)
        stock = {"ticker" : ticker, "watch" : watch_info["output"], "curPrice" : watch_info["curPrice"]}
        watch_stocks.append(stock)
        watch()
    else:
        menu()


def low_interval():
    ticker = input("Enter the Desired Stock's Ticker Symbol: ")
    days = input("Enter the Number of Days in this Interval: ")
    threshold = input("Enter the Threshold: ")
    output = IntervalIncrease(ticker, days, threshold)
    print(output)

def high_interval():
    ticker = input("Enter the Desired Stock's Ticker Symbol: ")
    days = input("Enter the Number of Days in this Interval: ")
    threshold = input("Enter the Threshold: ")
    output = IntervalDecrease(ticker, days, threshold)

def increase():
    pass

if __name__ == "__main__":
    main()