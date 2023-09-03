from views.main_view import MenuView


class MainController:
    def __init__(self):
        self.running = True
        self.menu_view = MenuView()

    def run(self):
        while self.running:
            self.menu_view.main_view_menu()
            choice = input("Enter your choice: ")
            self.handle_choice(choice)

    def handle_choice(self, choice):
        if choice == "1":
            self.menu_view.players_manager_menu()
            player_choice = input("Enter your choice: ")
        elif choice == "2":
            self.menu_view.event_manager_menu()
        elif choice == "3":
            self.menu_view.rounds_manager_menu()
        elif choice == "4":
            self.menu_view.match_manager_menu()
        elif choice == "5":
            self.menu_view.reports()
        elif choice == "0":
            self.running = False
            print("Exiting the application.")
        else:
            print("Invalid choice. Please select a valid option.")
