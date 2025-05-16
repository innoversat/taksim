import os


def restart_nginx():
    os.system("sudo systemctl restart nginx")
