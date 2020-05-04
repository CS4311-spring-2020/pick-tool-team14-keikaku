"""queue.py: A collection of information representing an Enforcement Action Report.
"""

__author__ = "Team Keikaku"
__version__ = "1.0"


class EnforcementActionReport:
    """A collection of information representing an Enforcement Action Report.

        Attributes
        ----------
        errors_dictionary: dict
            A dictionary of errors.
    """

    def __init__(self):
        self.errors_dictionary = {}

    def add_error(self, line_num, error):
        self.errors_dictionary[line_num] = error

    def set_ear(self, errors):
        self.errors_dictionary = errors

    def get_ear(self):
        return self.errors_dictionary
