# This module defines a Jar class to simulate
# a cookie jar with deposit and withdrawal functionality.
# It also includes a command-line interface for user interaction.

class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("❌ Capacity must be a non-negative integer")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        if self._cookies == 0:
            return "empty🗑️"
        bar_length = 20
        filled_length = int(self._cookies / self._capacity * bar_length)
        bar = "🍪" * filled_length + "-" * (bar_length - filled_length)
        return f"[{bar}] {self._cookies}/{self._capacity} cookies"

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError(
                "❌ Number of cookies must be a non-negative integer")
        if self._cookies + n > self._capacity:
            raise ValueError("❌ Cannot deposit: exceeds jar capacity")
        self._cookies += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError(
                "❌ Number of cookies must be a non-negative integer")
        if n > self._cookies:
            raise ValueError("❌ Cannot withdraw: not enough cookies")
        self._cookies -= n

    def empty(self):
        self._cookies = 0

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies

    @property
    def is_full(self):
        return self._cookies == self._capacity

    @property
    def is_empty(self):
        return self._cookies == 0


def main():
    jar = Jar()
    print(
        f"🍪 Welcome! You have a cookie jar with capacity of {jar.capacity}.\n")

    while True:
        print(f"Current jar: {jar}")
        print("Options: [D]eposit🍪⬆️   [W]ithdraw🍪⬇️   [E]mpty🗑️   [Q]uit❎")
        choice = input("Choose an option: ").strip().lower()

        if choice == "d":
            if jar.is_full:
                print("🍪🎊 The jar is already full! Cannot deposit more. ❌")
            else:
                try:
                    n = int(input("How many cookies to deposit? 🍪 "))
                    jar.deposit(n)
                    print(f"✅ Deposited {n} cookies!")
                    if jar.is_full:
                        print("🎉 The jar is now full! 🍪🎊")
                except ValueError as e:
                    print(f"{e}")

        elif choice == "w":
            if jar.is_empty:
                print("😢 The jar is empty. Nothing to withdraw. ❌")
            else:
                try:
                    n = int(input("How many cookies to withdraw? 🍪 "))
                    jar.withdraw(n)
                    print(f"✅ Withdrew {n} cookies!")
                    if jar.is_empty:
                        print("😢 The jar is now empty.")
                except ValueError as e:
                    print(f"{e}")

        elif choice == "e":
            if jar.is_empty:
                print("🗑️ The jar is already empty. 😢")
            else:
                jar.empty()
                print("🗑️ The jar has been emptied. 🍪 ➡️ 🗑️")

        elif choice == "q":
            print(f"👋 Exiting. Final jar: {jar}")
            break

        else:
            print("❌ Invalid option. Please choose D, W, E, or Q.")

        print()  # blank line for readability


if __name__ == "__main__":
    main()
