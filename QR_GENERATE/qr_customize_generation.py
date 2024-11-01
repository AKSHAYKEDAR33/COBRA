import qrcode             #used for generation of qr code
from PIL import Image     #used for saving qr code in the form of image.

qr=qrcode.QRCode(version=1, box_size=5, border=5)

qr.add_data("https://github.com/AKSHAYKEDAR33")

qr.make(fit=True)
img=qr.make_image(fill_color="red", back_color="black")

img.save("CUSTOMIZED ARK QRCODE.png")