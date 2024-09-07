import json  # Import the json to storing the contact.
import os  # Import the os to handle  the file operations.


CONTACTS_FILE = 'contacts.json'  #  contact wil be stored and saved.


def load_contacts():# Load contacts from the file.
    
    if os.path.exists(CONTACTS_FILE): #whether check the contact file and load data from the file.
        with open(CONTACTS_FILE, 'r') as file: # open the file in read mode. 
            return json.load(file)  # Load and return the contacts .
    return {}  # If the file doesn't exist, return an empty.

def save_contacts(contacts):# Save contacts to the file
    
    with open(CONTACTS_FILE, 'w') as file: # open the contacts file in write mode.
        json.dump(contacts, file, indent=4)  # Save the contactsinto the file and independently.


def add_contact(contacts):# Add a new contact.
    
    name = input("Enter contact name: ").strip() # Get the contact name from the user Remove any leading spaces from the input.
    if name in contacts:
        
        print("Contact already exists!") #print the contact already and display the message
        return  # Exit the function.
    
    phone = input("Enter phone number: ").strip() #get the all contact information
    email = input("Enter email address: ").strip()
    
    contacts[name] = {'phone': phone, 'email': email} #Store the contact's details in the contacts
    save_contacts(contacts)  # Save the updated contacts to the file
    print(f"Contact '{name}' added successfully!")  # the user that the contact was added.


def search_contact(contacts):# search for a contact by name
    # Get the contact name to search for.
    name = input("Enter the name of the contact to search: ").strip()
    if name in contacts:
        # If the contact is found, display the contact's details.
        print(f"Contact found: {name}")
        print(f"Phone: {contacts[name]['phone']}")  # Display the phone number.
        print(f"Email: {contacts[name]['email']}")  # Display the email address.
    else:
        # If the contact is not found, display a message.
        print(f"Contact '{name}' not found!")


def update_contact(contacts): #update the existing contact
    
    name = input("Enter the name of the contact to update: ").strip() # Get the contact name to update the input
    if name in contacts:
        
        print(f"Updating contact: {name}") # print the updating contact
        new_phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ").strip()# Ask the user forthe new phone number
        new_email = input(f"Enter new email address (current: {contacts[name]['email']}): ").strip()
        
        
        contacts[name]['phone'] = new_phone or contacts[name]['phone']  # Use the new phone if provided, else keep the old one.
        contacts[name]['email'] = new_email or contacts[name]['email']  # Use the new email if provided, else keep the old one.
        save_contacts(contacts)  # Save the updated contact details to the file
        print(f"Contact '{name}' updated successfully!")  # updated the contanct user
    else:
       
        print(f"Contact '{name}' not found!")# If the contact doesn't exist, display a message

def delete_contact(contacts):# Delete a contact
    # Get the contact name to delete.
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        # If the contact exists, delete it from the dictionary.
        del contacts[name]
        save_contacts(contacts)  # Save the updated contacts to the file.
        print(f"Contact '{name}' deleted successfully!")  # Notify the user.
    else:
        # If the contact doesn't exist, display a message.
        print(f"Contact '{name}' not found!")

def display_contacts(contacts):# Display all contacts
    if contacts:
        print("All Contacts:")
        
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")# check the all contacts and print their details (name, phone, and email).
    else:
        print("No contacts found!")# If no contacts exist, inform the user


def main(): # main function to run the program
    contacts = load_contacts()  # Load existing contacts from the file
    
    while True:
        # Display a menu of options to the user.
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()# Get the user's choice.
        
        # Execute the corresponding action based on the user's input.
        if choice == '1':
            add_contact(contacts)  # Call the function to add a contact.
        elif choice == '2':
            search_contact(contacts)  # Call the function to search for a contact.
        elif choice == '3':
            update_contact(contacts)  # Call the function to update a contact.
        elif choice == '4':
            delete_contact(contacts)  # Call the function to delete a contact.
        elif choice == '5':
            display_contacts(contacts)  # Call the function to display all contacts.
        elif choice == '6':
            print("Exiting the program. Goodbye!") # print the exit program
            break  # Exit the loop
        else:
            print("Invalid choice! Please select a valid option.")# print the invalid 

# The main function will be executed when the script is run directly
if __name__ == "__main__":
    main()  # Run the main function.
