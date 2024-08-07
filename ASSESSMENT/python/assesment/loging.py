import tkinter as tk
import re
from tkinter import messagebox

screen = tk.Tk()

screen.geometry('400x400')
screen.config(bg="#333333")
screen.title('Witzcode-Menu')

def open_register_window():
    register_window = tk.Toplevel(screen)
    register_window.geometry('300x200')
    register_window.title('Witzcode-Register')
    
    tk.Label(register_window, text="Create your account").grid(row=0, column=0)

    # Create labels and entry fields for user input
    username_label = tk.Label(register_window, text="Username : ")
    username_label.grid(row=1, column=0)
    username_entry = tk.Entry(register_window)
    username_entry.grid(row=1, column=1)

    email_label = tk.Label(register_window, text="Email : ")
    email_label.grid(row=2, column=0)
    email_entry = tk.Entry(register_window)
    email_entry.grid(row=2, column=1)

    email_error_label = tk.Label(register_window, text="", fg="red")
    email_error_label.grid(row=3, column=1)

    password_label = tk.Label(register_window, text="Password : ")
    password_label.grid(row=4, column=0)
    password_entry = tk.Entry(register_window, show="*")
    password_entry.grid(row=4, column=1)

    password_error_label = tk.Label(register_window, text="", fg="red")
    password_error_label.grid(row=5, column=1)

    c_password_label = tk.Label(register_window, text="Confirm Password : ")
    c_password_label.grid(row=6, column=0)
    c_password_entry = tk.Entry(register_window)
    c_password_entry.grid(row=6, column=1)

    c_password_error_label = tk.Label(register_window, text="", fg="red")
    c_password_error_label.grid(row=7, column=1)

    # Function to validate email
    def validate_email(email):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
        return re.match(pattern, email)
    
    # Function to validate password
    def validate_password(password):
        return re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$', password)

   

    # Function to get registration data
    def get_register_data():
        # Retrieve user inputs
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        c_password = c_password_entry.get()
        
        # Validate email
        if not validate_email(email):
            email_error_label.config(text="Invalid email")
            return
        else:
            email_error_label.config(text="")

        # Validate password
        if not validate_password(password):
            password_error_label.config(text="Invalid password")
            return
        else:
            password_error_label.config(text="")

        # Confirm password
        if password != c_password:
            c_password_error_label.config(text="Passwords do not match")
            return
        else:
            c_password_error_label.config(text="")

        # Print the retrieved data (for testing purposes)
        print("Username:", username)
        print("Email:", email)
        print("Password:", password)
        print("Confirm Password:", c_password)

        # Add further processing logic here, like validating inputs, saving to database, etc.

    # Button to trigger registration
    tk.Button(register_window, text='Register', command=get_register_data).grid(row=8, column=1)


    # Function to open a new window
def open_login_window():
    login_window = tk.Toplevel(screen)
    login_window.geometry('300x200')
    login_window.config(bg="#333333")
    login_window.title('Witzcode-Login')
    tk.Label(login_window, text="Login your account").grid(row=0, column=0)

    email_label = tk.Label(login_window, text="Email : ")
    email_label.grid(row=2, column=0)
    email_entry = tk.Entry(login_window)
    email_entry.grid(row=2, column=1)

    password_label = tk.Label(login_window, text="Password : ")
    password_label.grid(row=3, column=0)
    password_entry = tk.Entry(login_window)
    password_entry.grid(row=3, column=1)

    # Function to get login data
    def get_login_data():
        # Retrieve user inputs
        email = email_entry.get()
        password = password_entry.get()

        print("Email:", email)
        print("Password:", password)

    tk.Button(login_window, text='Login', command=get_login_data).grid(row=5, column=1)


# Define button style
button_style = {
    "bg": "lightblue",  # Background color
    "fg": "black",      # Foreground color
    "padx": 10,         # Horizontal padding
    "pady": 5,           # Vertical padding
    "font": ('Arial', 12)  # Font family and size
}

login_button = tk.Button(screen, text="Login", command=open_login_window, **button_style)
register_button = tk.Button(screen, text="Register", command=open_register_window, **button_style)

# Place the Login button
login_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Place the Register button
register_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

screen.mainloop()
