import os
from Model.DataHandler import DataHandler


class Controller:

    def __init__(self):
        self.file_name = os.getcwd() + "/userprofiles.json"
        data = DataHandler.import_from_json(self.file_name)
        self.user_profiles = DataHandler.convert_json_to_profiles(data)

    def __del__(self):
        DataHandler.export_to_json(self.file_name)