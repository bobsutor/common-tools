import os

from os_tools import delete_dir_if_present

delete_dir_if_present("__pycache__")

os.system("git add -A")
os.system("git commit")
os.system("git push -u origin main")
