# TASK:-Contact Book

# Contact Information: Store name, phone number, email, and address for each contact.

# Add Contact: Allow users to add new contacts with their details.
# View Contact List: Display a list of all saved contacts with names and phone numbers.
# Search Contact: Implement a search function to find contacts by name or phone number.
# Update Contact: Enable users to update contact details.
# Delete Contact: Provide an option to delete a contact.
# User Interface: Design a user-friendly interface for easy interaction.

'CODE:-'


import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")
        self.contacts = {}
        tk.Label(master, text="Name:").grid(row=0, column=0, sticky=tk.E)
        tk.Label(master, text="Phone:").grid(row=1, column=0, sticky=tk.E)
        tk.Label(master, text="Email:").grid(row=2, column=0, sticky=tk.E)
        tk.Label(master, text="Address:").grid(row=3, column=0, sticky=tk.E)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=1, column=1)
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1)
        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=3, column=1)
        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=5)
        self.view_button = tk.Button(master, text="View Contact List", command=self.view_contact_list)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=5)
        self.search_button = tk.Button(master, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=5)
        self.update_button = tk.Button(master, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=5)
        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name.strip() == "":
            messagebox.showerror("Error", "Name cannot be empty.")
            return

        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Success", "Contact added successfully!")
        self.clear_entries()

    def view_contact_list(self):
        if not self.contacts:
            messagebox.showinfo("Info", "Contact list is empty.")
            return

        contact_list = "Contact List:\n"
        for name, details in self.contacts.items():
            contact_list += f"Name: {name}, Phone: {details['phone']}\n"
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        name = self.name_entry.get()
        if name.strip() == "":
            messagebox.showerror("Error", "Name cannot be empty.")
            return

        if name in self.contacts:
            details = self.contacts[name]
            messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
        else:
            messagebox.showinfo("Contact Not Found", "Contact not found.")

    def update_contact(self):
        name = self.name_entry.get()
        if name.strip() == "":
            messagebox.showerror("Error", "Name cannot be empty.")
            return

        if name in self.contacts:
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showinfo("Contact Not Found", "Contact not found.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name.strip() == "":
            messagebox.showerror("Error", "Name cannot be empty.")
            return

        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showinfo("Contact Not Found", "Contact not found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
