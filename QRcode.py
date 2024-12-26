import qrcode  # Import the qrcode library

# Prompt the user to input the website link
website = input('Type in your link: ')

# Create a QRCode object with specified version, box size, and border
qr = qrcode.QRCode(version=1, box_size=5, border=5)

# Add the website data to the QRCode object
qr.add_data(website)

# Generate the QR code matrix
qr.make()

# Create a QR code image with specified fill and background colors
img = qr.make_image(fill_color='black', back_color='white')

# Save the generated QR code image to a file named 'personal_qr.png'
img.save('personal_qr.png')
