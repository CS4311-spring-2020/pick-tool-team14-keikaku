from src.model import event
from shutil import copyfile
from dateutil.parser import parse
import re
import csv
import os
import string


class Validator:

    def __init__(self):

        self.formats = [r'\d{1,2}[-/](Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[-/]\d{4}[:]\d{2}[:]\d{2}[:]\d{2}',
                        r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2} \d{4} \d{1,2}[:]\d{1,2}[:]\d{1,2}',
                        r'\d{1,2}[:]\d{1,2}([:]\d{1,2})? \d{1,2}[-/]\d{1,2}[-/]\d{4} (AM|PM)?',
                        r'\d{1,2}[-/]\d{1,2}[-/]\d{4} \d{1,2}[:]\d{1,2}([:]\d{1,2})? (AM|PM)?',
                        r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2} \d{2}[:]\d{2}[:]\d{2}',
                        r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2} \d{1,2}[:]\d{1,2}[:]\d{1,2} \d{4}',
                        r'\d{4}[-/]\d{1,2}[-/]\d{1,2} \d{1,2}[:]\d{1,2}[:]\d{1,2}']

        self.start_time = event.start_time
        self.end_time = event.end_time

    def remove_non_printable(self, line):
        cleansed_line = "".join(list(filter(lambda str: str in string.printable, line)))
        return cleansed_line

    def create_file_copy(self, log_file_path, directory_path):
        if not os.path.exists(directory_path):
            print("here")
            os.makedirs(directory_path)

        file = os.path.basename(log_file_path)
        file_name = file.split(".")
        copy_log_file_path = f"/{directory_path}/{file_name[0]}.{file_name[1]}"
        print(log_file_path)
        copyfile(log_file_path, copy_log_file_path)

        return copy_log_file_path

    def convert_to_standard(self, date_time_str):
        try:
            date_time = parse(date_time_str, fuzzy=True)
        except ValueError as e:
            print(e)

        return date_time

    def timestamp_bounds(self, date_time):
        print(date_time)
        if date_time < self.start_time:
            return "Bounds Error: Timestamp is before start of event!"
        elif date_time > self.end_time:
            return "Bounds Error: Timestamp is after end of event!"

        return ""

    def cleanse_log_file(self, log_file_path):
        if os.path.isfile(log_file_path) and os.path.getsize(log_file_path) > 0:
            try:
                with open(log_file_path) as in_file, open(log_file_path, 'r+') as out_file:
                    for line in in_file:
                        if line.strip():
                            clean_line = self.remove_non_printable(line)
                            out_file.writelines(clean_line)
                    out_file.truncate()
            except IOError as e:
                print(e)
        else:
            print("file is empty or does not exist", log_file_path)

    def cleanse_csv_file(self, log_file_path):
        if os.path.isfile(log_file_path) and os.path.getsize(log_file_path) > 0:
            with open(log_file_path) as in_file, open(log_file_path, 'r+') as out_file:
                writer = csv.writer(out_file)
                for row in csv.reader(in_file):
                    clean_row = " ".join(row)
                    if clean_row.strip():
                        writer.writerow(row)
                out_file.truncate()
        else:
            print("file is empty or does not exist", log_file_path)

    def validate_log_file(self, log_file):
        time_stamp_found = False
        errors = {}
        pattern = ""

        with open(log_file) as file:
            for line in file:
                if time_stamp_found:
                    break
                for format in self.formats:
                    pattern = re.compile(format)
                    match = pattern.search(line)
                    if match:
                        time_stamp_found = True
                        break

        if time_stamp_found:
            with open(log_file) as file:
                line_num = 1
                for line in file:
                    match = pattern.search(line)
                    if match:
                        date_time = self.convert_to_standard(match.group(0))
                        in_bounds = self.timestamp_bounds(date_time)
                        if in_bounds:
                            errors[line_num] = in_bounds
                    else:
                        errors[line_num] = "Error: Missing timestamp on this line!"
                    line_num += 1
        else:
            errors[1] = "Error: Cannot recognize file's timestamps!"

        return errors

    def validate_csv_file(self, csv_file):
        time_stamp_found = False
        errors = {}
        pattern = ""

        with open(csv_file) as file:
            reader = csv.reader(file, delimiter=',')
            next(reader, None)
            for row in reader:
                if time_stamp_found:
                    break
                for format in self.formats:
                    pattern = re.compile(format)
                    match = pattern.search(" ".join(row))
                    if match:
                        time_stamp_found = True
                        break

        if time_stamp_found:
            with open(csv_file) as file:
                reader = csv.reader(file, delimiter=',')
                next(reader, None)
                line_num = 1
                for row in reader:
                    match = pattern.search(" ".join(row))
                    if match:
                        date_time = self.convert_to_standard(match.group(0))
                        in_bounds = self.timestamp_bounds(date_time)
                        if in_bounds:
                            errors[line_num] = in_bounds
                    else:
                        errors[line_num] = "Error: Missing timestamp on this line!"
                    line_num += 1
        else:
            errors[1] = "Error: Cannot recognize file's timestamps!"

        return errors
