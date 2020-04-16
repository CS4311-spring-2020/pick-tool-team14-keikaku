"""definitions.py: A set of definitions used throughout the system."""

__author__ = "Team Keikaku"

__version__ = "0.3"

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SETTING_PATH = os.path.join(ROOT_DIR, 'src/model/settings.py')
UI_PATH = os.path.join(ROOT_DIR, 'ui/')
CACHE_PATH = os.path.join(ROOT_DIR, 'cache/')
PICK_DATA = os.path.join(ROOT_DIR, 'pickData/')
COPIED_FILES = os.path.join(PICK_DATA, 'copies/')
ICON_PATH = os.path.join(UI_PATH, 'icons/')
