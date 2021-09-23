import argparse
import os
import sys
import subprocess
from pathlib import Path


def systemSpecificPath(workingPath):
    if sys.platform in ["cygwin", "win32"]:
        return workingPath.replace("/", "\\")
    elif sys.platform in ["linux",  "darwin"]:
        return workingPath.replace("\\", "/")


def installFlask(workingDirectory):
    if sys.platform in ["cygwin", "win32"]:
        os.system('. {0} && pip -q install -q Flask'.format(systemSpecificPath(
            workingDirectory+"\\virtualenv\\Scripts\\activate")))
    elif sys.platform in ["linux",  "darwin"]:
        os.system('. {0} && pip -q install -q Flask'.format(
            systemSpecificPath(workingDirectory+"virtualenv/bin/activate")))
    print(u'\u2714', "Flask Installed!")


def installCORS(workingDirectory):
    if sys.platform in ["cygwin", "win32"]:
        os.system('. {0} && pip install -U flask-cors'.format(systemSpecificPath(
            workingDirectory+"\\virtualenv\\Scripts\\activate")))
    elif sys.platform in ["linux",  "darwin"]:
        os.system('. {0} && pip install -U flask-cors'.format(
            systemSpecificPath(workingDirectory+"virtualenv/bin/activate")))
    print(u'\u2714', "Flask Installed!")


def createProjectDirectory(workingDirectory, projectName):
    destination = workingDirectory+"/"+projectName+"/"
    if not os.path.isdir(destination):
        subprocess.run(["mkdir", destination])
        print(u'\u2714', "Working Directory Created!")
    else:
        print(u'\u2714', "Working Directory Exists!")
    return destination


def createVirtualEnvironment(workingDirectory):
    if sys.platform != "aix":
        try:
            subprocess.run(
                ["python", "-m", "venv", systemSpecificPath(workingDirectory)+"virtualenv"])
            print(u'\u2714', "Virtual Environment Created!")            
        except subprocess.CalledProcessError as e:
            print(
                "There was an error creating virtual environment. Check the error in errors.txt")
            with open(workingDirectory+"/error.txt", "w+") as err:
                err.write(e)
            print(u'\u2718', "Flinit Initialize Project Failed")
            sys.exit()
        installFlask(workingDirectory)
    else:
        print(u'\u2718', "Sysytem not supported. Flinit Initialize Project Failed")
        sys.exit()


def createREADME(location, projectName):
    Path(location+"README.md").touch()
    with open(location+"README.md", "w+") as readme:
        readme.write("# {0} is a Python-Flask Project".format(projectName))
    print(u'\u2714', "README.md Created!")


def dontCreateREADME(location, projectName):
    print(u'\u2718', "README.md not Created!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("projectName", type=str,
                        help="Name of the Project")

    parser.add_argument(
        "location", type=str, help="The Location where the Project is to be created")

    parser.add_argument("--git", "-gt", "-g", dest="shouldREADMEbeCreated", action="store_const",
                        const=createREADME, default=dontCreateREADME, help="The Location where the Project is to be created")

    parser.add_argument("--cors", "-cr", "-c", dest="shouldREADMEbeCreated", action="store_const",
                        const=createREADME, default=dontCreateREADME, help="The Location where the Project is to be created")

    parser.add_argument("--readme", "-rd", "-r", dest="shouldREADMEbeCreated", action="store_const",
                        const=createREADME, default=dontCreateREADME, help="The Location where the Project is to be created")

    args = parser.parse_args()

    workingDirectory = createProjectDirectory(args.location, args.projectName)

    args.shouldREADMEbeCreated(workingDirectory, args.projectName)

    createVirtualEnvironment(workingDirectory)
    
    print(u'\u2714', "flinit Complete!")
