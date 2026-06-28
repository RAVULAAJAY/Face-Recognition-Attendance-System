import cx_Freeze
import sys
import os

base = None 
if sys.platform == "win32":
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\alize\AppData\Local\Programs\Python\Python312\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\alize\AppData\Local\Programs\Python\Python312\tcl\tk8.6"

executables = [cx_Freeze.Executable("First.py", base=base, icon="M.ico")]

cx_Freeze.setup(
    name="Face Recognition System",
    options={
        "build_exe": {
            "packages": ["tkinter", "os"],
            "include_files": ["M.ico", "tcl86t.dll", "tk86t.dll","Images","Faces","database","Attendance"]
        }
    },
    version="1.0",
    description="Face Recognition Attendance System | Developed By Ajay",
    executables=executables
)
