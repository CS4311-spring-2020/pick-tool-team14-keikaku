"""splunk.py: Managing routines for Splunk.
"""

__author__ = "Team Keikaku"
__version__ = "0.8"

import json
from typing import List

import splunklib.client as client
import splunklib.results as results
from splunklib.binding import AuthenticationError


class SplunkManager:
    """A collection of managing routines for Splunk."""

    def __init__(self):
        self.service = None

    def connect(self, host, port, username, password=""):
        """Establishes a connection to Splunk."""

        error = ""
        try: # Create service instance to use
            self.service = client.connect(Host=host, port=port, username=username, password=password)
        except Exception as e:
            error = str(e)
        print(self.service)

        return error

    def create_index(self, index_name: str):
        """Creates a new index in Splunk.

        :param index_name: str
            The name of the index to create.
        """

        indexes = self.service.indexes

        if index_name.lower() not in indexes:
            self.service.indexes.create(index_name.lower())
        else:
            print("Index already exists!")

    def add_file(self, file_path: str, index_name: str):
        """Adds a file int a Splunk index.

        :param file_path: str
            The file path to the file to upload to Splunk.
        :param index_name: str
            The name of the index.
        """

        indexes = self.service.indexes
        # TODO exception handling

        if index_name.lower() in indexes:
            index = self.service.indexes[index_name.lower()]
            index.upload(file_path)
        else:
            print("No such Index exists!")

    def search(self, query: str) -> List[str]:
        """Searches Splunk with a query.

        :param query: str
            The query to give to Splunk.
        :return: List[str]
            A list of string entries found in Splunk.
        """

        print(self.service)
        entries = []
        jobs = self.service.jobs

        search_kwargs_params = {
            "exec_mode": "blocking"
        }
        job = jobs.create(query, **search_kwargs_params)

        for result in results.ResultsReader(job.results(count=0)):
            js = json.loads(json.dumps(result))
            entries.append(js)

        return entries

    def wipe_out_index(self, index_name: str):
        """Empties a Splunk index.

        :param index_name: str
             The name of the index.
        """

        index = self.service.indexes[index_name]
        timeout = 60
        index.clean(timeout)

    def delete_index(self, index_name: str):
        """Deletes a Splunk index.

        :param index_name: str
            The name of the index.
        """

        self.service.delete(index_name.lower())
