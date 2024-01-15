import unittest

from api.AvatarValidator import AvatarValidator


class TestAvatarValidator(unittest.TestCase):
    def test_validate_size(self):
        validator = AvatarValidator("./tests/data/right_sized_avatar.png")
        self.assertTrue(validator.validate_size())
        self.assertTrue(validator.close())

        validator = AvatarValidator("./tests/data/bad_sized_avatar.png")
        self.assertFalse(validator.validate_size())
        self.assertTrue(validator.close())

    def test_validate_transparency(self):
        validator = AvatarValidator("./tests/data/right_transparency_avatar.png")
        self.assertTrue(validator.validate_transparency())
        self.assertTrue(validator.close())

        validator = AvatarValidator("./tests/data/bad_transparency_avatar.png")
        self.assertFalse(validator.validate_transparency())
        self.assertTrue(validator.close())

    def test_validate_happiness(self):
        validator = AvatarValidator("./tests/data/happy_colored_avatar.png")
        self.assertTrue(validator.validate_hapiness())
        self.assertTrue(validator.close())

        validator = AvatarValidator("./tests/data/sad_colored_avatar.png")
        self.assertFalse(validator.validate_hapiness())
        self.assertTrue(validator.close())


if __name__ == "__main__":
    unittest.main()
