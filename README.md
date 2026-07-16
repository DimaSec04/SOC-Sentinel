# SOC Sentinel

SOC Sentinel is a Python-based Windows Event Log Analyzer designed to simulate basic SOC (Security Operations Center) investigations.

## Features

- Detect Failed Login Attempts (Event ID 4625)
- Count Successful Logins (Event ID 4624)
- Detect Possible Brute Force Attacks
- Analyze Windows Security Events
- Generate Security Report

## Project Structure

```
SOC-Sentinel/
│── app.py
│── analyzer.py
│── report.py
│── sample_logs.txt
│── README.md
│── requirements.txt
```

## Technologies

- Python
- Windows Event IDs
- Log Analysis

## Run

```bash
python app.py
```

## Future Improvements

- PowerShell Detection (4688)
- New User Detection (4720)
- Privilege Escalation Detection (4728)
- Export Report to TXT/PDF
- Flask Dashboard