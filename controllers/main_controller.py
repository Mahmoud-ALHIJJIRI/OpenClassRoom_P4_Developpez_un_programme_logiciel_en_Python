from views.main_view import MenuView
from controllers.player_controller import PlayerController
from controllers.event_controller import EventController
from controllers.reports_controller import ReportController


class MainController:
    def __init__(self):
        self.running = True
        self.menu_view = MenuView()
        self.player_controller = PlayerController()
        self.event_controller = EventController()
        self.report_controller = ReportController()

    def run(self):
        while self.running:
            self.menu_view.main_view_menu()
            choice = input("Enter your choice: ")
            self.handle_choice(choice)

    def handle_choice(self, choice):
        if choice == "1":
            self.menu_view.players_manager_menu()
            player_choice = input("Enter your choice: ")
            self.player_controller.handle_player_menu(player_choice)
        elif choice == "2":
            self.menu_view.event_manager_menu()
            event_choice = input("Enter your choice: ")
            self.event_controller.handle_event_menu(event_choice)
        elif choice == "3":
            self.menu_view.reports()
            report_choice = input("Enter your choice: ")
            self.report_controller.handle_report_menu(report_choice)

        elif choice == "0":
            self.running = False
            print("Exiting the application.")
        else:
            print("Invalid choice. Please select a valid option.")
