import os


def test_nginx():
    result = os.system("sudo nginx -t")
    if result.returncode == 0:
        print("Nginx is working, and config is valid.")
    else:
        print("Nginx is not working, or config is invalid.")
