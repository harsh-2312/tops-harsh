# import tkinter as tk
# from tkinter import messagebox
# import re

# screen = tk.Tk()
# screen.geometry('400x400')
# screen.config(bg="#333333")
# screen.title('Application Pharmacy Management System')

# def Pharmacy_Manager_button():
#     manager = tk.Toplevel(screen)
#     manager.geometry('400x400')
#     manager.title("Pharmacy Manage")
#     tk.Label(manager, text="Pharmacy Manage").grid(row=0, column=0)

#     # Can Register 
#     can_register = tk.Button(manager, text="Can Register", command=can_register_m)
#     can_register.grid(row=2, column=0)

#     # Can Login 
#     can_login = tk.Button(manager, text="Can Login")
#     can_login.grid(row=4, column=0)

#     # Can Add Medicine
#     can_add = tk.Button(manager, text="Can Add Medicine")
#     can_add.grid(row=6, column=0)

#     # Can View Medicine
#     can_view = tk.Button(manager, text="Can View Medicine")
#     can_view.grid(row=8, column=0)

#     # Can Delete Medicine
#     can_delete = tk.Button(manager, text="Can Delete Medicine")
#     can_delete.grid(row=10, column=0)

# def can_register_m():
#     manager_reg = tk.Toplevel(screen)
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
#     password_entry = tk.Entry(manager_reg, show="*")
#     password_entry.grid(row=4, column=1)

#     password_error_label = tk.Label(manager_reg, text="", fg="red")
#     password_error_label.grid(row=5, column=1)

#     c_password_label = tk.Label(manager_reg, text="Confirm Password : ")
#     c_password_label.grid(row=6, column=0)
#     c_password_entry = tk.Entry(manager_reg, show="*")
#     c_password_entry.grid(row=6, column=1)

#     c_password_error_label = tk.Label(manager_reg, text="", fg="red")
#     c_password_error_label.grid(row=7, column=1)

#     def validate_email(email):
#         pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
#         return re.match(pattern, email)

#     def validate_password(password):
#         return re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$', password)

#     def get_register_data():
#         username = username_entry.get()
#         email = email_entry.get()
#         password = password_entry.get()
#         c_password = c_password_entry.get()

#         if not validate_email(email):
#             messagebox.showerror("Error", "Invalid email")
#             return
#         else:
#             email_error_label.config(text="")

#         if not validate_password(password):
#             messagebox.showerror("Error", "Invalid password")
#             return
#         else:
#             password_error_label.config(text="")

#         if password != c_password:
#             messagebox.showerror("Error", "Passwords do not match")
#             return
#         else:
#             c_password_error_label.config(text="")

#         messagebox.showinfo("Success", "Registration Successful!")
#         manager_reg.destroy()

#     register_button = tk.Button(manager_reg, text="Register", command=get_register_data)
#     register_button.grid(row=8, column=0, columnspan=2)

# def admin_():
#     admin = tk.Toplevel(screen)
#     admin.geometry('400x400')
#     admin.title("Pharmacy Manage")
#     tk.Label(admin, text="admin").grid(row=0, column=0)

#     # Can register
#     can_admin_register = tk.Button(admin, text="Can Register")
#     can_admin_register.grid(row=3, column=0)

#     # Can Login
#     can_admin_login = tk.Button(admin, text="Admin Login")
#     can_admin_login.grid(row=6, column=0)

#     # Can View all manager
#     can_view_all_manager = tk.Button(admin, text="Can View all manager")
#     can_view_all_manager.grid(row=9, column=0)

#     # Can View all medicine
#     can_view_all_medicine = tk.Button(admin, text='Can View all medicine')
#     can_view_all_medicine.grid(row=12, column=0)

# login_button = tk.Button(screen, text="Pharmacy Manager", command=Pharmacy_Manager_button)
# login_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# register_button = tk.Button(screen, text="Admin", command=admin_)
# register_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# screen.mainloop()
