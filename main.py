import argparse
from app.utils.check_sudo import check_sudo
from app.utils.is_nginx_installed import is_nginx_installed
from app.utils.add_nginx_config import add_nginx_config
from app.utils.is_certbot_installed import is_certbot_installed
from app.utils.add_certbot_certs import add_certbot_certs


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

    try:
        if not check_sudo():
            print("This script must be run with sudo privileges.")
            exit(1)
        if not is_nginx_installed():
            print("Nginx must be installed to use this script")
            exit(1)
        if not is_certbot_installed():
            print("Certbot must be installed to use this script")
            exit(1)
    except Exception as e:
        print(e)
        exit(1)

    add_nginx_config(args.domains, args.port)
    add_certbot_certs(args.domains)


if __name__ == "__main__":
    main()
