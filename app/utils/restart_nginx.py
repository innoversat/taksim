import os


def restart_nginx():
    result = os.system("sudo systemctl restart nginx")
    if result.returncode == 0:
        print("Nginx restarted successfully.")
    else:
        print("Nginx failed to restart.")
        raise Exception("Nginx failed to restart.")
