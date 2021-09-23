import os
import argparse
import subprocess


'''
cowsay = Popen('cowsay', stdin=PIPE)
ls = Popen('ls', stdout=cowsay.stdin)
cowsay.communicate()
ls.wait()
'''


def systemSpecificPath():
    subprocess.Popen(
        ["python", "-m", "venv", "./test-test/virtualenv"], stdin=subprocess.PIPE)
    subprocess.run([".", "./test-test/virtualenv/bin/activate"], shell=True)
    subprocess.run(["pip", "install", "Flask"])


# Thsi Surprizingly works

def fucfunction():
    os.system(
        'python -m venv test-test/virtualenv && . test-test/virtualenv/bin/activate && pip install Flask')


parser = argparse.ArgumentParser()
'''
parser.add_argument("projectName", type=str,
                    help="Name of the Project")

parser.add_argument(
    "location", type=str, help="The Location where the Project is to be created")'''


parser.add_argument('--testval1', dest='feature1', action='store_true')
parser.add_argument('--testval2', dest='feature2', action='store_true')

parser.set_defaults(feature1=False, feature2=False)


args = parser.parse_args()

print(args.feature1, args.feature2)
