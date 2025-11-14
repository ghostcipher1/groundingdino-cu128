# Security Policy

## Supported Versions

We currently support the following versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 0.2.x   | :white_check_mark: |
| < 0.2   | :x:                |

## Reporting a Vulnerability

We take the security of groundingdino-cu128 seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via:

1. **GitHub Security Advisory**: Use the [GitHub Security Advisory](https://github.com/ghostcipher1/groundingdino-cu128/security/advisories/new) feature (preferred)

2. **Email**: Send an email to ghostcipher1 via GitHub contact methods

### What to Include

Please include the following information:

- Type of vulnerability
- Full paths of source file(s) related to the vulnerability
- Location of the affected source code (tag/branch/commit or direct URL)
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the vulnerability and how an attacker might exploit it

### Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 1 week
- **Fix Timeline**: Depends on severity and complexity

### Disclosure Policy

- Security issues will be disclosed publicly after a fix is available
- We will credit reporters in the security advisory (unless you prefer to remain anonymous)
- We aim to release security patches as soon as possible

## Security Best Practices for Users

### When Using This Package

1. **Keep Dependencies Updated**
   ```bash
   pip install --upgrade groundingdino-cu128
   ```

2. **Verify Package Integrity**
   ```bash
   pip install groundingdino-cu128 --require-hashes
   ```

3. **Use Virtual Environments**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install groundingdino-cu128
   ```

4. **Review Dependencies**
   ```bash
   pip show groundingdino-cu128
   pip list
   ```

### When Contributing

1. **Never commit secrets** (API keys, credentials, etc.)
2. **Use .gitignore** to exclude sensitive files
3. **Review dependencies** before adding new ones
4. **Run security scanners** before submitting PRs:
   ```bash
   pip install bandit safety
   bandit -r groundingdino shadow_dino
   safety check
   ```

## Security Features

### Current Security Measures

- **Automated Dependency Scanning**: Dependabot monitors dependencies
- **Code Quality Checks**: Automated linting and security scanning in CI/CD
- **License Compliance**: Apache 2.0 license enforcement
- **No Credential Leaks**: CI validates no sensitive data in commits

### Known Limitations

- This package includes CUDA extensions that compile C++/CUDA code
- CUDA code execution depends on NVIDIA drivers and CUDA toolkit security
- Users should ensure they're using updated CUDA drivers and toolkits

## Third-Party Dependencies

This project depends on:

- PyTorch (BSD-style license)
- torchvision (BSD-style license)
- transformers (Apache 2.0)
- Other dependencies listed in requirements.txt

We monitor these dependencies for security vulnerabilities through:
- GitHub Dependabot
- Automated CI checks
- Manual security reviews

## Security Contacts

- **GitHub Issues**: For non-security bugs
- **GitHub Security Advisory**: For security vulnerabilities
- **GitHub Discussions**: For security-related questions

## Acknowledgments

We appreciate the security research community and will acknowledge researchers who responsibly disclose vulnerabilities.

## Compliance

This project:
- Follows the Apache License 2.0
- Maintains attribution to original GroundingDINO authors
- Does not include malicious code or backdoors
- Undergoes automated security scanning

## Updates

This security policy may be updated periodically. Check this file for the latest version.

Last updated: 2025-11-08
