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
        
    print("writing compile script...")
        
    compile_script = """python setup.py built_ext --inplace"""

    with open("compile.sh", "w") as f:
        f.write(compile_script)
        
    print("It has been finished. you are good to go")
    print("To compile chmod the compile script, and run in the venv via the source command.")
    print("If you're on windows you will probably need to use the python script diractly")