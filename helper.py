import os


def create_proj_folder(devfolder, lang, proj_name):
    proj_dir = f"{devfolder}\\{lang}\\{proj_name}"
    proj_folder = proj_name
    
    idx = 1
    while os.path.isdir(proj_dir):
        proj_folder = f"{proj_name}_{str(idx).zfill(2)}"
        proj_dir = f"{devfolder}\\{lang}\\{proj_folder}"
        idx += 1

    # creating lang folder if not existing
    if not os.path.isdir(f"{devfolder}/{lang}"):
        os.mkdir(f"{devfolder}/{lang}")

    return proj_dir

def create_venv(proj_dir, devfolder, lang, proj_folder):
    if proj_dir:
        print("\nCreating virtual environment...\n")
        os.chdir(f"{devfolder}/{lang}")
        os.system(f"virtualenv {proj_folder}")
        os.chdir(proj_dir)
        print(f"\nThe new project folder: {proj_folder} has been created.")
        print(f"Local: {proj_dir}\n")