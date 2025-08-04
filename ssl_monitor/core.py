import socket
import ssl
import datetime
import yaml
import requests
import logging
from typing import List, Dict

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(path: str = "config.yaml") -> Dict:
    with open(path, 'r') as file:
        return yaml.safe_load(file)

def get_ssl_expiry_date(hostname: str, port: int = 443) -> datetime.datetime:
    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    conn.settimeout(10.0)
    conn.connect((hostname, port))
    ssl_info = conn.getpeercert()
    expiry_str = ssl_info['notAfter']
    return datetime.datetime.strptime(expiry_str, '%b %d %H:%M:%S %Y %Z')

def send_slack_notification(message: str, webhook_url: str):
    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        raise Exception(f"Slack webhook failed: {response.status_code}, {response.text}")

def check_certificates(domains: List[Dict], threshold_days: int, slack_webhook: str):
    today = datetime.datetime.utcnow()

    for domain in domains:
        try:
            expiry_date = get_ssl_expiry_date(domain['url'], domain.get('port', 443))
            days_left = (expiry_date - today).days
            logging.info(f"{domain['name']} ({domain['url']}) certificate expires in {days_left} days")

            if days_left <= threshold_days:
                msg = f"⚠️ SSL certificate for *{domain['name']}* ({domain['url']}) expires in {days_left} days (on {expiry_date})."
                send_slack_notification(msg, slack_webhook)

        except Exception as e:
            logging.error(f"Error checking {domain['name']} ({domain['url']}): {e}")
            error_msg = f"❌ Error checking SSL cert for *{domain['name']}* ({domain['url']}): {e}"
            send_slack_notification(error_msg, slack_webhook)

def main():
    config = load_config()
    domains = config.get("domains", [])
    alert_conf = config.get("alert", {})
    threshold = alert_conf.get("threshold_days", 30)
    slack_webhook = alert_conf.get("slack_webhook", "")

    if not slack_webhook:
        logging.error("Slack webhook URL is missing in config.yaml")
        return

    check_certificates(domains, threshold, slack_webhook)

if __name__ == "__main__":
    main()
