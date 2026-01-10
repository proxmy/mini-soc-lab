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

## 🔔 Alerting (Discord Integration)

This lab includes **real-time alerting** using **Grafana Alerting** with notifications sent to **Discord** via Webhook.

The alerting setup follows standard Grafana alerting workflows and is intentionally kept simple and robust.

---

## 🔔 Alerting (Discord Integration)

This lab includes **real-time alerting** using **Grafana Alerting** with notifications sent to **Discord** via Webhook.

The alerting setup follows standard Grafana alerting workflows and is intentionally kept simple and robust.

---

### 1️⃣ Create Discord Contact Point (one-time setup)

In Grafana UI:

Grafana → Alerts & IRM → Alerting → Contact points

markdown
Copiar código

Steps:
1. Click **Add contact point**
2. Select **Webhook**
3. Paste your **Discord Webhook URL**
4. Name it: `discord-mini-soc`
5. Click **Save**

---

### 2️⃣ Alert Rule — Infrastructure (High CPU)

This alert monitors high CPU usage on the SOC server.

**Location**
Grafana → Alert rules → New alert rule

less
Copiar código

**Query (Prometheus)**
```promql```
100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
Condition

IS ABOVE 85

For 2m

Labels

ini
Copiar código
team="security"
severity="warning"
Contact point

Copiar código
discord-mini-soc
3️⃣ Alert Rule — Security (Suricata LAB Alerts)
This alert fires whenever Suricata detects a LAB event.

Query (Loki)

logql
Copiar código
sum(count_over_time({job="suricata"} |= "[LAB]" [1m]))
Condition

IS ABOVE 0

For 0m–1m

Labels

ini
Copiar código
team="security"
severity="critical"
Contact point

Copiar código
discord-mini-soc
4️⃣ Minimal Validation
To validate the alerting pipeline:

From the Client/Test VM, send a ping to the SOC server IP
→ Suricata should generate a [LAB] ICMP ping alert

In Grafana → Explore (Loki), run:

logql
Copiar código
{job="suricata"}
and

logql
Copiar código
{job="suricata_eve"}
You should observe:

Suricata log events in Grafana

A Discord notification triggered by the alert rule

This confirms the full pipeline:
Traffic → Detection → Logs → Dashboard → Alert → Notification
---

### 2️⃣ Alert Rule — Infrastructure (High CPU)

This alert monitors high CPU usage on the SOC server.

**Location**


---

## ▶️ How to Run

```bash
git clone https://github.com/your-username/mini-soc-lab.git
cd mini-soc-lab
docker compose up -d
