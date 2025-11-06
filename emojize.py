# This script takes a string input containing emoji codes/aliases
# and converts them into actual emojis using the 'emoji' library.

import emoji  # install via: pip install emoji


def main():
    # Prompt user for input
    text = input(
        "Enter a string with emoji codes (e.g., I am happy :smile:): ")

    # Convert codes/aliases into actual emojis
    emojized_text = emoji.emojize(text, language="alias")

    # Output the emojized string
    print("Emojized:", emojized_text)


if __name__ == "__main__":
    main()
