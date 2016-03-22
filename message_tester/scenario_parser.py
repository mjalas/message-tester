import json


class ParseScenario(object):

    @staticmethod
    def to_dictionary(filename):
        data = {}
        with open(filename) as data_file:
            data = json.load(data_file)
        return data
