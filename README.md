> [!WARNING]  
> Taksim is still in development. It is not ready for production use, be careful when using it.

## Taksim

Taksim is a tool for setting up Nginx with SSL certificates with ease.

## Prerequisites

- Python 3.10+ (of course)
- Nginx
- Certbot

## Installation

```bash
git clone https://github.com/innoversat/taksim.git
cd taksim
```

## Usage

```bash
sudo python main.py -d example.com -d www.example.com -p 3000
```

This command will set Nginx to listen on port 3000 and redirect all requests to the domains to the local server, and Certbot will automatically generate and install the SSL certificate.

> Note: You have to set up Certbot before running this command.

## License

Taksim is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
