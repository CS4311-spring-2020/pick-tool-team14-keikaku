
class EnforcementActionReport:

    def __init__(self):
        self.errors_dictionary = {}

    def add_error(self, line_num, error):
        self.errors_dictionary[line_num] = error

    def set_ear(self, errors):
        self.errors_dictionary = errors

    def get_ear(self):
        return self.errors_dictionary