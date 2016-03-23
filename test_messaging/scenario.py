import json


class Message(object):

    def __init__(self, name, content):
        self.name = name
        self.content = content


class ScenarioData(object):

    def __init__(self, name, messages, message_order, host=None, port=None):
        self.name = name
        self.messages = messages
        self.message_rder = message_order
        self.host = host
        self.port = port

    def set_remote_address(self, host, port):
        """Set host and port attributes"""
        self.host = host
        self.port = port

    @staticmethod
    def create_from_dictionary(data):
        messages = ScenarioData.collect_messages(data)
        message_order = data['messageOrder']
        if data['host'] and data['port']:
            return ScenarioData(data['name'], messages, message_order,
                                host=data['host'], port=data['port'])
        else:
            return ScenarioData(data['name'], messages, message_order)

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

    def __init__(self, scenario_data, messaging_client):
        self.scenario_data = scenario_data
        self.client = messaging_client

    def run(self):
        host = self.scenario_data.host
        port = self.scenario_data.port
        print(port)
        print("Connecting to '" + host + ":" + str(port) + "'...\n")
        self.client.connect(host, port)
        self.client.send_message("Hello world!")
        response = self.client.receive_response()
        print(response)
        self.client.close()
