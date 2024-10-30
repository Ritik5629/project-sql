import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime

# Database connection function
def connect_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",  
            password="HP55@5629",  
            database="fitness_db"  
        )
    except mysql.connector.Error as err:
        messagebox.showerror("Database Connection Error", f"Error: {err}")
        return None

# Function to insert a new member
def insert_member():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    membership = membership_combo.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    join_date = join_date_entry.get().strip()
    
    if not name or not age or not membership or not email or not phone or not join_date:
        messagebox.showwarning("Input Error", "Please fill out all fields.")
        return
    
    try:
        age_int = int(age)
        # Convert the input date from DD-MM-YYYY to YYYY-MM-DD
        join_date_obj = datetime.strptime(join_date, "%d-%m-%Y")
        join_date_formatted = join_date_obj.strftime("%Y-%m-%d")
    except ValueError:
        messagebox.showwarning("Input Error", "Age must be a number and date must be in DD-MM-YYYY format.")
        return
    
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(""" 
                INSERT INTO members (name, age, membership_type, email, phone, join_date) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (name, age_int, membership, email, phone, join_date_formatted))
            conn.commit()
            messagebox.showinfo("Success", "Member added successfully.")
            clear_entries()
            refresh_treeview()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

# Function to view all members
def view_members():
    refresh_treeview()

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    membership_combo.set('')
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    join_date_entry.delete(0, tk.END)

# Function to refresh the treeview with data from the database
def refresh_treeview():
    for row in tree.get_children():
        tree.delete(row)

    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            # Format join_date as DD-MM-YYYY directly in the SQL query
            cursor.execute("SELECT name, age, membership_type, email, phone, DATE_FORMAT(join_date, '%d-%m-%Y') AS join_date FROM members")
            rows = cursor.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

# Create the main window
root = tk.Tk()
root.title("Fitness Management System")
root.geometry("600x400")
root.config(bg="lightblue")

# Create Labels and Entry widgets
tk.Label(root, text="Member Name", bg="lightblue", font=("Arial", 12)).grid(row=0, column=0, padx=20, pady=10, sticky=tk.W)
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Age", bg="lightblue", font=("Arial", 12)).grid(row=1, column=0, padx=20, pady=10, sticky=tk.W)
age_entry = tk.Entry(root, width=30)
age_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Membership Type", bg="lightblue", font=("Arial", 12)).grid(row=2, column=0, padx=20, pady=10, sticky=tk.W)
membership_combo = ttk.Combobox(root, values=["Monthly", "Quarterly", "Yearly"], state="readonly", width=28)
membership_combo.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Email", bg="lightblue", font=("Arial", 12)).grid(row=3, column=0, padx=20, pady=10, sticky=tk.W)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Phone Number", bg="lightblue", font=("Arial", 12)).grid(row=4, column=0, padx=20, pady=10, sticky=tk.W)
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=4, column=1, padx=10, pady=10)

tk.Label(root, text="Join Date (DD-MM-YYYY)", bg="lightblue", font=("Arial", 12)).grid(row=5, column=0, padx=20, pady=10, sticky=tk.W)
join_date_entry = tk.Entry(root, width=30)
join_date_entry.grid(row=5, column=1, padx=10, pady=10)

# Create buttons and position them properly
button_frame = tk.Frame(root, bg="lightblue")
button_frame.grid(row=6, column=0, columnspan=2, pady=10)

add_button = tk.Button(button_frame, text="Add Member", command=insert_member, bg="green", fg="white", font=("Arial", 12), width=20)
add_button.grid(row=0, column=0, padx=10)

view_button = tk.Button(button_frame, text="View Members", command=view_members, bg="blue", fg="white", font=("Arial", 12), width=20)
view_button.grid(row=0, column=1, padx=10)

# Create a frame for the treeview and scrollbar
frame = tk.Frame(root, bg="lightblue", width=800, height=300)
frame.grid(row=7, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

# Configure grid weights for the frame
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Create a treeview to display data
tree = ttk.Treeview(frame, columns=("name", "age", "membership_type", "email", "phone", "join_date"), show="headings", height=15)
tree.heading("name", text="Name")
tree.heading("age", text="Age")
tree.heading("membership_type", text="Membership Type")
tree.heading("email", text="Email")
tree.heading("phone", text="Phone")
tree.heading("join_date", text="Join Date")

# Center-align all columns
tree.column("name", width=200, anchor=tk.CENTER)
tree.column("age", width=100, anchor=tk.CENTER)
tree.column("membership_type", width=150, anchor=tk.CENTER)
tree.column("email", width=250, anchor=tk.CENTER)
tree.column("phone", width=150, anchor=tk.CENTER)
tree.column("join_date", width=150, anchor=tk.CENTER)

tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a scrollbar
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tree.configure(yscrollcommand=scrollbar.set)

# Initially populate the treeview
refresh_treeview()

root.mainloop()
