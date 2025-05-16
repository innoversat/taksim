import os


def check_sudo():
    if os.geteuid() != 0:
        print("This script must be run with sudo privileges.")
        exit(1)
