from PIL import Image
import qrcode
img = qrcode.make('Hello World')
img.save("test1.png")