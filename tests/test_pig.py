import pytest
from src import pig

class Tests:
    def test_engtopig(self):
        expected = "equal"
        actual = pig.toEnglish("equalay")
        assert actual == expected