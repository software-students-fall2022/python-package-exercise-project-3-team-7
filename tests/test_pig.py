import pytest
from src import pig

class Tests:
    def test_engtopig(self):
        expected = "equal "
        actual = pig.toEnglish(['equalay'])
        assert actual == expected

    
    #Unit tests for toPL()
    
    def test_pl(self):
        expected = "equalay "
        actual = pig.toPL(["equal"], False)
        assert actual == expected
    
    def test_int_pl(self):
        expected = "equal-ay "
        actual = pig.toPL(["equal"], True)
        assert actual == expected

    def test_phrase_pl(self):
        expected = "ellohay ymay amenay isay "
        actual = pig.toPL(["hello", "my", "name", "is"], False)
        assert actual == expected