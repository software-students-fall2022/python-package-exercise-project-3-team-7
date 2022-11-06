import pytest
from src import pig

class Tests:
    #Unit tests for toEnglish()
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

    #Unit tests for process_input()
    def test_empty_input(self):
        expected = []
        actual = pig.process_input(" ", "e")
        actual2 = pig.process_input(" ", "p")
        assert actual == expected and actual2 == expected

    def test_punc_input(self):
        expected = ["-"]
        actual = pig.process_input(".,/,/,/,[][]][]!!!*-")
        assert actual == expected

    def test_phrase_input(self):
        expected = ["hello", "my", "name", "is"]
        actual = pig.process_input("hello my name is")
        assert actual == expected