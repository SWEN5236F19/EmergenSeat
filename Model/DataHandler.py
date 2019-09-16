import json


class DataHandler(object):

    @staticmethod
    def export_to_json(self, file_name, user_profiles):
        with open(file_name, 'w') as outfile:
            json.dump(user_profiles, outfile)

    @staticmethod
    def import_to_json(self, file_name):
        with open(file_name) as json_file:
            data = json.load(file_name, json_file)
            return data
