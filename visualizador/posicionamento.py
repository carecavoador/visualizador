from PIL import Image, ImageChops

img_a = Image.open(r'C:\Users\everton.souza\python\visualizador\visualizador\azul.png')
img_b = Image.open(r'C:\Users\everton.souza\python\visualizador\visualizador\vermelho.png')

offset = (2, 6)
x, y = offset

# img_b = ImageChops.offset(img_b, x, y)
img_b = ImageChops.invert(img_b)

# img_c = ImageChops.blend(img_a, ImageChops.invert(img_b), 0.5)
img_c = ImageChops.subtract(img_a, img_b)
img_c.show()
