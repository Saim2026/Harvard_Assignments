# This program determines meal times based on user input time.
# It converts the input time from "HH:MM" format to a float representation
# and checks if it falls within breakfast, lunch, or dinner time ranges.

def main():
    print("⏰ Welcome! Let's check if it's meal time. 🍽️")
    print("Enter time in 24-hour format (HH:MM). Example: 07:30\n")

    while True:
        time_input = input("What time is it? (HH:MM) or 'q' to quit: ").strip()
        if time_input.lower() == 'q':
            print("👋 Goodbye! Stay hungry 😉")
            break

        try:
            hours = convert(time_input)
            if not (0 <= hours < 24):
                raise ValueError("Time must be within 00:00 to 23:59")
        except ValueError as e:
            print(f"❌ Invalid input: {e}. Please try again.\n")
            continue

        # Check meal times
        if 7 <= hours <= 8:
            print("🍳 Breakfast Time! 🥐\n")
        elif 12 <= hours <= 13:
            print("🥗 Lunch Time! 🍔\n")
        elif 18 <= hours <= 19:
            print("🍽️  Dinner Time! 🍝\n")
        else:
            print("😢 Sorry, it's not a meal time.\n")


def convert(time_str):
    """Convert HH:MM string to float hours"""
    try:
        parts = time_str.split(":")
        if len(parts) != 2:
            raise ValueError("Time must be in HH:MM format")
        hours = int(parts[0])
        minutes = int(parts[1])
        if not (0 <= hours <= 23) or not (0 <= minutes <= 59):
            raise ValueError("Hours must be 0-23 and minutes 0-59")
        return hours + minutes / 60
    except ValueError:
        raise ValueError("Invalid number format for hours or minutes")


if __name__ == "__main__":
    main()
