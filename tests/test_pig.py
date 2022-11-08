import pytest
import sys
sys.path.append('../src')
from piglatin import pig

class Tests:
    #Unit tests for toEnglish()
    def test_engtopig(self):
        expected = "equal "
        actual = pig.toEnglish('equal-ay')
        assert actual == expected, f"expected the test to yield equal, instead it yielded {actual}"

    #Unit tests for toPL()
    def test_pl(self):
        expected = "equalay "
        actual = pig.toPL("equal", False)
        assert actual == expected, f"expected the test to yield equalay, instead it yielded {actual}"
    
    def test_int_pl(self):
        expected = "equal-ay "
        actual = pig.toPL("equal", True)
        assert actual == expected, f"expected the test to yield equal-ay, instead it yielded {actual}"

    def test_phrase_pl(self):
        expected = "ellohay ymay amenay isay "
        actual = pig.toPL("hello my name is", False)
        assert actual == expected, f"expected the test to yield 'ellohay ymay amenay isay', instead it yielded {actual}"

    #Unit tests for process_input()
    
    def test_empty_input(self):
        expected = []
        actual = pig.process_input(" ", "e")
        actual2 = pig.process_input(" ", "p")
        assert len(actual) == len(expected), f"(e flag) expected an empty list, instead produced {actual}"
        assert len(actual2) == len(expected), f"(p flag) expected an empty list, instead produced {actual2}"
   
    def test_punc_input(self):
        expected = ["-"]
        actual = pig.process_input(".,/,/,/,[][]][]!!!*-", "e")

        correct_flag = False

        if len(actual) == 1 and actual[0] == "-":
            correct_flag = True

        assert correct_flag == True, f"expected to return only a hyphen, instead returned {actual}"

    def test_phrase_input(self):
        expected = ["hello", "my", "name", "is"]
        actual = pig.process_input("hello my name is", "p")

        correct_flag = True

        if len(expected) != len(actual):
            correct_flag = False
        else:
            for i in range(len(actual)):
                if expected[i] != actual[i]:
                    correct_flag = False

        assert correct_flag == True

    # def test_speech_bubble(self):
    #     expected = "\n()"
    #     actual = pig.speech_bubble("")

    #     assert actual == expected




