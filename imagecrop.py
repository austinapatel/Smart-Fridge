from PIL import Image


def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    cropped_image.show()


if __name__ == '__main__':
    image = 'image.jpg'
    crop(image, (0, 0, 230, 170), 'top_left.jpg')
    crop(image, (0, 260, 185, 480), 'bottom_left.jpg')
    crop(image, (200, 200, 350, 370), 'middle.jpg')
    crop(image, (370, 270, 640, 480), 'bottom_right.jpg')
    crop(image, (310, 100, 500, 300), 'top_right.jpg')