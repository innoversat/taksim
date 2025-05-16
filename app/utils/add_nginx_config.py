import os
from app.utils.restart_nginx import restart_nginx
from app.utils.test_nginx import test_nginx


def add_nginx_config(domains: list[str], port: int):
    config_template = f"""server {{
    listen 80;
    server_name {" ".join(domains)};

    location /.well-known/acme-challenge/ {{
        root /var/www/html;
    }}

    location / {{
        proxy_pass http://localhost:{port};
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }}
}}"""

    for domain in domains:
        config_path = f"/etc/nginx/sites-available/{domain.replace('.', '-')}"
        with open(config_path, "w") as f:
            f.write(config_template)

        os.system(
            f"sudo ln -s /etc/nginx/sites-available/{domain.replace('.', '-')} /etc/nginx/sites-enabled/{domain.replace('.', '-')}"
        )

    restart_nginx()
    test_nginx()
