from message_client.option_parser import MessageClientOptionParser
from message_client.message_client import MessageClient
from message_tester.scenario_parser import ParseScenario
from message_tester.scenario import ScenarioData

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8700


class App():

    def __init__(self):

        self.parser = MessageClientOptionParser()
        self.parser.parse_options()

        self.client = MessageClient()

    def get_host(self):
        try:
            host = self.parser.host
        except AttributeError:
            host = DEFAULT_HOST
        return host

    def get_port(self):
        try:
            port = self.parser.port
        except AttributeError:
            port = DEFAULT_PORT
        return port

    def get_scenario_data(self):
        scenario_data = ParseScenario.to_dictionary(self.parser.filename)
        return ScenarioData.create_from_dictionary(scenario_data)


    def run(self, ):
        host = self.getHost()
        port = self.getPort()

        scenario = self.get_scenario_data()

        print("Connecting to '" + host + ":" + str(port) + "'...\n")
        self.client.connect(host, port)

        # run scenario

        self.client.close()


def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()
