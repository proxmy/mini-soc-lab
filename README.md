# 🛡️ Mini SOC Lab — Dockerized Blue Team Environment

## 📌 Overview
This project is a **Mini Security Operations Center (SOC) lab**, designed to practice **monitoring, detection, log analysis and alerting** in a **fully isolated and reproducible environment**.

The focus is on **defensive security and observability**, simulating how a SOC ingests telemetry, detects suspicious activity, visualizes events and triggers alerts in real time.

The entire stack is deployed using **Docker & Docker Compose**, allowing the lab to be launched with a simple `git clone`.

---

## 🎯 Objectives
- Build a **realistic SOC-style environment**
- Centralize **metrics, logs and security alerts**
- Practice **IDS tuning and noise reduction**
- Correlate **system metrics with security events**
- Learn through **real troubleshooting and iteration**

---

## 🧱 Architecture

### Recommended VM Network Configuration (Important)

This lab is designed to run inside **virtual machines** using a **dual-network setup**.

#### SOC Server VM
- **Network Adapter 1:** NAT  
  - Used for system updates and Docker image downloads
- **Network Adapter 2:** Host-only / Internal Network  
  - Used for traffic inspection and IDS monitoring

#### Client/Test VM
- **Network Adapter 1:** Host-only / Internal Network only  
  - Used to generate controlled traffic toward the SOC Server

⚠️ Do **not** expose Suricata directly to your home or public network.

### Lab setup
- **2 Linux virtual machines**
  - **SOC Server**: runs the monitoring and detection stack
  - **Client/Test VM**: generates controlled network activity
- **Dual network design**
  - **NAT** → system updates and image downloads
  - **Isolated private network (host-only)** → traffic analysis without external exposure

### Deployment model
- Fully containerized stack
- Persistent data via Docker volumes
- Explicit image versioning (no `latest` tags)

## 🌐 Network Interface Selection (Suricata – Mandatory)

If your SOC Server VM has **multiple network interfaces** (for example NAT + host-only),
you **must manually select the correct interface** for Suricata.

### Step 1: Identify interfaces
Run on the SOC Server VM:
```bash```
ip -br link


---

## 🧰 Technology Stack

### 📊 Observability
- **Grafana** → dashboards and visualization
- **Prometheus** → metrics collection
- **Node Exporter** → host-level metrics

### 📜 Logging
- **Loki** → centralized log storage
- **Promtail** → log shipping and labeling

### 🚨 Security
- **Suricata (IDS)** → network intrusion detection
- Custom local rules and alert tuning

### 🔔 Alerting
- **Grafana Alerting**
- Notifications sent to **Discord**

### 🐳 Orchestration
- **Docker**
- **Docker Compose**

---

## 🪵 Logging Notes

- Suricata logs (`fast.log` and `eve.json`) are fully collected and visualized
- Application and file-based system logs are collected via Promtail
- Journald logs are not collected by default

This lab focuses on **security telemetry**, not full system log ingestion.

## 💾 Storage & Retention Notes

- Loki stores log data locally on disk
- Default retention is suitable for short-lived labs
- Long-running setups may consume significant disk space

For extended usage, consider reducing retention time or increasing disk size.

## ▶️ How to Run

```bash
git clone https://github.com/proxmy/mini-soc-lab.git
cd mini-soc-lab
docker compose up -d

Once deployed

Grafana is available at: http://localhost:3000

All dashboards and data sources are auto-provisioned

Metrics, logs and alerts start flowing immediately

📈 Dashboards

The lab includes preconfigured dashboards for:

System Overview

CPU usage

Memory consumption

Disk usage

Network throughput

Security Overview

Suricata alerts by severity

Top source IPs

Alert timelines

Log Analysis

Centralized logs with filters and labels

📸 Screenshots are available in the /docs/screenshots folder.

🔔 Alerting (Discord Integration)

This lab includes real-time alerting using Grafana Alerting, with notifications sent to Discord via Webhook.

1️⃣ Create Discord Contact Point (one-time setup)

In Grafana UI:

Grafana → Alerts & IRM → Alerting → Contact points


Steps:

Click Add contact point

Select Webhook

Paste your Discord Webhook URL

Name it: discord-mini-soc

Click Save

2️⃣ Alert Rule — Infrastructure (High CPU)

Query (Prometheus)

100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)


Condition

IS ABOVE 85

For 2m

Labels

team="security"

severity="warning"

Contact point

discord-mini-soc

3️⃣ Alert Rule — Security (Suricata LAB Alerts)

Query (Loki)

sum(count_over_time({job="suricata"} |= "[LAB]" [1m]))


Condition

IS ABOVE 0

For 0m–1m

Labels

team="security"

severity="critical"

Contact point

discord-mini-soc

4️⃣ Minimal Validation

From the Client/Test VM, send a ping to the SOC server IP
→ Suricata should generate a [LAB] ICMP ping alert

In Grafana → Explore (Loki), run:

{job="suricata"}


and:

{job="suricata_eve"}


Confirm:

Logs appear in Grafana

A Discord notification is triggered

✅ This validates the full pipeline:
Traffic → Detection → Logs → Dashboard → Alert → Notification

🧪 What This Lab Demonstrates
🔵 Blue Team / SOC Skills

IDS deployment and tuning

Log centralization

Alert triage and visualization

Event correlation

🛠️ DevOps / SRE Practices

Infrastructure as Code

Service observability

Persistent data management

Reproducible environments

🌐 Networking Concepts

Network isolation

Traffic visibility

Source/destination analysis

⚠️ Lessons Learned (Real Issues Solved)

This project documents real problems encountered during development and how they were resolved:

Dashboards disappearing → fixed with persistent volumes

Services unreachable → Docker network misconfiguration

IDS alerts not firing → incorrect network interface selection

Excessive noise → rule tuning and severity filtering

Logs missing in Grafana → label mismatches in Promtail

Detailed explanations are available in:

docs/troubleshooting.md

📁 Repository Structure
mini-soc-lab/
├── docker-compose.yml
├── README.md
├── .env.example
│
├── docs/
│   ├── architecture.md
│   ├── troubleshooting.md
│   └── screenshots/
│
├── grafana/
├── prometheus/
├── suricata/
├── loki/
├── promtail/
└── scripts/

🚀 Roadmap

 Add more Suricata rule examples

 Expand alerting conditions

 Improve dashboards with correlations

 Optional ELK stack comparison

 Export dashboards as reusable templates

⚠️ Disclaimer

This lab is for educational and defensive purposes only.
All testing is performed in an isolated environment under the user's control.
