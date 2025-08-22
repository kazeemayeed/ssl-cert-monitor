# Security Policy

## Supported Versions

We actively maintain and support only the **latest release** of the project.  
Please upgrade to the latest version to benefit from security fixes and updates.

| Version        | Supported     |
|----------------|---------------|
| Latest release |  Yes        |
| Older versions |  No         |

---

## Reporting a Vulnerability

If you discover a security issue, please **do not open a public GitHub issue**.  
Instead, report it responsibly:

1. git checkout -b feature/<short-description>
# or
git checkout -b fix/<short-description> 

2. **Do not** share exploit details publicly until the issue is resolved.  

3. We will acknowledge your report within **48 hours** and provide a timeline for remediation.

---

## Disclosure Policy

We follow a **responsible disclosure** model:
- Security issues will be handled **privately and discreetly**
- Once resolved, a public advisory will be issued—unless you've requested anonymity
- Please allow a reasonable time period before publicly sharing details

---

## Project Security Best Practices

To help keep your deployment secure:
- Always use the **latest release**
- Avoid committing secrets, API keys, or private certificates into the repository
- Use `.gitignore` to prevent accidental inclusion of sensitive files (e.g., `config.yaml`, `.env`)
- Regularly scan dependencies for vulnerabilities using tools like GitHub Dependabot or similar :contentReference[oaicite:0]{index=0}
- Consider enabling GitHub's built-in **Code Scanning** and **Security Alerts** for early detection of issues :contentReference[oaicite:1]{index=1}

---

## Acknowledgements

Thank you for helping us keep **ssl-cert-monitor** safe, secure, and reliable!

