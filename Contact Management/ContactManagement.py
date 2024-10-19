import csv

file_path = r"C:\Users\Naveen Kumar\OneDrive\Desktop\Python Projects\Contact Management\ContactDetails.csv"

print("\nWelcome to Contact Management system.\n")

def Add(filepath):
    
    contacts = []
    
    with open(file_path,'a',newline='') as write_file:
        write = csv.writer(write_file)
        
        while True:
            name = input("Name: ").upper()
            age = input("Age: ").upper()
            email = input("Email: ").upper()
            
            person = {"Name":name,"Age":age,"Email":email}
            write.writerow([name,age,email])
            print("Contact added sucessfully.")
            contacts.append(person)
            print("Contact Details:", contacts)
            
            add_again = input("Do you want to add more (y/n)?: ").lower()
            if add_again == "n":
                return
            elif add_again == "y":
                continue
            else:
                print("Invalid option, Try again.")

def Search(file_path):
    while True:
        search = input("Type 'Name' or 'Email' to Search or 'all' to display all contacts: ").upper()

        with open(file_path, 'r') as read_file:
            read = csv.DictReader(read_file)
            
            if search == "ALL":
                print("All Contacts:")
                for all in read:
                    print(f"Name: {all['Name']}, Age: {all['Age']}, Email: {all['Email']}")
                return

            read_file.seek(0)
            search_results = []
            for detail in read:
                if search in detail["Name"].upper() or search in detail["Email"].upper():
                    search_results.append(detail)
                    print(f"Search Results: Name: {detail['Name']}, Age: {detail['Age']}, Email: {detail['Email']}")

            if not search_results:
                print("Details not found, please enter correct details.")

        search_exit = input("Enter 'q' to exit or any key to continue: ").lower()
        if search_exit == 'q':
            return
        
        
def delete(file_path):
    while True:
        with open(file_path, "r", newline="") as infile:
            read = csv.DictReader(infile)
            rows = [row for row in read]
            
            delete_data = input("Enter the name or email to delete or 'q' to return to the main menu: ").upper()
            if delete_data == "Q":
                return
            
            filtered_contacts = []
            for row in rows:
                if row['Name'] != delete_data and row['Email'] != delete_data:
                    filtered_contacts.append(row)
                    
        with open(file_path, "w", newline="") as outfile:
            write = csv.DictWriter(outfile, fieldnames=read.fieldnames)
            write.writeheader()
            write.writerows(filtered_contacts)

        if len(rows) > len(filtered_contacts):
            print(f"Contact '{delete_data}' deleted.")
        else:
            print("No matching contact found.")

        delete_again = input("Do you want to delete another contact (y/n)? ").lower()
        if delete_again != "y":
            return
        if len(rows) < 1:
            print("There no more contacts to delete.")
            return
    
def Main():
    while True:
        user_choice = input("Enter the choice to continue. \n1.Add \n2.Search \n3.Delete \n4.Exit \nChoice: ").lower()
        if user_choice == "add" or user_choice == '1':
            Add(file_path)
            
        elif user_choice == "search" or user_choice == '2':
            Search(file_path)
        
        elif user_choice == "delete" or user_choice == '3':
            delete(file_path)
        
        elif user_choice == "exit" or user_choice == '4':
            break
        
        else:
            print("Invalid option. Please enter correct option.")
    
    
Main()