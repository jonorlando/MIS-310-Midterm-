#Project 1: Book Club Points Calculator

from tkinter import *

# Create main application window
root = Tk()
root.title("Book Club Points Calculator")
root.geometry("400x300")
root.resizable(0, 0)  # Make window non-resizable as per requirements


# Function to calculate points based on books purchased
def calculate_points():
    try:
        # Get the number of books from entry widget and convert to integer
        books = int(entry.get())

        # Determine points based on the book purchase tiers
        if books < 0:
            result_label.config(text="Please enter a positive number")
        elif books == 0:
            result_label.config(text="Points earned: 0")
        elif books == 2:
            result_label.config(text="Points earned: 5")
        elif books == 4:
            result_label.config(text="Points earned: 15")
        elif books == 6:
            result_label.config(text="Points earned: 30")
        elif books >= 8:
            result_label.config(text="Points earned: 60")
        else:
            # For purchases of 1, 3, 5, 7 books (not in specified tiers)
            result_label.config(text="Points earned: 0")
    except:
        # Handle invalid input (non-numeric values)
        result_label.config(text="Please enter a valid number")


# Create instruction label widget
instruction_label = Label(root, text="Enter number of books purchased this month:", font=('Arial', 12))
instruction_label.pack(pady=20)  # Add vertical padding

# Create entry widget for user input
entry = Entry(root, font=('Arial', 12), width=10)
entry.pack(pady=10)  # Add vertical padding

# Create button to trigger points calculation
calculate_button = Button(root, text="Calculate Points", command=calculate_points, font=('Arial', 12))
calculate_button.pack(pady=10)  # Add vertical padding

# Create label to display results
result_label = Label(root, text="Points will be displayed here", font=('Arial', 12), fg='blue')
result_label.pack(pady=20)  # Add vertical padding

# Start the GUI event loop
root.mainloop()