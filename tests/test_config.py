import pytest


class NotInRange(Exception):
    def __init__(self, msg = 'data is not in range'):
        self.msg = msg
        super().__init__(self.msg)


def test_generic():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(15,20):
            raise NotInRange

