import os
from Model import DataHandler


class Controller:

    def __init__(self):
        self.file_name = os.getcwd() + "/userprofiles.json"
        DataHandler.import_to_json(self.file_name)

    def __del__(self):
        DataHandler.export_to_json(self.file_name)