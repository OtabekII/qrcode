import qrcode
import random
import string

def generate_qr_code(data):
    # QR code yaratish
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")

    print("QR code yaratildi: qr_code.png")

def generate_random_link():
    letters = string.ascii_letters + string.digits
    link = ''.join(random.choice(letters) for i in range(10))
    link = f"https://example.com/{link}"
    return link

def generate_random_filename():
    letters = string.ascii_letters + string.digits
    filename = ''.join(random.choice(letters) for i in range(8))+".png"
    return filename

link = generate_random_link()
filename = generate_random_filename()
generate_qr_code(link)
print(f"Yaratilgan link: {link}")
print(f"Yaratilgan fayl nomi: {filename}")