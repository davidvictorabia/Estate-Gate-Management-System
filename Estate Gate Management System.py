import random
import string
import datetime
import json
from tkinter import *
from tkinter import messagebox, ttk

class EstateGateSystem:
    def __init__(self):
        self.visitors = {}  # Store active visitors
        
    def generate_code(self, length=6):
        letters = string.ascii_uppercase
        numbers = string.digits
        code = ''.join(random.choices(letters + numbers, k=length))
        return code
    
    def register_visitor(self, name, phone, purpose, house_number):
        entry_code = self.generate_code(6)
        exit_code = self.generate_code(6)
        
        visitor_data = {
            "name": name,
            "phone": phone,
            "purpose": purpose,
            "house": house_number,
            "entry_code": entry_code,
            "exit_code": exit_code,
            "entry_time": datetime.datetime.now().strftime("%H:%M:%S"),
            "status": "Inside"
        }
        
        self.visitors[entry_code] = visitor_data
        
        print(f"\n✅ Visitor Registered Successfully!")
        print(f"Name: {name}")
        print(f"House: {house_number}")
        print(f"Entry Code: {entry_code}")
        print(f"Exit Code : {exit_code}")
        print(f"Time: {visitor_data['entry_time']}")
        
        return visitor_data
    
    def check_out(self, code):
        if code in self.visitors:
            visitor = self.visitors[code]
            visitor['status'] = "Exited"
            visitor['exit_time'] = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"\n✅ Check-out successful for {visitor['name']}")
            print(f"Exit Time: {visitor['exit_time']}")
            return True
        else:
            print("❌ Invalid Code!")
            return False

# ====================== GUI VERSION ======================
def main_gui():
    system = EstateGateSystem()
    
    root = Tk()
    root.title("Estate Gate Management System")
    root.geometry("700x600")
    root.configure(bg="#0f172a")
    
    Label(root, text="🏡 ESTATE GATE SYSTEM", font=("Arial", 20, "bold"), 
          bg="#0f172a", fg="#22d3ee").pack(pady=20)
    
    # Notebook (Tabs)
    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, expand=True, fill="both")
    
    # Tab 1: Register Visitor
    register_tab = Frame(notebook, bg="#1e2937")
    notebook.add(register_tab, text="Register Visitor")
    
    Label(register_tab, text="Visitor Name:", bg="#1e2937", fg="white", font=("Arial", 11)).place(x=50, y=50)
    name_entry = Entry(register_tab, width=40, font=("Arial", 12))
    name_entry.place(x=200, y=50)
    
    Label(register_tab, text="Phone Number:", bg="#1e2937", fg="white", font=("Arial", 11)).place(x=50, y=90)
    phone_entry = Entry(register_tab, width=40, font=("Arial", 12))
    phone_entry.place(x=200, y=90)
    
    Label(register_tab, text="Purpose of Visit:", bg="#1e2937", fg="white", font=("Arial", 11)).place(x=50, y=130)
    purpose_entry = Entry(register_tab, width=40, font=("Arial", 12))
    purpose_entry.place(x=200, y=130)
    
    Label(register_tab, text="House Number:", bg="#1e2937", fg="white", font=("Arial", 11)).place(x=50, y=170)
    house_entry = Entry(register_tab, width=40, font=("Arial", 12))
    house_entry.place(x=200, y=170)
    
    def register():
        name = name_entry.get()
        phone = phone_entry.get()
        purpose = purpose_entry.get()
        house = house_entry.get()
        
        if name and phone and purpose and house:
            data = system.register_visitor(name, phone, purpose, house)
            messagebox.showinfo("Success", f"Entry Code: {data['entry_code']}\nExit Code: {data['exit_code']}")
        else:
            messagebox.showwarning("Error", "All fields are required!")
    
    Button(register_tab, text="Generate Codes & Register", bg="#22d3ee", fg="black", 
           font=("Arial", 12, "bold"), command=register).place(x=180, y=230, width=300, height=50)
    
    # Tab 2: Check Out
    checkout_tab = Frame(notebook, bg="#1e2937")
    notebook.add(checkout_tab, text="Check Out")
    
    Label(checkout_tab, text="Enter Exit Code:", bg="#1e2937", fg="white", font=("Arial", 14)).pack(pady=50)
    code_entry = Entry(checkout_tab, font=("Arial", 16), justify="center", width=30)
    code_entry.pack(pady=10)
    
    def checkout():
        code = code_entry.get().strip().upper()
        if system.check_out(code):
            messagebox.showinfo("Success", "Visitor has successfully exited the estate.")
            code_entry.delete(0, END)
        else:
            messagebox.showerror("Invalid", "Invalid Exit Code!")
    
    Button(checkout_tab, text="CHECK OUT", bg="#ef4444", fg="white", 
           font=("Arial", 14, "bold"), command=checkout).pack(pady=30, ipadx=20, ipady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main_gui()