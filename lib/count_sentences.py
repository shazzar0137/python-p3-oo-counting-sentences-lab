#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value  # Use the setter for validation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            raise TypeError("The value must be a string.")
        self._value = new_value  

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        import re
        sentences = re.split(r'[.!?]+', self.value.strip())
        return len([s for s in sentences if s.strip()])  # Ensuring empty splits are ignored

# Test case
string_instance = MyString("My name is Joseph.")  # Should not raise an error
print(string_instance.is_sentence())  # Expected output: True
print(string_instance.count_sentences())  # Expected output: 1
