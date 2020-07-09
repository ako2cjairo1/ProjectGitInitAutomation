import sys
import os
from github import Github
from helper import create_proj_folder, create_venv

param = sys.argv
lang = str(param[1])
foldername = str(param[2])
# add projects dirctory to the env vars
project_path = os.environ.get("DevPath")

# add github token to the env vars
git_login_token = os.environ.get("GitToken")
new_project_dir = create_proj_folder(project_path, lang, foldername)

try:
    create_venv(new_project_dir, project_path, lang, foldername)

    # create folder/file patter that will be ignore by git
    with open(".gitignore", "w") as ignore_file:
        ignore_file.write("Lib/*\nScripts/*\n.gitignore\n*.cfg")

    # settting up Github connection and auth
    gh = Github(git_login_token)
    user = gh.get_user()
    login = user.login
    repo = user.create_repo(foldername)

    commands = [f'echo # initial file commit for project {foldername} >> README.md',
                'git init',
                f'git remote add origin https://github.com/{login}/{foldername}.git',
                'git add README.md',
                'git commit -m "Initial commit"',
                'git push -u origin master']

    # execute each git commands
    for c in commands:
        os.system(c)

    # activate the virtual environment
    print(f"\nActivating virtual environment for \"{foldername}\"...\n")
    os.system(".\\scripts\\activate.bat")

    print(f"Remote: https://github.com/{login}/{foldername}\n")
    print("Opening the newly created project in Visual Studio Code...OK")
    os.system("code .")

except:
    print("Something went wrong. Cannot create a new project and then push to git.")
