import splunklib.client as client
import splunklib.results as results
from splunklib.binding import AuthenticationError
import json
import time

splunk_config = {'host': "localhost",  # Configuration details
                 'port': 8089,
                 'username': "darayner",
                 'password': "D@man2177"}


class SplunkManager:

    def __init__(self):
        self.connect()

    def connect(self):
        global splunk_config

        try:
            self.service = client.connect(Host=splunk_config['host'],  # Create service instance to use
                                          port=splunk_config['port'],
                                          username=splunk_config['username'],
                                          password=splunk_config['password'])
        except AuthenticationError:
            print("Authentication Error!")

    def create_index(self, index_name: str):
        indexes = self.service.indexes

        if index_name.lower() not in indexes:
            self.service.indexes.create(index_name.lower())
        else:
            print("Index already exists!")

    def add_file(self, file_path: str, index_name: str):
        indexes = self.service.indexes
        # TODO exception handling

        if index_name.lower() in indexes:
            index = self.service.indexes[index_name.lower()]
            index.upload(file_path)
        else:
            print("No such Index exists!")

    def search(self, query: str) -> dict:
        entries = []
        jobs = self.service.jobs

        search_kwargs_params = {
            "exec_mode": "blocking"
        }
        job = jobs.create(query, **search_kwargs_params)

        for result in results.ResultsReader(job.results()):
            js = json.loads(json.dumps(result))
            entries.append(js)

        return entries

    def wipe_out_index(self, index_name: str):
        index = self.service.indexes[index_name]
        timeout = 60
        index.clean(timeout)

    def delete_index(self, index_name: str):
        self.service.delete(index_name.lower())