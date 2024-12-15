import qrcode
website = input('Type in your link: ')

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(website)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('personal_qr.png')