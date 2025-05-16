import os


def test_nginx():
    os.system("sudo nginx -t")
