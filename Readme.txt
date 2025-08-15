Readme for My Simple Application Build Automation

This document provides instructions on how to build and test the application using the provided build script.

Prerequisites:
- Python 3.6 or higher installed.
- pip (Python package installer) installed.
- Git installed.

Setup:
1. Clone the repository:
   git clone https://github.com/Ambaya0224/my-simple-app.git
   cd my-simple-app

2. Install required Python packages:
   pip install pytest setuptools wheel build

Running the Build Script:

For macOS / Linux:
1. Open your terminal.
2. Navigate to the project directory:
   cd /path/to/my-simple-app
3. Make the build script executable (if not already):
   chmod +x build.sh
4. Run the script:
   ./build.sh

For Windows:
1. Open Command Prompt or PowerShell.
2. Navigate to the project directory:
   cd C:\path\to\my-simple-app
3. Run the script:
   build.bat

What the build script does:
- Cleans up any previous build artifacts.
- Runs all unit tests using pytest (expected to show 3 passing and 2 failing tests for demonstration).
- Creates a deployable Python package (.whl and .tar.gz files) in the 'dist/' directory.

After running the script, you can find the generated package files in the 'dist/' folder.
