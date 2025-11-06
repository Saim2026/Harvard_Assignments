# This program simulates a coke machine that accepts coins until the price of a coke is paid.

def main():

    price = 50
    amount_due = price

    while amount_due > 0:
        print("\nPlease Enter Amount in cents (25, 10, 5):")
        print("Amount Due = ", amount_due, "¢")
        coin = int(input("Enter your Coin: "))
        if coin in [25, 10, 5]:
            amount_due -= coin  # amount_due = amount_due - coin
        else:
            print("Invalid coin. Please insert 25, 10, or 5 cents. ")

    # we call abs(amount_due) to flip it to positive, abs(-10) = 10
    print("Change Owed:", abs(amount_due), "¢")

    print("\n****Thank you!*******\n")


if __name__ == "__main__":
    main()
