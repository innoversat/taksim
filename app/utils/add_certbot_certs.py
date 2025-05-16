import os


def add_certbot_certs(domains: list[str]):
    for domain in domains:
        os.system(f"certbot --nginx -d {domain}")
