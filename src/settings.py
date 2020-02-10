"""settings.py: Handles the settings of the system windows.

    Attributes
    ----------
    lead_status : int
        Signifies if lead (2) or not lead (0).
    tab_index : int
        Signifies the current tab index to display.
    hostname : str
        Host name of the current system.
    host_ip_address : str
        IP address of the local host.
    target_ip_address : str
        IP address of the target system to connect to.

    Methods
    -------
    toggle_lead()
        Toggle the lead_status between 0 and 2.
"""
import socket

__author__ = "Team Keikaku"

__version__ = "0.2"

lead_status: int = 0
tab_index: int = 0
hostname: str = socket.gethostname()
host_ip_address: str = socket.gethostbyname(hostname)
target_ip_address: str = '127.0.0.1'
red_team_folder: str = 'RedTeam'
blue_team_folder: str = 'BlueTeam'
white_team_folder: str = 'WhiteTeam'


def toggle_lead():
    """Toggle the lead_status between 0 and 2."""

    global lead_status
    lead_status = lead_status ^ 2
