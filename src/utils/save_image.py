from PIL import Image


def image_add_origin(image, folder, book_name):
    path_image = f"{folder}/{book_name}.webp"

    image = Image.open(image.file)

    new_image = image.resize((256, 400))
    new_image.save(path_image, format="webp", quality=100, optimize=True)

    return path_image
