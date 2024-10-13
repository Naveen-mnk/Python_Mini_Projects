import qrcode

user_data = input("Enter the text or URL: ").strip()
file_name = input("Enter the file name: ").strip()

qr = qrcode.QRCode(box_size=10, border= 4)
qr.add_data(user_data)
image = qr.make_image(fill_color = 'red', back_color = 'white')
image.save(file_name)
print(f'QR code saved as "{file_name}" ')


