from messaging_client.messaging_client import MessagingClient
from test_messaging.scenario_parser import ParseScenario
from test_messaging.scenario import ScenarioData, Scenario


class App():

    def __init__(self):

        self.client = MessagingClient()
        self.command_line_values = self.client.parse_command_line()

    def get_scenario_data(self):
        scenario_data = ParseScenario.to_dictionary(
                                self.command_line_values['file'])
        return ScenarioData.create_from_dictionary(scenario_data)

    def run(self):
        scenario_data = self.get_scenario_data()
        scenario = Scenario(scenario_data, self.client)
        scenario.run()

if __name__ == '__main__':
    app = App()
    app.run()
