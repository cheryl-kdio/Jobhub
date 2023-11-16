import dotenv

from presentation.start_view import StartView

# This script is the entry point of your application


if __name__ == "__main__":
    dotenv.load_dotenv(override=True)

    # run the Start View
    current_view = StartView()

    # while current_view is not none, the application is still running
    while current_view:
        # a border between view
        with open(
            "presentation/graphical_assets/border.txt", "r", encoding="utf-8"
        ) as asset:
            print(asset.read())
        # Display the info of the view
        current_view.display_info()
        # ask user for a choice
        current_view = current_view.make_choice()

    with open("presentation/graphical_assets/bye.txt", "r", encoding="utf-8") as asset:
        print(asset.read())
