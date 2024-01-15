from PIL import Image
from api.AvatarValidatorAbstract import AvatarValidatorAbstract


class AvatarValidator(AvatarValidatorAbstract):
    def __init__(self, path: str):
        self.path = path
        self.img = Image.open(self.path)

    # validate if the image size
    # is 512 * 512
    def validate_size(self):
        width, height = self.img.size
        self.img.close()
        return width == height == 512

    def validate_transparency(self):
        return super().validate_transparency()

    def validate_hapiness(self):
        return super().validate_hapiness()
