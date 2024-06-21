import tkinter as tk
from tkinter import messagebox

import pharmacy


screen= tk.Tk()
screen.geometry('400x400')
screen.config(bg="#333333")
screen.title('Application Pharmacy Management System')

def Pharmacy_Manager_button():
    manager= tk.Toplevel(screen)
    manager.geometry('400x400')
    manager.title("Pharmacy Manage")
    tk.Label(manager, text="Pharmacy Manage").grid(row=0, column=0)

    #  Can Register 
    can_registre=tk.Button(manager,text="can registre:")
    can_registre.grid(row=1, column=12, padx=10, pady=10)
    

    #  Can Login 
    can_login=tk.Button(manager,text="can login:")
    can_login.grid(row=2, column=12, padx=10, pady=10)


    # Can add Medicine
    can_add=tk.Button(manager,text="Can add Medicine:")
    can_add.grid(row=3, column=12, padx=10, pady=10)


    # Can View Medicine
    can_view=tk.Button(manager,text="can registre:")
    can_view.grid(row=4, column=12, padx=10, pady=10)

    #  Can Delete Medicine
    can_delete=tk.Button(manager,text="can Delete Medicine:")
    can_delete.grid(row=5, column=12, padx=10, pady=10)
  
def admin_():
    admin= tk.Toplevel(screen)
    admin.geometry('400x400')
    admin.title("admin manager")
    tk.Label(admin, text="").grid(row=0, column=0)

    #  Can register 
    can_admin_register=tk.Button(admin,text="can register:",)
    can_admin_register.grid(row=1, column=12, padx=10, pady=10)

    #   Can Login 
    can_admin_login=tk.Button(admin,text="admin login")
    can_admin_login.grid(row=5,column=12)

    # Can View all manager
    can_view_all_manager=tk.Button(admin,text="can view all manager")
    can_view_all_manager.grid(row=8,column=12)

    #   Can View al medicine
    can_view_all_madicine=tk.Button(admin,text='Can View al medicine')
    can_view_all_madicine.grid(row=11,column=12)


login_button = tk.Button(screen, text="Pharmacy Manager", command=Pharmacy_Manager_button)
login_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

register_button = tk.Button(screen, text="Admin", command=admin_)
register_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

screen.mainloop()
