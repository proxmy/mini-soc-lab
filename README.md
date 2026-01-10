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

```mermaid
graph TD
    subgraph "Offensive Stack"
      A[👾 Attacker Container] -->|Nmap / LFI / Noise| B(Bridge Network)
    end
    
    subgraph "Defensive Stack (SOC)"
      B -->|Traffic Mirror/Capture| C{Suricata IDS}
      B -->|Traffic Mirror/Capture| D{Zeek NSM}
      C -->|eve.json| E[Promtail]
      D -->|*.log| E
      E -->|Log Stream| F[Loki]
      G[Node Exporter] -->|Metrics| H[Prometheus]
    end

    subgraph "Visualization & Alerting"
      F --> I[Grafana]
      H --> I
      I -->|Webhook| J[🔔 Discord Alerts]
    end
