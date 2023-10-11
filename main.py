# Import the MainController class from the main_controller module
from controllers.main_controller import MainController


# Define the main function
def main():
    # Create an instance of the MainController class
    main_controller = MainController()

    # Run the main controller
    main_controller.run()


# Check if this script is the main entry point
if __name__ == "__main__":
    # Call the main function to start the program
    main()
