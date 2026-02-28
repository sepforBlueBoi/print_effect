import subprocess
import os
#import sys
#import shutil

def cythoni():
    print("Setting up Cython enviroment")
    if not os.path.exists("venv"):
        subprocess.run(["python3", "-m", "venv", "venv"])
    print("venv set up, downloading needed tools...")
    
    venv = os.path.join("venv", "Scripts" if os.name == "nt" else "bin", "python3")
    
    subprocess.run([venv, "-m", "pip", "install", "cython"])
    subprocess.run([venv, "-m", "pip", "install", "setuptools"])
    
    print("Setting up setup.py...")
    setup_content = """from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("your_file.pyx")
)
"""

    with open("setup.py", "w") as f:
        f.write(setup_content)
        
    print("it has been finished. you are good to go")
    print("to compile just do 'python setup.py build_ext --inplace'")
    print("if your on linux you may need to enter the venv via source to compile.")