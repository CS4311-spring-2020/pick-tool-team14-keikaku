"""settings.py: Handles the settings of the system windows.

    Attributes
    ----------
    lead_status: bool
        True if lead, false otherwise.
    tab_index: int
        Signifies the current tab index to display.
    hostname: str
        Host name of the current system.
    host_ip_address: str
        IP address of the local host.
    target_ip_address: str
        IP address of the target system to connect to.
    red_team_folder: str
        Folder name for red team log files.
    blue_team_folder: str
        Folder name for blue team log files.
    white_team_folder: str
        Folder name for white team log files.
    Methods
    -------
    toggle_lead()
        Toggle the lead_status.
    save():
        Saves this settings instance to a file __filename.
    load() -> Settings
        Reads a settings instance from a file __filename.
"""

__author__ = "Team Keikaku"

__version__ = "0.5"

import socket

from src.util import file_util

__filename: str = "settings.pk"

lead_status: bool = False
tab_index: int = 0
try:
    hostname: str = socket.gethostname()
    host_ip_address: str = socket.gethostbyname(hostname)
except:
    host_ip_address: str = '127.0.0.1'
target_ip_address: str = '127.0.0.1'
red_team_folder: str = 'RedTeam'
blue_team_folder: str = 'BlueTeam'
white_team_folder: str = 'WhiteTeam'


def toggle_lead():
    """Toggle the lead_status."""

    global lead_status
    lead_status = not lead_status


def save():
    """Saves this settings instance to a file "settings"."""

    print('Saving settings...')
    file_util.save_object([lead_status, tab_index, hostname, host_ip_address, target_ip_address,
                           red_team_folder, blue_team_folder, white_team_folder], __filename)


def load():
    """Reads a settings instance from a file "settings"."""

    if file_util.check_file(__filename):
        print('Loading settings...')
        global lead_status, tab_index, hostname, host_ip_address, target_ip_address, \
            red_team_folder, blue_team_folder, white_team_folder
        (lead_status, tab_index, hostname, host_ip_address, target_ip_address,
         red_team_folder, blue_team_folder, white_team_folder) = file_util.read_file(__filename)
