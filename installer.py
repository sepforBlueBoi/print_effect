import subprocess
import os
import sys
import shutil

def install_tool(name, url):
    print(f"Installing {name}...")
    
    # Check if git exists
    git_cmd = shutil.which("git")
    if not git_cmd:
        print("Git not found! Please install Git or add it to PATH.")
        return
    
    if not os.path.exists(name):
        subprocess.run([git_cmd, "clone", url])
    else:
        print(f"{name} already exists, skipping clone.")
    
    if os.name == 'nt':
        subprocess.run([sys.executable, "-m", "pip", "install", "-e", "."], cwd=name)
    else:
        subprocess.run([sys.executable, "-m", "pip", "install", "-e", ".", "--break-system-packages"], cwd=name)
        
    print(f"{name} done!")

install_tool("print_effect", "https://github.com/sepforBlueBoi/print_effect")