import requests as rq
import os


def internet_on():
    try:
        response = rq.get("https://www.google.com/")
        if response.reason == "OK":
            return True

        return False

    except Exception:
        return False


if __name__ == "__main__":
    lang = input("Language Type (Python, Swift, etc.): ")
    folder = input("Project folder name: ")
    input_mode = input("Create a repository in GitHub? (y/n): ")

    mode = "l"  # create project folder locally, no Github repository
    if (not internet_on()) and input_mode.lower() == "y":
        print(
            "\n**No internet connection.\n**Creating the project locally on your machine.\n")
    elif internet_on() and input_mode.lower() == "y":
        mode = "g"  # "g" to create a github repository

    os.system(f"create.bat {lang} {folder} {mode}")
