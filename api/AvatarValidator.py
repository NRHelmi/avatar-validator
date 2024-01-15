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
    def validate_transparency(self):
        center_x = self.img.width // 2
        center_y = self.img.height // 2
        radius = 100  # 1 < radius < 256

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

    def validate_hapiness(self):
        return super().validate_hapiness()

    def close(self):
        try:
            self.img.close()
            return True
        except Exception:
            return False
