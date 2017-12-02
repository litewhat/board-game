"""
Models
"""


class BaseModel:
    def __init__(self, *args, **kwargs):
        super().__init__()
        for attr, value in zip(self.attributes, args):
            setattr(self, attr, value)

        for attr, value in kwargs.items():
            if not getattr(self, attr, None):
                setattr(self, attr, value)
