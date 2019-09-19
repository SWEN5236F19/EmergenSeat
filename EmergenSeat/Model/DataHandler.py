import json


class DataHandler(object):

    @staticmethod
    def export_to_json(file_name, user_profiles):
        with open(file_name, "w") as outfile:
            json.dump(user_profiles, outfile)

    @staticmethod
    def import_to_json(file_name):
        with open(file_name) as json_file:
            data = json.load(file_name)
            return data
