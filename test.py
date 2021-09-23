import os
import sys
import subprocess


'''
cowsay = Popen('cowsay', stdin=PIPE)
ls = Popen('ls', stdout=cowsay.stdin)
cowsay.communicate()
ls.wait()
'''

def systemSpecificPath():
    subprocess.Popen(["python", "-m", "venv", "./test-test/virtualenv"], stdin=subprocess.PIPE)
    subprocess.run([".", "./test-test/virtualenv/bin/activate"], shell=True)
    subprocess.run(["pip", "install", "Flask"])


# Thsi Surprizingly works

def fucfunction():
    os.system('python -m venv test-test/virtualenv && . test-test/virtualenv/bin/activate && pip install Flask')

fucfunction()

