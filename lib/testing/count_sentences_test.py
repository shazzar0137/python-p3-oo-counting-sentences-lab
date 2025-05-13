import re

class MyString:
    def __init__(self, value=""):
        self.value = value  # Use setter for validation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")  # Matches test expectation
            return
        self._value = new_value  # Correctly assign value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        sentences = re.split(r'[.!?]+', self.value.strip())
        return len([s for s in sentences if s.strip()])  