# import tkinter as tk
# from tkinter import messagebox
# import re

# screen= tk.Tk()
# screen.geometry('400x400')
# screen.config(bg="#333333")
# screen.title('Application Pharmacy Management System')

# def Pharmacy_Manager_button():
#     manager= tk.Toplevel(screen)
#     manager.geometry('400x400')
#     manager.title("Pharmacy Manage")
#     tk.Label(manager, text="Pharmacy Manage").grid(row=0, column=0)

#     #  Can Register 
#     can_registre=tk.Button(manager,text="can registre:",command=can_registre_m)
#     can_registre.grid(row=2,column=0)
    
#     #  Can Login 
#     can_login=tk.Button(manager,text="can login:")
#     can_login.grid(row=4,column=0)

#     # Can add Medicine
#     can_add=tk.Button(manager,text="Can add Medicine:")
#     can_add.grid(row=6,column=0)

#     # Can View Medicine
#     can_view=tk.Button(manager,text="can registre:")
#     can_view.grid(row=8,column=0)

#     #  Can Delete Medicine
#     can_delete=tk.Button(manager,text="can Delete Medicine:")
#     can_delete.grid(row=10,column=0)

# def can_registre_m():
#     manager_reg= tk.Toplevel(screen)
#     manager_reg.geometry('400x400')
#     manager_reg.title("Manage register")
#     tk.Label(manager_reg, text="Manage Create your account ").grid(row=0, column=0)

#     username_label = tk.Label(manager_reg, text="Username : ")
#     username_label.grid(row=1, column=0)
#     username_entry = tk.Entry(manager_reg)
#     username_entry.grid(row=1, column=1)

#     email_label = tk.Label(manager_reg, text="Email : ")
#     email_label.grid(row=2, column=0)
#     email_entry = tk.Entry(manager_reg)
#     email_entry.grid(row=2, column=1)

#     email_error_label = tk.Label(manager_reg, text="", fg="red")
#     email_error_label.grid(row=3, column=1)

#     password_label = tk.Label(manager_reg, text="Password : ")
#     password_label.grid(row=4, column=0)
#     password_entry = tk.Entry(manager_reg)
#     password_entry.grid(row=4, column=1)

#     password_error_label = tk.Label(manager_reg, text="", fg="red")
#     password_error_label.grid(row=5, column=1)

#     c_password_label = tk.Label(manager_reg, text="c_Password : ")
#     c_password_label.grid(row=6, column=0)
#     c_password_entry = tk.Entry(manager_reg)
#     c_password_entry.grid(row=6, column=1)

#     c_password_error_label = tk.Label(manager_reg, text="", fg="red")
#     c_password_error_label.grid(row=5, column=1)

#         # Function to validate email

# def validate_email(email):
#     pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
#     return re.match(pattern, email)
    
#     # Function to validate password
# def validate_password(password):
#     return re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$', password)

#     # Function to get registration data
# def get_register_data():
#     # Retrieve user inputs
#     username = username_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     c_password = c_password_entry.get()

#         # Validate email
#     if not validate_email(email):
#         email_error_label.config(text="Invalid email")
#         return
#     else:
#         email_error_label.config(text="")

#     # Validate password
#     if not validate_password(password):
#         password_error_label.config(text="Invalid password")
#         return
#     else:
#         password_error_label.config(text="")

#     # Confirm password
#     if password != c_password:
#         c_password_error_label.config(text="Passwords do not match")
#         return
#     else:
#         c_password_error_label.config(text="")

#     # Print the retrieved data (for testing purposes)
#     print("Username:", username)
#     print("Email:", email)
#     print("Password:", password)
#     print("Confirm Password:", c_password)






    

# def admin_():
#     admin= tk.Toplevel(screen)
#     admin.geometry('400x400')
#     admin.title("Pharmacy Manage")
#     tk.Label(admin, text="admin").grid(row=0, column=0)

#     #  Can register 
#     can_admin_register=tk.Button(admin,text="can register:")
#     can_admin_register.grid(row=3,column=0)

#     #   Can Login 
#     can_admin_login=tk.Button(admin,text="admin login")
#     can_admin_login.grid(row=6,column=0)

#     # Can View all manager
#     can_view_all_manager=tk.Button(admin,text="can view all manager")
#     can_view_all_manager.grid(row=9,column=0)

#     #   Can View al medicine
#     can_view_all_madicine=tk.Button(admin,text='Can View al medicine')
#     can_view_all_madicine.grid(row=12,column=0)


# login_button = tk.Button(screen, text="Pharmacy Manager", command=Pharmacy_Manager_button)
# login_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# register_button = tk.Button(screen, text="Admin", command=admin_)
# register_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# screen.mainloop()