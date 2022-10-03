#convert pyside2-designer generater UI-files to Python-files by using the pyside2-uic executable
print("[DEVENV] Converting files...")
import subprocess
subprocess.run(".\calendar.venv\Scripts\pyside2-uic.exe main_ui.ui -o main_ui.py", shell=True, check=True)
subprocess.run(".\calendar.venv\Scripts\pyside2-uic.exe calendar_ui.ui -o calendar_ui.py", shell=True, check=True)
subprocess.run(".\calendar.venv\Scripts\pyside2-uic.exe task_element.ui -o task_element.py", shell=True, check=True)
subprocess.run(".\calendar.venv\Scripts\pyside2-uic.exe error_element.ui -o error_element.py", shell=True, check=True)
subprocess.run(".\calendar.venv\Scripts\pyside2-rcc.exe flags.qrc -o flags_rc.py", shell=True, check=True)
subprocess.run(".\calendar.venv\Scripts\pyside2-rcc.exe tango.qrc -o tango_rc.py", shell=True, check=True)
subprocess.run(".\calendar.venv\Scripts\pyside2-lupdate.exe main_ui.ui calendar_ui.ui error_element.ui -ts eng-fi.ts", shell=True, check=True)
subprocess.run(".\calendar.venv\Lib\site-packages\PySide2\lrelease.exe eng-fi.ts -qm translations/eng-fi.qm", shell=True, check=True)
print("[DEVENV] Files converted!")