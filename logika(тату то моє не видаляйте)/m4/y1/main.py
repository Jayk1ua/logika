from PIL import Image, ImageFilter

with Image.open('m4/y1/ss.jpg') as original:
    grey = original.convert('L')
    grey.save('grey.jpg')


    left = original.transpose(Image.ROTATE_90)
    right = original.transpose(Image.ROTATE_270)

    left.save('m4/y1/left.jpg')
    right.save('right.jpg')