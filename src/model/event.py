"""event.py: Stores the attributes of the current
adversarial assessment.

    Attributes
    ----------
    name : str
        Name of the adversarial assessment.
    description : str
        Description of the adversarial assessment.
    start_time : str
        Start time of the adversarial assessment
    end_time : str
        End time of the adversarial assessment.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

from PyQt5.QtCore import QDateTime

saved: bool = False
name: str = ''
description: str = ''
start_time: QDateTime = QDateTime()
end_time: QDateTime = QDateTime()
