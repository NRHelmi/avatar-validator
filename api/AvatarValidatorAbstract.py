from abc import ABC, abstractmethod


class AvatarValidatorAbstract(ABC):
    @abstractmethod
    def validate_size(self):
        pass

    @abstractmethod
    def validate_transparency(self):
        pass

    @abstractmethod
    def validate_hapiness(self):
        pass
