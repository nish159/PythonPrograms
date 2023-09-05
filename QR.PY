# PIP3 INSTALL QRCODE - INSTALLS QRCODE LIBRARY
# PIP3 INSTALL PILLOW - USED FOR IMAGE HANDLING
import qrcode

# INPUT TEXT OR URL
data = "https://www.example.com"

# CREATE QR CODE INSTANCE
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# ADD DATA TO QR CODE
qr.add_data(data)
qr.make(fit=True)

# CREATE AN IMAGE OBJECT FROM THE QR CODE INSTANCE
img = qr.make_image(fill_color="black", back_color="white")

# SAVE THE QR CODE AS AN IMAGE FILE
img.save("qr_code.png")

print("QR code saved as qr_code.png")
