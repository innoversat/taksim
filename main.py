import argparse
from app.utils.check_sudo import check_sudo
from app.utils.is_nginx_installed import is_nginx_installed
from app.utils.add_nginx_config import add_nginx_config


def main():
    parser = argparse.ArgumentParser(description="Configure Nginx for domains")
    parser.add_argument(
        "-d",
        "--domains",
        action="append",
        required=True,
        help="Domain to configure (can be specified multiple times)",
    )
    parser.add_argument(
        "-p", "--port", type=int, required=True, help="Port number to use"
    )

    args = parser.parse_args()

    print(args)

    try:
        print("Checking if user has sudo privileges...")
        check_sudo()
        print("User has sudo privileges, continuing...")
        print("Checking if Nginx is installed...")
        if not is_nginx_installed():
            print("Nginx is not installed, exiting...")
            exit(1)
        print("Nginx is installed, continuing...")
    except Exception as e:
        print(e)
        exit(1)

    add_nginx_config(args.domains, args.port)


if __name__ == "__main__":
    main()
