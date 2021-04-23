from PIL import Image
im = Image.open("tmp.jpg")
im.save("tmp_compressed_0.1.jpg", quality=10)
