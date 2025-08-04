# Changelog

All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/).

---

## [1.0.0]

### Initial Release

- Added support for checking SSL certificate expiry for multiple domains.
- Configurable via `config.yaml` (domain list, threshold days, Slack webhook).
- Slack alert integration for certificates expiring within a threshold.
- Basic error handling and logging included.
- Fully written in Python (lightweight, dependency-minimal).
- Ready to be scheduled via `cron` or integrated into monitoring systems.

## [1.1.0]

- Revised the structure for building a CLI-style script

---

## [Unreleased]

### Planned

- [ ] Email alert integration (SMTP support)
- [ ] Prometheus metrics endpoint (`/metrics`) for Grafana integration
- [ ] Docker container for easy deployment
- [ ] Kubernetes CronJob YAML support
- [ ] Unit tests and GitHub Actions CI pipeline
