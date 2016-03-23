import json


class Message(object):

    def __init__(self, name, content):
        self.name = name
        self.content = content


class ScenarioData(object):

    def __init__(self, name, messages, message_order):
        self.name = name
        self.messages = messages
        self.message_rder = message_order

    @staticmethod
    def create_from_dictionary(data):
        scenario_name = data['name']
        messages = ScenarioData.collect_messages(data)
        message_order = data['messagesOrder']
        return ScenarioData(scenario_name, messages, message_order)

    @staticmethod
    def collect_messages(data):
        messages = []
        for message_data in data['messages']:
            message_name = message_data['name']
            if type(message_data['content']) is dict:
                message_content = json.dumps(message_data['content'])
            elif type(message_data['content']) is list:
                raise NotImplemented("Content of type list not implemented!")
            else:
                message_content = message_data['content']
            message = Message(message_name, message_content)
            messages.append(message)
        return messages



class Scenario(object):

    def __init__(self, scenario_data):
        self.scenario_data = scenario_data
