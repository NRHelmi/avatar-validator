from PIL import Image
from api.AvatarValidatorAbstract import AvatarValidatorAbstract


class AvatarValidator(AvatarValidatorAbstract):
    def __init__(self, path: str):
        self.path = path
        self.img = Image.open(self.path)

    # validate that the image size
    # is 512 * 512
    def validate_size(self):
        width, height = self.img.size
        return width == height == 512

    # validate that the non transpared
    # pixels are within a circle
    def validate_transparency(self, radius: int = 100):
        center_x = self.img.width // 2
        center_y = self.img.height // 2

        def is_pixel_in_circle(
            x: int, y: int, center_x: int, center_y: int, radius: int
        ):
            return (x - center_x) ** 2 + (y - center_y) ** 2 <= radius**2

        pixels = self.img.load()

        for x in range(self.img.width):
            for y in range(self.img.height):
                if is_pixel_in_circle(x, y, center_x, center_y, radius):
                    if pixels[x, y][3] == 0:
                        return False
        return True

    def validate_hapiness(
        self,
        red_threshold: int = 100,
        green_threshold: int = 60,
        blue_threshold: int = 30,
    ):
        pixels = list(self.img.getdata())
        # Calculate the average color
        average_color = (
            sum(pixel[0] for pixel in pixels) / len(pixels),
            sum(pixel[1] for pixel in pixels) / len(pixels),
            sum(pixel[2] for pixel in pixels) / len(pixels),
        )

        # Check if the average colors threshold
        warm_color_condition = (
            average_color[0] > red_threshold
            and average_color[1] > green_threshold
            and average_color[2] > blue_threshold
        )

        return warm_color_condition

    def close(self):
        try:
            self.img.close()
            return True
        except Exception:
            return False
