# 🛡️ Mini SOC Lab — Dockerized Blue Team Environment

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Suricata](https://img.shields.io/badge/Suricata-EF3B2D?style=for-the-badge&logo=suricata&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

> **A fully isolated, reproducible Security Operations Center (SOC) lab focused on monitoring, detection, log analysis, and alerting.**

---

## 📌 Overview

This project simulates a realistic **Blue Team environment**. It ingests telemetry, detects suspicious activity via **Suricata IDS & Zeek**, visualizes events in **Grafana**, and triggers real-time alerts.

The entire stack is deployed using **Docker Compose**, featuring an **internal "Attacker" container** that generates real traffic and attacks, allowing you to see the SOC in action immediately without external VMs.

---

## 🧱 Architecture

The architecture consists of three main components working in unison:

1.  **Offensive Stack:** An internal attacker container generating Nmap scans, LFI attacks, and noise.
2.  **Defensive Stack:** * **Suricata & Zeek:** Analyze traffic via traffic mirroring.
    * **Promtail:** Ships logs to Loki.
    * **Node Exporter:** Sends system metrics to Prometheus.
3.  **Visualization:** Grafana displays dashboards and sends alerts via Discord Webhooks.

### 🎯 Key Objectives
* **Realistic Simulation:** Centralize metrics, logs, and alerts in a single pane of glass.
* **Hands-on Defense:** Practice IDS tuning (Suricata) and metadata analysis (Zeek).
* **Traffic Correlation:** Correlate system spikes (CPU/RAM) with security events.
* **Detection Engineering:** Map alerts to **MITRE ATT&CK** techniques.

---

## ⚡ Quick Start (The "Out of the Box" Experience)

You don't need complex external VMs to test this. The lab comes with an auto-attacker.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/proxmy/mini-soc-lab.git](https://github.com/proxmy/mini-soc-lab.git)
    cd mini-soc-lab
    ```

2.  **Launch the stack:**
    ```bash
    docker compose up -d
    ```

3.  **Wait ~30 seconds** for the services to initialize.

4.  **Access Grafana:**
    * **URL:** `http://localhost:3000`
    * **User:** `admin`
    * **Password:** `admin` (or check `.env`)

> **🚀 Instant Action:** The `attacker` container will automatically start launching Nmap scans and web attacks against the SOC. Check the **"Security Overview"** dashboard to see alerts populating immediately.

---

## 🧰 Technology Stack

| Category | Tool | Function |
| :--- | :--- | :--- |
| **Observability** | ![Grafana](https://img.shields.io/badge/-Grafana-gray?logo=grafana) | Dashboards, Visualization & Alerting |
| **Metrics** | ![Prometheus](https://img.shields.io/badge/-Prometheus-gray?logo=prometheus) | Time-series metrics collection |
| **Logging** | ![Loki](https://img.shields.io/badge/-Loki-gray?logo=grafana) | Log aggregation and query engine |
| **Ingestion** | ![Promtail](https://img.shields.io/badge/-Promtail-gray?logo=grafana) | Log shipping and labeling |
| **IDS / IPS** | ![Suricata](https://img.shields.io/badge/-Suricata-gray?logo=suricata) | Network Intrusion Detection (ET Open Rules) |
| **NSM** | **Zeek** | Network Security Monitoring (Metadata analysis) |
| **Automation** | **Python** | Automated traffic & attack generation |

---

## 🗺️ MITRE ATT&CK Mapping

This lab is designed to detect specific adversarial techniques.

| ID | Tactic | Technique | Detection Method |
| :--- | :--- | :--- | :--- |
| **T1046** | Discovery | Network Service Scanning | **Suricata** detects Nmap SYN scans. |
| **T1190** | Initial Access | Exploit Public-Facing App | **Suricata** alerts on Directory Traversal / LFI. |
| **T1071** | Command & Control | Application Layer Protocol | **Zeek** logs suspicious connection metadata. |

---

## ⚙️ Advanced Configuration (Optional)

If you prefer to use **External VMs** (e.g., VirtualBox) instead of the internal Docker attacker, follow this network topology.

<details>
<summary><b>🔻 Click to expand VM Network Setup</b></summary>

### Recommended VM Network
* **SOC Server VM:**
    * Adapter 1: **NAT** (Internet/Docker pull)
    * Adapter 2: **Host-only** (Traffic Inspection)
* **Attacker VM (Kali/Ubuntu):**
    * Adapter 1: **Host-only** (Targeting the SOC)

### ⚠️ Interface Selection
If your VM has multiple interfaces, you must tell Suricata which one to listen on in `docker-compose.yml` or `suricata.yaml`:
```bash
# Check interfaces
ip -br link
</details>

🔔 Alerting Setup (Discord)
To receive real-time notifications on your phone/PC:

Create a Webhook in your Discord Server (Server Settings → Integrations → Webhooks).

Configure Grafana:

Go to Alerting → Contact points.

Add new: Discord.

Paste your Webhook URL.

Click Test (You should see a message in Discord).

🧪 Validation & Testing
Method A: Automatic (Default)
Just watch the dashboards! The attacker container runs a loop of:

Benign traffic (HTTP browsing)

Port Scans (Nmap)

Web Exploits (LFI payloads)

Method B: Manual (Interactive)
Access the attacker container shell to run custom commands:

Bash

docker exec -it soc-attacker /bin/bash

# Run a manual scan
nmap -sV soc-suricata
📂 Repository Structure
Plaintext

mini-soc-lab/
├── docker-compose.yml       # Orchestration of the full stack
├── .env.example             # Environment variables
├── traffic-generator/       # Python scripts for noise/attacks
├── suricata/
│   ├── rules/               # Local rules & ET Open config
│   └── suricata.yaml        # IDS Configuration
├── zeek/                    # Zeek local policies
├── grafana/                 # Provisioning & Dashboards
├── loki/                    # Log retention config
└── docs/                    # Architecture & Troubleshooting
⚠️ Disclaimer
This lab is for educational and defensive purposes only. All testing is performed in an isolated environment.
