# ssl-cert-monitor
This script monitors SSL certificate expiry for a list of domains, notifies via Slack (or email), and can be run as a cronjob or integrated into monitoring stacks like Prometheus (with minor additions).

# SSL Certificate Expiry Monitor

A lightweight Python tool to monitor SSL certificate expiration dates and notify via Slack.

## Features

- Monitors expiry of multiple domains
- Sends Slack alerts if SSL expiry is approaching
- YAML-configurable
- Easy to run as a cronjob or in Kubernetes CronJob

## Setup

1. Clone the repo
2. Configure your `config.yaml` with domains and Slack webhook
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

Run it:

python ssl_monitor.py

Automate (optional)
Add to crontab:

0 9 * * * /usr/bin/python3 /path/to/ssl_monitor.py