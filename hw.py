import cbpro
import datetime
import time

client = cbpro.PublicClient()

# loading dots
def loading():
    for c in range(3):
        print(".", end="")
        time.sleep(.5)

# gets ethereum price
def get_price_eth():
    prods = client.get_product_ticker(product_id='ETH-GBP')
    price = prods["price"]
    return price

# gets Bitcoin price
def get_price():
    prods = client.get_product_ticker(product_id='BTC-GBP')
    price = prods["price"]
    return price

# gets the time stamp
def get_timestamp():
    timestamp = datetime.datetime.now()
    timestamp = timestamp.strftime("%d-%m-%y %H:%M:%S")  # puts it into format so not too many nums
    return timestamp

# writes into external file - Bitcoin
def write_line(output):
    fh = open("bitcoin-price.txt", "a")
    fh.write(f"{output} \n")  # or '\r'
    fh.close()

# writes into external file - Ethereum
def write_line_eth(output):
    fh = open("Ethereum-price.txt", "a")
    fh.write(f"{output} \n")  # or '\r'
    fh.close()

# bitcoin method
def bitcoin():
    count = 1
    # main program
    print("---Bitcoin to GBP---")
    while True:
        frequency = int(input("how often do you want to detect price change? (seconds) ")) # asks user for how often they want to detect
        if frequency < 1:
            print("sorry you please enter an integer more than 1") # only excepts values greater than one
        else:
            break
    times = int(input("how many times you you want to detect the price? ")) # asks how many times

    print()
    print("     Date      Time     GBP(£)") # creates headings
    for x in range(times):                  # depending on 'times' repeats gathering of price & time stamp
        price = get_price()
        timestamp = get_timestamp()
        output = f"{count}. {timestamp}, {price}"
        write_line(output)
        print(output)
        time.sleep(frequency)               # waits depending on how frequent the user wants the data
        count = count + 1                   # adds a count for user to know which value the line is currently on

    loading()
    print("successfully added to bitcoin-price.txt")

# Ethereum method
def ethereum():
    count = 1
    # main program
    print("---Ethereum to GBP---")
    while True:
        frequency = int(input("how often do you want to detect price change? (seconds) "))   # asks user for how often they want to detect
        if frequency < 1:
            print("sorry you please enter an integer more than 1")                           # only excepts values greater than one
        else:
            break
    times = int(input("how many times you you want to detect the price? "))                  # asks how many times

    print()
    print("     Date      Time     GBP(£)")                                                  # creates headings
    for x in range(times):                                                                   # depending on 'times' repeats gathering of price & time stamp
        price = get_price_eth()
        timestamp = get_timestamp()
        output = f"{count}. {timestamp}, {price}"
        write_line_eth(output)
        print(output)
        time.sleep(frequency)                                                                # waits depending on how frequent the user wants the data
        count = count + 1                                                                    # adds a count for user to know which value the line is currently on

    loading()                                                                                # displays loading dots
    print("successfully added to Ethereum-price.txt")


# main program


while True:
    try:
        question = input("what would you like to convert to GBP Bitcoin (B) OR Ethereum (E)? ")     # asks user which Crypto-currency they want to use
        question = question.upper()
        if question == 'E':
            ethereum()                                                                              # uses ethereum function
            break
        elif question == 'B':
            bitcoin()                                                                               # uses bitcoin function
            break
    except Exception:
        print("please enter a valid letter")
