#Project 2 Part One: CCSU Mobile App (Basic Version)

from tkinter import *
from PIL import ImageTk, Image  # Import PIL for image handling
import pandas as pd
from io import StringIO

# Sample CSV data structure - REPLACE WITH ACTUAL midterm_exam.csv FILE
csv_data = """Buildings,CalendarDate,FacultyName
Elihu Burritt Library,2025-08-25 – Classes Begin,Armel D
Copernicus Hall,2025-08-29 – Last Day to Add/Drop,Jordan Nguyen
Willard–DiLoreto Hall,2025-09-01 – Labor Day – No Classes,Taylor Patel
Maria Sanford Hall,2025-09-09 – Census Date,Casey Garcia
Barnard Hall,2025-10-20 – Midterm Week Begins,Morgan Lopez"""

# Window setup and configuration

root = Tk()
root.title('CCSU Mobile App')  # Set window title as required
root.geometry("600x550")  # Increased height to accommodate logo space
root.resizable(0, 0)  # Make window non-resizable
root.configure(bg='light blue')  # Set light blue background as required


# Load and prepare data from CSV

# Read CSV data into pandas DataFrame
# REPLACE StringIO(csv_data) WITH "midterm_exam.csv" when you have the actual file
data = pd.read_csv(StringIO(csv_data))

# Create logo display at top of GUI USING YOUR ACTUAL LOGO IMAGE

try:
    # Load and resize your logo image (logo1 (1).png should be in same directory)
    img = Image.open('logo1 (1).png')
    img = img.resize((120, 120), Image.Resampling.LANCZOS)  # Resize to fit nicely at top
    logo = ImageTk.PhotoImage(img)

    # Create label with the actual image logo
    logo_label = Label(root, image=logo, bg='light blue')
    logo_label.place(x=10, y=10)  # Position at top-left corner
    logo_label.image = logo  # Keep reference to prevent garbage collection

    # Add some space below the logo for the buttons
    logo_bottom = 140  # logo y=10 + logo height=120 + 10px padding

except Exception as e:
    # Fallback to text logo if image file is not found
    print(f"Image loading error: {e}")
    logo_label = Label(root, text="CCSU\nMOBILE APP", bg='light blue',
                       font=('Arial', 14, 'bold'), fg='dark blue')
    logo_label.place(x=10, y=10)
    logo_bottom = 80  # Adjust for text logo

# Create result display area - POSITIONED BELOW BUTTONS

# Single label widget that displays output from all buttons
# Prevents overlapping by updating the same widget
result_label = Label(root, text="Select a button to display information",
                     bg='white', font=('Arial', 10), justify=LEFT,
                     wraplength=500, relief=SOLID, bd=1)
result_label.place(x=50, y=250, width=500, height=250)  # Moved down to y=250

# Button function definitions

def calendar():
    """Display calendar dates from CSV data"""
    # Extract only CalendarDate column from DataFrame
    df = pd.DataFrame(data, columns=['CalendarDate'])
    # Remove any rows with missing calendar dates
    selected_rows = df[~df['CalendarDate'].isnull()]
    # Update result label with formatted calendar data
    result_label.config(text="CALENDAR DATES:\n\n" + selected_rows.to_string(index=False))


def building():
    """Display building information from CSV data"""
    # Extract only Buildings column from DataFrame
    df = pd.DataFrame(data, columns=['Buildings'])
    # Remove any rows with missing building data
    selected_rows = df[~df['Buildings'].isnull()]
    # Update result label with formatted building data
    result_label.config(text="CAMPUS BUILDINGS:\n\n" + selected_rows.to_string(index=False))


def faculty():
    """Display faculty information from CSV data"""
    # Extract only FacultyName column from DataFrame
    df = pd.DataFrame(data, columns=['FacultyName'])
    # Remove any rows with missing faculty data
    selected_rows = df[~df['FacultyName'].isnull()]
    # Update result label with formatted faculty data
    result_label.config(text="FACULTY MEMBERS:\n\n" + selected_rows.to_string(index=False))

# Create and position buttons horizontally BELOW THE LOGO

# Button 1: Calendar - displays academic calendar dates
button1 = Button(root, text='Calendar', command=calendar, width=12, height=2)
button1.place(x=50, y=150)  # Positioned below logo (was y=120)

# Button 2: Buildings - displays campus building information
button2 = Button(root, text='Buildings', command=building, width=12, height=2)
button2.place(x=180, y=150)  # Positioned below logo (was y=120)

# Button 3: Faculty - displays faculty member names
button3 = Button(root, text='Faculty', command=faculty, width=12, height=2)
button3.place(x=310, y=150)  # Positioned below logo (was y=120)

# Start the application

root.mainloop()