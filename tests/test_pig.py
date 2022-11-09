import pytest
import sys
#sys.path.append('../src')
#from piglatin import pig
from src.piglatinTeam7 import pig
class Tests:
    #Unit tests for toEnglish()
    def test_engtopig(self):
        expected = "equal "
        actual = pig.toEnglish('equal-ay')
        assert actual == expected, f"expected the test to yield equal, instead it yielded {actual}"

    def test_phrase_eng(self):
        expected = "hello my name is "
        actual = pig.toEnglish("ello-hay y-may ame-nay is-ay ")
        assert actual == expected, f"expected the test to yield equal, instead it yielded {actual}"

    def test_consonant_eng(self):
        expected = "characteristic "
        actual = pig.toEnglish('aracteristic-chay')
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

    # unit tests for speech bubble

    def test_speech_bubble_type_empty(self): # checking return type when an empty string is passed
        actual = pig.speech_bubble("")
        assert type(actual) is str

    def test_speech_bubble_type_text(self): # checking return type when a populated string is passed
        actual = pig.speech_bubble("Hello, my name is Foo. I am a great person.")
        assert type(actual) is str

    def test_speech_bubble_empty(self): # testing output with empty string
        expected = "\n \n()\n "
        actual = pig.speech_bubble("")

        assert actual == expected

    def test_speech_bubble_text(self): # testing output with populated multiline string
        expected = "\n ---------------------------\n(Hello, my name is Foo. I am)\n(a great person.            )\n ---------------------------"
        actual = pig.speech_bubble("Hello, my name is Foo. I am a great person.")

        assert actual == expected

    def test_speech_bubble_one_line(self): # testing output with populated single line string
        expected = "\n ----------------------\n(Hello, my name is Foo.)\n ----------------------"
        actual = pig.speech_bubble("Hello, my name is Foo.")

        assert actual == expected

    # unit tests for arrow_to_bubble

    def test_arrow_to_bubble_type(self): # testing type of return for arrow_to_bubble
        actual = pig.arrow_to_bubble()
        assert type(actual) is str

    def test_arrow_to_bubble_length(self): # testing length of string returned for arrow_to_bubble
        actual = pig.arrow_to_bubble()
        assert len(actual) == 18

    def test_arrow_to_bubble(self): # testing arrow_to_bubble
        expected = "       \\\n        \\"
        actual = pig.arrow_to_bubble()

        assert actual == expected

    # unit tests for print_pig

    def test_print_pig_type(self): # testing type of return for print_pig
        actual = pig.print_pig()
        assert type(actual) is str

    def test_print_pig_length(self): # testing length of string returned for print_pig
        actual = pig.print_pig()
        assert len(actual) == 141

    def test_print_pig(self): # testing print_pig
        expected = "         <`--'\>______" + "\n" + "         /. .  `'     \\" + "\n" + "        (`')  ,        @" + "\n" + "         `-._,        /" + "\n" + "            )-)_/--( >" + "\n" + "           ''''  ''''" + "\n"
        actual = pig.print_pig()

        assert actual == expected

    # unit tests for print_everythin

    def test_print_everything_type(self): # testing type for print_everything function
        actual = pig.print_everything("Hello, my name is Foo.")

        assert type(actual) is str

    # testing print_everything function
    def test_print_everything_empty(self):
        expected = "\n \n()\n " + "\n" + "       \\\n        \\" + "\n" + "         <`--'\>______" + "\n" + "         /. .  `'     \\" + "\n" + "        (`')  ,        @" + "\n" + "         `-._,        /" + "\n" + "            )-)_/--( >" + "\n" + "           ''''  ''''" + "\n"
        actual = pig.print_everything("")

        assert actual == expected

    def test_print_everything_one_line(self):
        expected = "\n ----------------------\n(Hello, my name is Foo.)\n ----------------------" + "\n" + "       \\\n        \\" + "\n" + "         <`--'\>______" + "\n" + "         /. .  `'     \\" + "\n" + "        (`')  ,        @" + "\n" + "         `-._,        /" + "\n" + "            )-)_/--( >" + "\n" + "           ''''  ''''" + "\n"
        actual = pig.print_everything("Hello, my name is Foo.")

        assert actual == expected

    def test_print_everything_text(self):
        expected = "\n ---------------------------\n(Hello, my name is Foo. I am)\n(a great person.            )\n ---------------------------" + "\n" + "       \\\n        \\" + "\n" + "         <`--'\>______" + "\n" + "         /. .  `'     \\" + "\n" + "        (`')  ,        @" + "\n" + "         `-._,        /" + "\n" + "            )-)_/--( >" + "\n" + "           ''''  ''''" + "\n"
        actual = pig.print_everything("Hello, my name is Foo. I am a great person.")

        assert actual == expected
