"""settings.py: Handles the settings of the system windows.

    Attributes
    ----------
    lead_status : int
        Signifies if lead (2) or not lead (0).

    Methods
    -------
    toggle_lead()
        Toggle the lead_status between 0 and 2.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

lead_status: int = 0


def toggle_lead():
    """Toggle the lead_status between 0 and 2."""

    global lead_status
    lead_status = lead_status ^ 2
