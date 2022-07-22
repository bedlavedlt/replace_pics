from PIL import Image
from os import walk, path

image_types = ['.jpg', '.png']

def gen_images(directory):
    for root, dirs, files in walk(directory):
        for file in files:
            extension = path.splitext(file)[-1]
            if extension in image_types:
                image_path = path.join(root, file)
                image = Image.open(image_path)
                print(image_path)
                image.show()
                yield image_path

