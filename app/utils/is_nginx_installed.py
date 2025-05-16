import subprocess


def is_nginx_installed():
    try:
        result = subprocess.run(["nginx", "-v"], capture_output=True, text=True)
        if result.returncode == 0:
            return True
        else:
            return False
    except:
        return False
