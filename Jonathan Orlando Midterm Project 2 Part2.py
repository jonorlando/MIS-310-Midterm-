#Project 2 Part Two: Enhanced CCSU Mobile App

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
root.title('CCSU Mobile App')  # Set window title as specified
root.geometry("650x650")  # Increased size to accommodate logo and buttons
root.resizable(0, 0)  # Window cannot be resized
root.configure(bg='light blue')  # Light blue background as required

# Load CSV data

# Read the CSV file into a pandas DataFrame
# REPLACE StringIO(csv_data) WITH "midterm_exam.csv" for actual implementation
data = pd.read_csv(StringIO(csv_data))

# Create logo display USING YOUR ACTUAL LOGO IMAGE

try:
    # Load your logo image file (logo1 (1).png must be in same directory)
    img = Image.open('logo1 (1).png')
    img = img.resize((120, 120), Image.Resampling.LANCZOS)  # Resize for proper placement
    logo = ImageTk.PhotoImage(img)

    # Create label widget with the actual image logo
    logo_label = Label(root, image=logo, bg='light blue')
    logo_label.place(x=10, y=10)  # Position at top-left, not occupying full GUI
    logo_label.image = logo  # Maintain reference to prevent image garbage collection

    # Calculate space needed for logo
    logo_space = 140  # logo y=10 + height=120 + 10px padding

except Exception as e:
    # Fallback to text logo if image cannot be loaded
    print(f"Image loading error: {e}")
    logo_label = Label(root, text="CCSU\nMOBILE APP", bg='light blue',
                       font=('Arial', 14, 'bold'), fg='dark blue')
    logo_label.place(x=10, y=10)
    logo_space = 80  # Adjust for text logo

# Create enhanced output display area - POSITIONED LOWER

# Text widget provides better formatting and scrolling capabilities
output_text = Text(root, wrap=WORD, width=70, height=20, bg='white',
                   font=('Arial', 10), relief=SOLID, bd=1)
output_text.place(x=50, y=300, width=550, height=300)  # Moved down to y=300
output_text.config(state=DISABLED)  # Initially set to read-only

# Add scrollbar for content that exceeds display area
scrollbar = Scrollbar(root, command=output_text.yview)
scrollbar.place(x=600, y=300, height=300)  # Adjusted y position
output_text.config(yscrollcommand=scrollbar.set)

# Button functions for Part One requirements

def calendar():
    """Display academic calendar dates from CSV column"""
    output_text.config(state=NORMAL)  # Enable editing to update content
    output_text.delete(1.0, END)  # Clear previous content to prevent overlap
    # Extract and filter calendar date data
    df = pd.DataFrame(data, columns=['CalendarDate'])
    selected_rows = df[~df['CalendarDate'].isnull()]
    # Format and display the data
    output_text.insert(END, "ACADEMIC CALENDAR:\n\n")
    output_text.insert(END, selected_rows.to_string(index=False))
    output_text.config(state=DISABLED)  # Set back to read-only


def building():
    """Display campus buildings from CSV column"""
    output_text.config(state=NORMAL)
    output_text.delete(1.0, END)  # Clear previous content
    # Extract and filter building data
    df = pd.DataFrame(data, columns=['Buildings'])
    selected_rows = df[~df['Buildings'].isnull()]
    # Format and display the data
    output_text.insert(END, "CAMPUS BUILDINGS:\n\n")
    output_text.insert(END, selected_rows.to_string(index=False))
    output_text.config(state=DISABLED)


def faculty():
    """Display faculty members from CSV column"""
    output_text.config(state=NORMAL)
    output_text.delete(1.0, END)  # Clear previous content
    # Extract and filter faculty data
    df = pd.DataFrame(data, columns=['FacultyName'])
    selected_rows = df[~df['FacultyName'].isnull()]
    # Format and display the data
    output_text.insert(END, "FACULTY MEMBERS:\n\n")
    output_text.insert(END, selected_rows.to_string(index=False))
    output_text.config(state=DISABLED)

# Button functions for Part Two additional requirements

def business():
    """Display School of Business department information"""
    output_text.config(state=NORMAL)
    output_text.delete(1.0, END)  # Clear previous content
    # Pre-defined business department list as specified in requirements
    business_info = """SCHOOL OF BUSINESS DEPARTMENTS:

• Accounting
• Finance
• Management & Organization
• Marketing
• Management Information Systems (MIS)
• Business Analytics"""
    output_text.insert(END, business_info)
    output_text.config(state=DISABLED)


def mis_department():
    """Display MIS Department course information"""
    output_text.config(state=NORMAL)
    output_text.delete(1.0, END)  # Clear previous content
    # Pre-defined MIS course list as specified in requirements
    mis_courses = """MIS DEPARTMENT COURSES:

• Intro to MIS
• Databases Management
• Systems Analysis & Design
• Business Analytics / Data Visualization
• Network and Information Security
• Project Management"""
    output_text.insert(END, mis_courses)
    output_text.config(state=DISABLED)

# Create and position all buttons horizontally BELOW THE LOGO

# Part One Required Buttons (first three)
button1 = Button(root, text='Calendar', command=calendar, width=12, height=2)
button1.place(x=50, y=150)  # Positioned below logo (was y=120)

button2 = Button(root, text='Buildings', command=building, width=12, height=2)
button2.place(x=160, y=150)  # Positioned below logo (was y=120)

button3 = Button(root, text='Faculty', command=faculty, width=12, height=2)
button3.place(x=270, y=150)  # Positioned below logo (was y=120)

# Part Two Additional Buttons with different background colors
button4 = Button(root, text='School of Business', command=business,
                 bg="light coral", width=15, height=2)  # Light coral background
button4.place(x=380, y=150)  # Positioned below logo (was y=120)

button5 = Button(root, text='MIS Department', command=mis_department,
                 bg="light yellow", width=15, height=2)  # Light yellow background
button5.place(x=510, y=150)  # Positioned below logo (was y=120)

# Initialize with welcome message

output_text.config(state=NORMAL)
output_text.insert(END, "Welcome to CCSU Mobile App!\n\nClick any button to display information.")
output_text.config(state=DISABLED)

# Start the application

root.mainloop()