import os


def check_sudo():
    return os.geteuid() == 0
