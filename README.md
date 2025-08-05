# recon-tool
A modular reconnaissance tool for offensive security
# Recon Tool 🕵️‍♂️

A custom reconnaissance tool for offensive security tasks, built with Python.  
It automates passive and active recon tasks to help penetration testers gather intelligence efficiently.

---

## 🚀 Features

- 🔍 **Passive Reconnaissance**  
  - WHOIS Lookup  
  - DNS & Subdomain Enumeration

- 🔨 **Active Reconnaissance**  
  - Port Scanning (Nmap)  
  - Banner Grabbing  
  - Technology Detection

- 📝 **Report Generation**  
  - Automatically creates HTML reports using Jinja2 templates

---

## 🛠️ Requirements

This tool requires the following Python libraries:

- `python-whois`
- `dnspython`
- `requests`
- `python-nmap`
- `jinja2`

---

## ⚙️ Installation

1. Clone this repository:

bash
git clone https://github.com/mabdullahabd888/recon-tool.git
cd recon-tool

2. Create a virtual environment (optional but recommended):

bash
python3 -m venv venv
source venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

4.Run the tool from the terminal:

python3 main.py

📂 Output
Results are shown in the terminal

An HTML report is generated in the /reports/ folder

🤝 Contributing
Feel free to fork and improve the tool. Pull requests are welcome!




