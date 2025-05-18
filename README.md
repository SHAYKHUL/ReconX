````markdown
# ReconX
A lightweight CLI recon toolkit for Kali Linux written in Python.

## Usage

```bash
./reconx.py -t example.com --dns --subs --ports --waf
````

## Features

* DNS Lookup
* Subdomain Enumeration
* Port Scanning (Top Ports)
* WAF Detection

## Install

```bash
pip install -r requirements.txt
chmod +x reconx.py
```

````

---

### ✅ How to Use

```bash
git clone https://github.com/yourname/reconx.git
cd reconx
pip install -r requirements.txt
chmod +x reconx.py
./reconx.py -t example.com --dns --subs --ports --waf
````

---

## 💡 Future Ideas

* Add Shodan/Whois integrations
* Export results as JSON/HTML
* Use concurrency (asyncio/threading)
* Auto-update module
