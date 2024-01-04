import qrcode
from PIL import Image
# Create a QRCode object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
# Add data to the QRCode object
qr.add_data('https://www.google.com')
# Make the QRCode image
qr.make(fit=True)
# Convert the QRCode image to a PIL Image object
qr_image = qr.make_image(fill_color="black", back_color="white")
# Display the QR code image
qr_image.show()
# Optionally, you can save the QR code image
qr_image.save('qrcode.png')