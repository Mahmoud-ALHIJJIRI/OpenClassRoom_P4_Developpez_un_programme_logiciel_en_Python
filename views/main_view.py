class MenuView:

    @staticmethod
    def main_view_menu():
        print("*********************************", "**# Main Menu #**", "1- Players Manager", "2- Events Manager",
              "3- Reports", "0- Exit", "*********************************", sep="\n")

    @staticmethod
    def players_manager_menu():
        print("*********************************", "#Player Manager:", "1 - Add a new Player", "2 - List Players",
              "9 - Return to Main Menu", "0- To Exit the application.", "*********************************", sep="\n")

    @staticmethod
    def event_manager_menu():
        print("*********************************", "#Events Manager:", "1- Add a New Event", "2- List Events",
              "3- Manage an Event", "9- Return to Main Menu",
              "0- Exiting the application.", "*********************************", sep="\n")

    @staticmethod
    def one_event_manage_menu():
        print("1. Add players to the event", "2. View registered players", "3. Add a new Round to the event",
              "4. Listing Event's Rounds", "5. Event's General Notes: ",
              "9. Return to the previous menu", "0. To Exit the application.", sep="\n")

    @staticmethod
    def rounds_manager_menu():
        print("1. Terminate Current Round and Start a new Round", "2. List registered rounds",
              "9. Return to the previous menu", "0. To Exit the application.", sep="\n")

    @staticmethod
    def match_manager_menu():
        print("****************", "#Match Manager:", "1- Add Match", "2- Add Opponents", "3- Enter Results",
              "4 - Return to Main Menu", "****************", sep="\n")

    @staticmethod
    def reports():
        print("*********************************", "# Reports:", "1- List of all players in alphabetical order.",
              "2- List of all Events.", "3- Reports from one Event.", "9- Return to main Menu",
              "0- To Exit the Application", "*********************************", sep="\n")

    @staticmethod
    def one_event_reports_menu():
        print("*********************************", "# Reports:", "1- Name and dates of this event.",
              "2- List of players registered for this Event alphabetically.",
              "3- List of all rounds in this Event.", "4- List of all the matches in this Event.",
              "9- Return to main Menu", "0- To Exit the Application",
              "*********************************", sep="\n")

    @staticmethod
    def round_options():
        print("            Choose an option:",
              "1. Terminate current Round and start next Round",
              "9. Return to the main menu to stay in this round",
              "0. To quite the application without saving the new change to Rounds", sep="\n            ")

    def print_all_menus(self):
        self.main_view_menu()
        self.players_manager_menu()
        self.event_manager_menu()
        self.match_manager_menu()
        self.reports()
