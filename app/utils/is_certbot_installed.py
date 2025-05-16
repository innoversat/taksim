import subprocess


def is_certbot_installed():
    try:
        result = subprocess.run(
            ["certbot", "--version"], capture_output=True, text=True
        )
        if result.returncode == 0:
            return True
        else:
            return False
    except:
        return False
