class MenuView:

    @staticmethod
    def main_view_menu():
        print("****************", "**# Main Menu #**", "1- Players Manager", "2- Event Manager", "3- Rounds Manager",
              "4- Match Manager", "5- Reports", "0- Exit", "****************", sep="\n")

    @staticmethod
    def players_manager_menu():
        print("****************", "#Player Manager:", "1 - Add Player", "2 - List Players", "3 - Return to Main Menu",
              "0- Exiting the application.", "****************", sep="\n")

    @staticmethod
    def event_manager_menu():
        print("****************", "#Event Manager:", "1- Add New Event", "2 - List Event", "3 - Return to Main Menu",
              "****************", sep="\n")

    @staticmethod
    def rounds_manager_menu():
        pass

    @staticmethod
    def match_manager_menu():
        print("****************", "#Match Manager:", "1- Add Match", "2- Add Opponents", "3- Enter Results",
              "4 - Return to Main Menu", "****************", sep="\n")

    @staticmethod
    def reports():
        print("****************", "# Reports:", "1- List of all players in alphabetical order.",
              "2- List of all tournaments.", "3- Name and dates of a given tournament.",
              "4- List of players in the tournament in alphabetical order.",
              "5- List of all rounds in the tournament and all matches in the round.", "****************", sep="\n")

    def print_all_menus(self):
        self.main_view_menu()
        self.players_manager_menu()
        self.event_manager_menu()
        self.match_manager_menu()
        self.reports()
