import pytest
import sys
#sys.path.append('../src')
from src.piglatin import pig

class Tests:
    #Unit tests for toEnglish()
    def test_engtopig(self):
        expected = "equal "
        actual = pig.toEnglish('equal-ay')
        assert actual == expected, f"expected the test to yield equal, instead it yielded {actual}"

    
    #Unit tests for toPL()
    def test_pl(self):
        expected = "equalay "
        actual = pig.toPL(["equal"], False)
        assert actual == expected, f"expected the test to yield equalay, instead it yielded {actual}"
    
    def test_int_pl(self):
        expected = "equal-ay "
        actual = pig.toPL(["equal"], True)
        assert actual == expected, f"expected the test to yield equal-ay, instead it yielded {actual}"

    def test_phrase_pl(self):
        expected = "ellohay ymay amenay isay "
        actual = pig.toPL(["hello", "my", "name", "is"], False)
        assert actual == expected, f"expected the test to yield 'ellohay ymay amenay isay', instead it yielded {actual}"

    #Unit tests for process_input()
    
    def test_empty_input(self):
        expected = []
        actual = pig.process_input(" ", "e")
        actual2 = pig.process_input(" ", "p")
        assert actual == expected , f"(e flag) expected an empty list, instead produced {actual}"
        assert actual2 == expected, f"(p flag) expected an empty list, instead produced {actual2}"
   
    def test_punc_input(self):
        expected = ["-"]
        actual = pig.process_input(".,/,/,/,[][]][]!!!*-")
        assert actual == expected, f"expected to return only a hyphen, instead returned {actual}"

    def test_phrase_input(self):
        expected = ["hello", "my", "name", "is"]
        actual = pig.process_input("hello my name is")
        assert actual == expected

