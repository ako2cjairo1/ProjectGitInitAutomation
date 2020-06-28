import sys
import os

param = sys.argv
project_path = os.environ.get("DevPath")
lang = str(param[1])
foldername = str(param[2])
new_project_dir = f"{project_path}/{lang}/{foldername}"

try:
    if not os.path.isdir(f"{project_path}/{lang}"):
        os.mkdir(f"{project_path}/{lang}")

    print("\nCreating virtual environment...\n")
    os.chdir(f"{project_path}/{lang}")
    os.system(f"virtualenv {foldername}")
    os.chdir(new_project_dir)

    # create folder/file patter that will be ignore by git
    with open(".gitignore", "w") as ignore_file:
        ignore_file.write("Lib/*\nScripts/*\n.gitignore\n*.cfg")

    # execute git commands, just commit no push
    os.system("git init")
    os.system(
        f"echo # initial file commit for project {foldername} > README.md")
    os.system("git add README.md")
    os.system('git commit -m "Initial commit"')

    # activate the virtual environment
    print(f"\nActivating virtual environment for \"{foldername}\"...")
    os.system(".\\scripts\\activate.bat")

    print(f"\nThe new project folder:{foldername} created.")
    print(f"Local: {new_project_dir}\n")
    print("Opening the newly created project in Visual Studio Code...OK")
    os.system("code .")

except:
    print("e.g.: create <fldername> <mode: l/g>")
