# Protec - Security API

Protec is a REST API server for managing device security modes (`normal`, `lockdown`, `shutdown`).  
It is built with **FastAPI** and uses **SQLite** as a simple database.

---

## 1. Requirements
- Python 3.10+ installed
- Git (if cloning from repository)

---

## 2. Setup

### Linux / MacOS
```bash
# Clone repository
git clone <your-repo-url>
cd protec

# Create virtual environment
python3 -m venv venv

# Activate environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Windows (PowerShell)
```powershell
# Clone repository
git clone <your-repo-url>
cd protec

# Create virtual environment
python -m venv venv

# Activate environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 3. Running the server

### Development mode (auto-reload)
```bash
python main.py
```

Server will start at:
```
http://127.0.0.1:2016
```

---

## 4. Running as a background service

### Linux (systemd service)
Create file `/etc/systemd/system/protec.service`:
```
[Unit]
Description=Protec Security API
After=network.target

[Service]
User=yourusername
WorkingDirectory=/path/to/protec
ExecStart=/path/to/protec/venv/bin/python /path/to/protec/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl daemon-reload
sudo systemctl enable protec
sudo systemctl start protec
sudo systemctl status protec
```

Logs will appear in `protec.log`.

### Windows (run in background)
Option 1: Run with `pythonw.exe` (no console window):
```powershell
.\venv\Scripts\pythonw.exe main.py
```

Option 2: Use [NSSM (Non-Sucking Service Manager)](https://nssm.cc/):
- Install NSSM
- Run:
```powershell
nssm install Protec "C:\path\to\venv\Scripts\python.exe" "C:\path\to\main.py"
```
- Start service:
```powershell
nssm start Protec
```

---

## 5. Testing the API

Set your token in `config.yaml`. Example:
```yaml
auth:
  token: "supersecrettoken123"
```

Test `/status` (no auth required):
```bash
curl http://127.0.0.1:2016/status/
```

Test `/mode/current` (auth required):
```bash
curl -H "Authorization: Bearer supersecrettoken123" http://127.0.0.1:2016/mode/current
```

---

## 6. Useful commands

### Linux
```bash
source venv/bin/activate
python main.py
```

### Windows
```powershell
.\venv\Scripts\activate
python main.py
```
