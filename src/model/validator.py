"""validator.py: A set of routines to determine the validity of a file.

    Attributes
    ----------
    formats: List[str]
        Set of valid timestamp format regular expressions.
    Methods
    -------
    remove_non_printable(line: str) -> str:
        Removes non-printable characters from a string.
    create_file_copy(log_file_path: str, directory_path: str) -> str:
        Creates a copy of a file into a different directory.
    cleanse_log_file(log_file_path: str):
        Cleanses a log file of invalid elements.
    cleanse_csv_file(csv_file_path: str):
        Cleanses a csv file of invalid elements.
    validate_log_file(log_file: TextIO):
        Validates a log file.
    validate_csv_file(csv_file: TextIO):
        Validates a csv file.
"""

__author__ = "Team Keikaku"
__version__ = "1.0"

import csv
import os
import re
import string
from datetime import datetime
from shutil import copyfile
from typing import TextIO

from dateutil.parser import parse

from src.model import event

formats = [r'\d{1,2}[-/](Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[-/]\d{4}[:]\d{2}[:]\d{2}[:]\d{2}',
           r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2} \d{4} \d{1,2}[:]\d{1,2}[:]\d{1,2}',
           r'\d{1,2}[:]\d{1,2}([:]\d{1,2})? \d{1,2}[-/]\d{1,2}[-/]\d{4} (AM|PM)?',
           r'\d{1,2}[-/]\d{1,2}[-/]\d{4} \d{1,2}[:]\d{1,2}([:]\d{1,2})? (AM|PM)?',
           r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2} \d{2}[:]\d{2}[:]\d{2}',
           r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2} \d{1,2}[:]\d{1,2}[:]\d{1,2} \d{4}',
           r'\d{4}[-/]\d{1,2}[-/]\d{1,2} \d{1,2}[:]\d{1,2}[:]\d{1,2}']


def remove_non_printable(line: str) -> str:
    """Removes non-printable characters from a string.

    :param line: str
        The line to remove non-printable characters from.
    :return: str
        The line with non-printable characters removed.
    """

    cleansed_line = "".join(list(filter(lambda s: s in string.printable, line)))
    return cleansed_line


def create_file_copy(log_file_path: str, directory_path: str) -> str:
    """Creates a copy of a file into a different directory.

    :param log_file_path: str
        The log file path to the file to make a copy of.
    :param directory_path: str
        The directory to place the file copy in.
    :return: str
        The copied log file path.
    """

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    file = os.path.basename(log_file_path)
    file_name = file.split(".")
    copy_log_file_path = f"/{directory_path}/{file_name[0]}.{file_name[1]}"
    print(log_file_path)
    copyfile(log_file_path, copy_log_file_path)

    return copy_log_file_path


def cleanse_log_file(log_file_path: str):
    """Cleanses a log file of invalid elements.
    
    :param log_file_path: str
        The log file path to the file to cleanse.
    """

    if os.path.isfile(log_file_path) and os.path.getsize(log_file_path) > 0:
        try:
            with open(log_file_path) as in_file, open(log_file_path, 'r+') as out_file:
                for line in in_file:
                    if line.strip():
                        clean_line = remove_non_printable(line)
                        out_file.writelines(clean_line)
                out_file.truncate()
        except IOError as e:
            print(e)
    else:
        print("file is empty or does not exist", log_file_path)


def cleanse_csv_file(csv_file_path: str):
    """Cleanses a csv file of invalid elements.

    :param csv_file_path: str
        The csv file path to the file to cleanse.
    """

    if os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0:
        with open(csv_file_path) as in_file, open(csv_file_path, 'r+') as out_file:
            writer = csv.writer(out_file)
            for row in csv.reader(in_file):
                clean_row = " ".join(row)
                if clean_row.strip():
                    writer.writerow(row)
            out_file.truncate()
    else:
        print("file is empty or does not exist", csv_file_path)


def validate_log_file(log_file: TextIO):
    """Validates a log file.

    :param log_file: TextIO
        The log file to validate.
    """

    time_stamp_found = False
    errors = {}
    pattern = ""

    with open(log_file) as file:
        for line in file:
            for fmt in formats:
                pattern = re.compile(fmt)
                match = pattern.search(line)
                if match:
                    time_stamp_found = True
                    break
            else:
                break

    if time_stamp_found:
        with open(log_file) as file:
            line_num = 1
            for line in file:
                match = pattern.search(line)
                if match:
                    date_time = __convert_to_standard(match.group(0))
                    in_bounds = __timestamp_bounds(date_time)
                    if in_bounds:
                        errors[line_num] = in_bounds
                else:
                    errors[line_num] = "Error: Missing timestamp on this line!"
                line_num += 1
    else:
        errors[1] = "Error: Cannot recognize file's timestamps!"

    return errors


def validate_csv_file(csv_file: TextIO):
    """Validates a csv file.

    :param csv_file: TextIO
        The csv file to validate.
    """

    time_stamp_found = False
    errors = {}
    pattern = ""

    with open(csv_file) as file:
        reader = csv.reader(file, delimiter=',')
        next(reader, None)
        for row in reader:
            for fmt in formats:
                pattern = re.compile(fmt)
                match = pattern.search(" ".join(row))
                if match:
                    time_stamp_found = True
                    break
            else:
                break

    if time_stamp_found:
        with open(csv_file) as file:
            reader = csv.reader(file, delimiter=',')
            next(reader, None)
            line_num = 1
            for row in reader:
                match = pattern.search(" ".join(row))
                if match:
                    date_time = __convert_to_standard(match.group(0))
                    in_bounds = __timestamp_bounds(date_time)
                    if in_bounds:
                        errors[line_num] = in_bounds
                else:
                    errors[line_num] = "Error: Missing timestamp on this line!"
                line_num += 1
    else:
        errors[1] = "Error: Cannot recognize file's timestamps!"

    return errors


def __convert_to_standard(date_time_str: str) -> datetime:
    """Converts a datetime string into a standard datetime object.

    :param date_time_str: str
        The datetime string to convert to a standard format.
    :return: datetime
        A standard format datetime object.
    """

    date_time = None
    try:
        date_time = parse(date_time_str, fuzzy=True)
    except ValueError as e:
        print(e)

    return date_time


def __timestamp_bounds(date_time: datetime) -> str:
    """Prints a message detailing if the date_time is not within bounds.

    :param date_time: datetime
        The datetime to determine if within bounds set.
    :return: str
        A string message explaining if the date_time is not within bounds.
    """

    start_time = event.start_time
    end_time = event.end_time

    if date_time < start_time - datetime.timedelta(seconds=59, minutes=59, hours=23):
        return "Bounds Error: Timestamp is before start of event!"
    elif date_time > end_time + datetime.timedelta(seconds=59, minutes=59, hours=23):
        return "Bounds Error: Timestamp is after end of event!"

    return ""
