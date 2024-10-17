import csv
import qrcode
import datetime


print("\n**Welcome to online Bill payment Portal**\n")    

card_path = r"C:\Users\Card_Details.csv"
upi_path = r"C:\Users\UPI_Details.csv"

def Card_payment():
    
    while True:
        
        card_continue = input("you have selected for Card payment, 'y' to continue or 'q' to Main menu: ").lower()
        if card_continue == "y":
            card_num = input("Card Number: ")
            card_name = input("Card Holder Name: ").upper()
            card_cvv = input("CVV: ")

            with open(card_path,"r") as card_file:
                card_read = csv.DictReader(card_file)
                
                for row in card_read:
                    if (row["Card Number"] == card_num and row['Card Holder Name'] == card_name and
                        row['CVV'] == card_cvv):
                        print(f"Your Card details: \n Card Number- {row['Card Number']},\n Holder Name- {row['Card Holder Name']}\n")
                        
                        final_step = input(" 'y' to pay or 'q' to exit: ")
                        if final_step == 'q':
                            print("Exiting card payement")
                            return
                        else:
                            print("Amount Paid successfully.")
                            return
                else:
                    print("Invalid card number, Please enter the correct card number.")
        elif card_continue == "q":
            print("Exiting Card Payement.")
            break
        else:
            print("Invalid input, Please enter 'y' or 'q'. ")
            break


def UPI_payment():
    
    while True:
        
        upi_continue = input("you have selected for UPI payment, 'y' to continue or 'q' to Main menu: ").lower()
        if upi_continue == "y":
            upi_choice = input("1.Enter '1' for Scan QR code.\n2.Enter '2' for UPI ID.\n")
            
            if upi_choice == "1":
                
                time = datetime.datetime.now().strftime("Date: %d-%m-%Y, Time: %H:%M:%S")
                timestamp  = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
                upi_success = f"Amount paid successfully on {time}."
                file_name = f"qr_code_{timestamp}.png"
                
                qr = qrcode.QRCode(box_size=10, border= 4)
                qr.add_data(upi_success)
                image = qr.make_image(fill_color = 'black', back_color = 'white')
                image.save(file_name)
                print(f'QR code saved as "{file_name}" ')
                
            elif upi_choice == "2":
                upi_id = input("UPI ID: ").lower()
                upi_name = input("Name: ").upper()
                
                with open(upi_path,"r") as upi_file:
                    upi_read = csv.DictReader(upi_file)
                    
                    for row in upi_read:
                        if row['UPI Id'] == upi_id and row['Name'] == upi_name:
                            print(f"Your UPI Details:\n UPI ID: {row['UPI Id']},\n Name: {row['Name']} ")
                            
                            upi_final = input(" 'y' to pay and 'q' to exit: ")
                            if upi_final == 'y':
                                print("Amount paid successfully.")
                                return
                            else:
                                print("Exiting UPI Payment.")
                                return
                            
                    else:
                        print("Invalid UPI Details, Please enter correct UPI Details.")
                        return
            elif upi_continue == "q":
                print("Exiting UPI Payment.")
                return
            else:
                print("Invalid input, please enter 'y' or 'q'.")

def main():
    
    while True:
        
        payment_choice = input(
            "Welcome to the online Bill Payment Portal.\n Please Select Payment Method,\n1.Card\n2.UPI\n3.Exit\n").lower()
        
        if payment_choice == "1" or payment_choice == "card":
            Card_payment()
        elif payment_choice == "2" or payment_choice == "upi":
            UPI_payment()
        elif payment_choice == "3" or payment_choice == "exit":
            print("Exiting Bill payment.")
            break
        else:
            print("Invalid Choice, Plase select 1.Card or 2.UPI payment option to continue.")
            
main()