# This program mimics the behavior of the 'figlet' command-line tool.
# It takes an optional font argument and prints the input text in ASCII art.
# Usage:
#   python figlet.py                # Uses a random font
#   python figlet.py -f <fontname>  # Uses the specified font

import sys
import random
from pyfiglet import Figlet      # pip install pyfiglet


def main():
    figlet = Figlet()
    available_fonts = figlet.getFonts()

    # --- Validate arguments ---
    if len(sys.argv) == 1:
        # Zero args → random font
        chosen_font = random.choice(available_fonts)
    elif len(sys.argv) == 3:
        flag, fontname = sys.argv[1], sys.argv[2]
        if flag not in ["-f", "--font"] or fontname not in available_fonts:
            sys.exit("Invalid usage")
        chosen_font = fontname
    else:
        sys.exit("Invalid usage")

    # --- Set font ---
    figlet.setFont(font=chosen_font)

    # --- Prompt and output ---
    s = input("Input: ")
    print(figlet.renderText(s))


if __name__ == "__main__":
    main()
