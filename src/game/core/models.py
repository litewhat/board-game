"""
Models
"""


class Model:
    attributes = 'uuid'

    def __init__(self, *args, **kwargs):
        super().__init__()
        for attr, value in zip(self.attributes, args):
            if value is not None:
                setattr(self, attr, value)

        for attr, value in kwargs.items():
            if value is None:
                raise TypeError()

            if not getattr(self, attr, None):
                setattr(self, attr, value)
