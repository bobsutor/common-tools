import os
import shutil
import time


def delete_dir_if_present(_dir):
    if os.path.isdir(_dir):
        # weird Windows permission error work around - something to do with timing
        while True:
            try:
                shutil.rmtree(_dir)
            except PermissionError:
                print(f"Saw PermissionError in 'delete_dir_if_present' for '{_dir}'")
                time.sleep(1.0)
            else:
                break


delete_dir_if_present("__pycache__")

os.system("git add -A")
os.system("git commit")
os.system("git push -u origin main")
