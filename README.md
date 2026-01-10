# 🛡️ Mini SOC Lab — Dockerized Blue Team Environment

## 📌 Overview
This project is a **Mini Security Operations Center (SOC) lab**, designed to practice **monitoring, detection, log analysis and alerting** in a **fully isolated and reproducible environment**.

The goal is not offensive exploitation, but **observability and defensive operations**, simulating how a SOC ingests telemetry, detects suspicious activity and visualizes events in real time.

The entire stack is deployed using **Docker & Docker Compose**, allowing anyone to spin up the lab with a simple `git clone`.

---

## 🎯 Objectives
- Build a **realistic SOC-style environment**
- Centralize **metrics, logs and security alerts**
- Practice **IDS tuning and noise reduction**
- Correlate **system metrics + security events**
- Learn through **real troubleshooting and iteration**

---

## 🧱 Architecture

**Lab setup**
- 2 Linux virtual machines  
  - **SOC Server**: runs the monitoring and detection stack  
  - **Client/Test Machine**: generates controlled activity  
- Dual network setup:
  - **NAT** → system updates and package downloads  
  - **Isolated private network (host-only)** → traffic analysis without risk  

**Deployment model**
- All services containerized
- Persistent data via Docker volumes
- Explicit versioning (no `latest` tags)

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
- Custom rule set + alert tuning

### 🔔 Alerting
- **Grafana Alerting**
- Notifications sent to **Discord**

### 🐳 Orchestration
- **Docker**
- **Docker Compose**

---

## ▶️ How to Run

```bash
git clone https://github.com/your-username/mini-soc-lab.git
cd mini-soc-lab
docker compose up -d
