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

## ▶️ How to Run

```bash
git clone https://github.com/proxmy/mini-soc-lab.git
cd mini-soc-lab
docker compose up -d
