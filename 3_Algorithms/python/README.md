Getting started
===============

Quick steps to run the demo scripts and tests locally.

1.	Make sure Docker Desktop is running
1. Make sure you are using your Python profile with these extensions - Container Tools and Dev Containers
1. Open Container
	1. Open command pallete  (CTRL+SHIFT+P)
	1. Search for **Reopen in Container**
	1. Select **Reopen in Container**
1. Run the demo scripts 
1. Run the tests with `pytest`:
	```terminal
	pytest -q
	```
1. Return to local workspace
	1. Open command pallete  (CTRL+SHIFT+P)	 
	1. Search for **Reopen Folder Locally**
	1. Select **Reopen Folder Locally**


> Note: If you have trouble loading container, then you can run locally if you install have requirements installed.

```bash 
# Make sure you are in the virtual environment created for this class.
# If you are using Windows, do not use PowerShell.
pip install -r requirements.txt
```

Notes
- The test suite uses a small dynamic importer so filenames that start with digits can be loaded.
- If you prefer, you can rename files to valid module names (e.g., `selection_sort.py`) and import normally.

