import qrcode

data = "https://www.youtube.com/@bachalkhokhar994"

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

img.save("A:\AI Course Material\Quarter-3\Class Work\Assignment_Projects\Project_4_Assignments\Assignments_01\QR code en-de-coder Python Project\qrcode.png")