import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import os

class TrafficApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Traffic Offense System")
        self.master.geometry("400x300")

        self.style = ttk.Style()
        self.style.configure("App.TButton", foreground="black", background="black", font=("Helvetica", 12), padding=10)
        self.style.configure("App.TLabel", foreground="#4CAF50", font=("Helvetica", 12))
        self.style.configure("App.TFrame", background="#f5f5f5", borderwidth=2, relief="groove", padding=10)

        self.offenders = []  # List to store offenders
        self.offender_id = 1  # Initial offender ID

        self.frame = ttk.Frame(self.master)
        self.frame.pack()

        self.show_login()

    def show_login(self):
        self.frame.destroy()
        self.frame = ttk.Frame(self.master)
        self.frame.pack()

        ttk.Label(self.frame, text="Traffic Offense System", font=('Helvetica', 20, 'bold'), style="App.TLabel").grid(row=0, columnspan=2, padx=10, pady=10)

        image_path = os.path.join(os.path.expanduser("~"), "Desktop", "frsc.jpeg")
        if os.path.exists(image_path):
            image = Image.open(image_path)
            image = image.resize((200, 200))
            logo_image = ImageTk.PhotoImage(image)
            ttk.Label(self.frame, image=logo_image, style="App.TLabel").grid(row=1, columnspan=2, padx=10, pady=10)
            # Keep a reference to the image to prevent garbage collection
            self.logo_image = logo_image
        else:
            ttk.Label(self.frame, text="Logo image not found", style="App.TLabel").grid(row=1, columnspan=2, padx=10, pady=10)

        ttk.Label(self.frame, text="Username:", style="App.TLabel").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = ttk.Entry(self.frame)
        self.username_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.frame, text="Password:", style="App.TLabel").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = ttk.Entry(self.frame, show="*")
        self.password_entry.grid(row=3, column=1, padx=10, pady=5)

        ttk.Button(self.frame, text="Login", command=self.login, style="App.TButton").grid(row=4, columnspan=2, padx=10, pady=10, sticky="ew")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin":
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def show_main_menu(self):
        self.frame.destroy()
        self.frame = ttk.Frame(self.master)
        self.frame.pack()

        ttk.Label(self.frame, text="Main Menu", font=('Helvetica', 20, 'bold'), style="App.TLabel").grid(row=0, columnspan=2, padx=10, pady=10)

        ttk.Button(self.frame, text="Input New Offender", command=self.input_offender_screen, style="App.TButton").grid(row=1, columnspan=2, padx=10, pady=5, sticky="ew")
        ttk.Button(self.frame, text="Offenders List", command=self.offenders_list_screen, style="App.TButton").grid(row=2, columnspan=2, padx=10, pady=5, sticky="ew")
        ttk.Button(self.frame, text="Search Offender", command=self.search_offender_screen, style="App.TButton").grid(row=3, columnspan=2, padx=10, pady=5, sticky="ew")
        ttk.Button(self.frame, text="Edit Offender", command=self.edit_offender_screen, style="App.TButton").grid(row=4, columnspan=2, padx=10, pady=5, sticky="ew")
        ttk.Button(self.frame, text="Logout", command=self.logout, style="App.TButton").grid(row=5, columnspan=2, padx=10, pady=10, sticky="ew")

    def input_offender_screen(self):
        self.frame.destroy()
        self.frame = ttk.Frame(self.master)
        self.frame.pack()

        ttk.Label(self.frame, text="Input New Offender", font=('Helvetica', 20, 'bold'), style="App.TLabel").grid(row=0, columnspan=2, padx=10, pady=10)

        ttk.Label(self.frame, text="Offender ID:", style="App.TLabel").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.offender_id_entry = ttk.Entry(self.frame)
        self.offender_id_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.frame, text="Name:", style="App.TLabel").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.frame, text="Violation Type:", style="App.TLabel").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.violation_entry = ttk.Entry(self.frame)
        self.violation_entry.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(self.frame, text="Date of Offense:", style="App.TLabel").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.date_entry = ttk.Entry(self.frame)
        self.date_entry.grid(row=4, column=1, padx=10, pady=5)

        ttk.Label(self.frame, text="Recording Officer:", style="App.TLabel").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.officer_entry = ttk.Entry(self.frame)
        self.officer_entry.grid(row=5, column=1, padx=10, pady=5)

        ttk.Button(self.frame, text="Submit", command=self.submit_offender, style="App.TButton").grid(row=6, columnspan=2, padx=10, pady=10, sticky="ew")
        ttk.Button(self.frame, text="Main Menu", command=self.show_main_menu, style="App.TButton").grid(row=7, columnspan=2, padx=10, pady=10, sticky="ew")

    def submit_offender(self):
        offender_id = self.offender_id_entry.get()
        name = self.name_entry.get()
        violation_type = self.violation_entry.get()
        date_of_offense = self.date_entry.get()
        recording_officer = self.officer_entry.get()

        if offender_id and name and violation_type and date_of_offense and recording_officer:
            self.offenders.append((offender_id, name, violation_type, date_of_offense, recording_officer))
            messagebox.showinfo("Success", "Offender information submitted successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def offenders_list_screen(self):
        self.frame.destroy()
        self.frame = ttk.Frame(self.master)
        self.frame.pack()

        ttk.Label(self.frame, text="Offenders List", font=('Helvetica', 20, 'bold'), style="App.TLabel").pack(padx=10, pady=10)

        for index, offender in enumerate(self.offenders, start=1):
            ttk.Label(self.frame, text=f"{index}. Offender ID: {offender[0]}, Name: {offender[1]}, Violation Type: {offender[2]}, Date of Offense: {offender[3]}, Recording Officer: {offender[4]}", style="App.TLabel").pack()

        ttk.Button(self.frame, text="Main Menu", command=self.show_main_menu, style="App.TButton").pack(pady=10)

    def search_offender_screen(self):
        self.frame.destroy()
        self.frame = ttk.Frame(self.master)
        self.frame.pack()

        ttk.Label(self.frame, text="Search Offender", font=('Helvetica', 20, 'bold'), style="App.TLabel").pack(padx=10, pady=10)

        ttk.Label(self.frame, text="Enter Offender ID:", style="App.TLabel").pack(pady=5)
        self.offender_id_entry = ttk.Entry(self.frame)
        self.offender_id_entry.pack(pady=5)

        ttk.Button(self.frame, text="Search", command=self.search_offender, style="App.TButton").pack(pady=5)
        self.search_result_label = ttk.Label(self.frame, text="", style="App.TLabel")
        self.search_result_label.pack(pady=5)

        ttk.Button(self.frame, text="Main Menu", command=self.show_main_menu, style="App.TButton").pack(pady=10)

    def search_offender(self):
        offender_id = self.offender_id_entry.get()
        for offender in self.offenders:
            if offender[0] == offender_id:
                self.search_result_label.config(text=f"Offender ID: {offender[0]}, Name: {offender[1]}, Violation Type: {offender[2]}, Date of Offense: {offender[3]}, Recording Officer: {offender[4]}", style="App.TLabel")
                return
        self.search_result_label.config(text="Offender not found", style="App.TLabel")

    def edit_offender_screen(self):
        self.frame.destroy()
        self.frame = ttk.Frame(self.master)
        self.frame.pack()

        ttk.Label(self.frame, text="Edit Offender", font=('Helvetica', 20, 'bold'), style="App.TLabel").pack(padx=10, pady=10)

        ttk.Label(self.frame, text="Select Offender ID to Edit:", style="App.TLabel").pack(pady=5)

        self.offender_id_to_edit = ttk.Combobox(self.frame, values=[offender[0] for offender in self.offenders])
        self.offender_id_to_edit.pack(pady=5)

        ttk.Label(self.frame, text="New Name:", style="App.TLabel").pack(pady=5)
        self.new_name_entry = ttk.Entry(self.frame)
        self.new_name_entry.pack(pady=5)

        ttk.Label(self.frame, text="New Violation Type:", style="App.TLabel").pack(pady=5)
        self.new_violation_entry = ttk.Entry(self.frame)
        self.new_violation_entry.pack(pady=5)

        ttk.Label(self.frame, text="New Date of Offense:", style="App.TLabel").pack(pady=5)
        self.new_date_entry = ttk.Entry(self.frame)
        self.new_date_entry.pack(pady=5)

        ttk.Label(self.frame, text="New Recording Officer:", style="App.TLabel").pack(pady=5)
        self.new_officer_entry = ttk.Entry(self.frame)
        self.new_officer_entry.pack(pady=5)

        ttk.Button(self.frame, text="Save Changes", command=self.save_changes, style="App.TButton").pack(pady=10)
        ttk.Button(self.frame, text="Main Menu", command=self.show_main_menu, style="App.TButton").pack(pady=10)

    def save_changes(self):
        selected_offender_id = self.offender_id_to_edit.get()
        new_name = self.new_name_entry.get()
        new_violation_type = self.new_violation_entry.get()
        new_date_of_offense = self.new_date_entry.get()
        new_recording_officer = self.new_officer_entry.get()

        for i, offender in enumerate(self.offenders):
            if offender[0] == selected_offender_id:
                self.offenders[i] = (selected_offender_id, new_name, new_violation_type, new_date_of_offense, new_recording_officer)
                messagebox.showinfo("Success", "Changes saved successfully!")
                return
        messagebox.showerror("Error", "Selected offender ID not found")

    def logout(self):
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.show_login()

def main():
    root = tk.Tk()
    app = TrafficApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
