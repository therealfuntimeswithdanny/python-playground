import random

def generate_random_number(start=1, end=100):
    """
    Generate a random integer between 'start' and 'end' (inclusive).
    
    Parameters:
    start (int): The lowest possible integer.
    end (int): The highest possible integer.
    
    Returns:
    int: A random integer between start and end.
    """
    return random.randint(start, end)

if __name__ == "__main__":
    print("=== Random Number Generator ===")
    
    # Optionally, let the user customize the range
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
    except ValueError:
        print("Invalid input! Please enter integer values.")
        exit(1)
        
    if start > end:
        print("Error: The start must be less than or equal to the end.")
        exit(1)
    
    while True:
        number = generate_random_number(start, end)
        print(f"\nYour random number is: {number}")
        
        # Ask if the user would like to generate another number
        again = input("\nWould you like to generate a new number? (y/n): ").strip().lower()
        if again not in ('y', 'yes'):
            print("Thanks for using the Random Number Generantor! Goodbye.")
            print("_________________________")
            print("Follow me on Bluesky @madebydanny.uk")
            print("Fork this project on GitHub! @ therealfuntimeswithdanny/python-playground")
            print("_________________________")
            print("End of Python Script")
            print("Code is open source and free to use!")
            break
