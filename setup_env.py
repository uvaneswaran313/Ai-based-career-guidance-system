import os
import sys
import urllib.request
import zipfile
import subprocess
import shutil

WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
NODE_ZIP_URL = "https://nodejs.org/dist/v20.11.0/node-v20.11.0-win-x64.zip"
NODE_ZIP_PATH = os.path.join(WORKSPACE_DIR, "node.zip")
NODE_ENV_DIR = os.path.join(WORKSPACE_DIR, "node-env")
VENV_DIR = os.path.join(WORKSPACE_DIR, ".venv")

def log(msg):
    print(f"[*] {msg}")
    sys.stdout.flush()

def download_node():
    if os.path.exists(os.path.join(NODE_ENV_DIR, "node.exe")):
        log("Portable Node.js already exists. Skipping download.")
        return

    if os.path.exists(NODE_ZIP_PATH):
        log("Portable Node.js zip already exists locally. Skipping download.")
    else:
        log(f"Downloading Node.js portable from {NODE_ZIP_URL}...")
        try:
            urllib.request.urlretrieve(NODE_ZIP_URL, NODE_ZIP_PATH)
        except Exception as e:
            log(f"Error downloading Node.js: {e}")
            sys.exit(1)

    try:
        log("Extracting Node.js zip...")
        # Extract to workspace
        temp_extract_dir = os.path.join(WORKSPACE_DIR, "node_temp_extract")
        os.makedirs(temp_extract_dir, exist_ok=True)
        
        with zipfile.ZipFile(NODE_ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall(temp_extract_dir)
            
        nested_dir = os.path.join(temp_extract_dir, "node-v20.11.0-win-x64")
        if os.path.exists(NODE_ENV_DIR):
            shutil.rmtree(NODE_ENV_DIR)
            
        shutil.move(nested_dir, NODE_ENV_DIR)
        shutil.rmtree(temp_extract_dir)
        os.remove(NODE_ZIP_PATH)
        log(f"Portable Node.js successfully set up in {NODE_ENV_DIR}")
    except Exception as e:
        log(f"Error setting up Node.js: {e}")
        sys.exit(1)

def setup_venv():
    log("Setting up Python virtual environment...")
    try:
        if not os.path.exists(VENV_DIR):
            subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
            log("Virtual environment created.")
        else:
            log("Virtual environment already exists.")
            
        # Determine paths
        pip_path = os.path.join(VENV_DIR, "Scripts", "pip.exe")
        requirements_path = os.path.join(WORKSPACE_DIR, "requirements.txt")
        
        log("Installing Python dependencies from requirements.txt...")
        # Skip upgrading pip to avoid Windows permissions locks, install dependencies directly
        subprocess.run([pip_path, "install", "-r", requirements_path], check=True)
        log("Python dependencies installed successfully.")
    except Exception as e:
        log(f"Error setting up virtual environment: {e}")
        sys.exit(1)

if __name__ == "__main__":
    download_node()
    setup_venv()
    log("Environment setup successfully completed!")
