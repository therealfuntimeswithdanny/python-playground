import tkinter as tk
import random

def generate_number():
    try:
        # Get the starting and ending values from the entry widgets
        start = int(start_entry.get())
        end = int(end_entry.get())

        # Validate that the start of the range is not greater than the end
        if start > end:
            result_label.config(text="Error: Start must be ≤ End")
            return

        # Generate and display the random number
        number = random.randint(start, end)
        result_label.config(text=f"Random number: {number}")
    except ValueError:
        result_label.config(text="Invalid input! Please enter valid integers.")

# Initialize the main window
root = tk.Tk()
root.title("Number Generator")
root.geometry("300x200")  # Set a fixed size for the window

# Create and position the label and entry for the start of the range
start_label = tk.Label(root, text="Start of Range:")
start_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
start_entry = tk.Entry(root)
start_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and position the label and entry for the end of the range
end_label = tk.Label(root, text="End of Range:")
end_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
end_entry = tk.Entry(root)
end_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and position the "Generate" button
generate_button = tk.Button(root, text="Generate", command=generate_number)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

# A label to display the result or error messages
result_label = tk.Label(root, text="Developed by Daniel Morrisey, madebydanny.uk")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
