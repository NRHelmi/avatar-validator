import unittest

from api.AvatarValidator import AvatarValidator


class TestAvatarValidator(unittest.TestCase):
    def test_validate_size(self):
        validator = AvatarValidator("./tests/data/right_sized_avatar.png")
        self.assertTrue(validator.validate_size())


if __name__ == '__main__':
    unittest.main()
