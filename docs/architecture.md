# 🧱 Architecture

## Overview
This Mini SOC Lab simulates a **Security Operations Center** using a containerized stack focused on **observability, detection and alerting**.

The environment is fully isolated and reproducible, designed for hands-on Blue Team practice.

---

## Lab Topology

- **SOC Server (Linux VM)**
  - Runs the entire SOC stack via Docker
  - Captures real traffic from its network interface
  - Centralizes metrics, logs and alerts

- **Client/Test VM**
  - Generates controlled network activity
  - Used to validate detection and alerting

---

## Network Design

- **NAT interface**
  - Used for system updates and image pulls

- **Isolated private network (host-only)**
  - Used for traffic analysis and IDS monitoring
  - No exposure to the host or external networks

---

## Data Flow

flowchart LR
  subgraph LAB["Local Lab (Virtualized)"]
    A["Client/Test VM\n(Attacker / Traffic Generator)"]
    B["SOC Server VM\n(Ubuntu + Docker)"]
  end

  subgraph NET["Networks"]
    N1["NAT (Internet)\nUpdates / Docker pulls"]
    N2["Host-only / Isolated network\nLab traffic only"]
  end

  A --- N2
  B --- N2
  B --- N1

  subgraph DOCKER["Docker Stack (on SOC Server VM)"]
    S["Suricata IDS\n(network_mode: host)\nCaptures host-only interface"]
    PTAIL["Promtail\nShips Suricata logs"]
    LOKI["Loki\nCentral log store"]
    PROM["Prometheus\nMetrics store"]
    NODE["Node Exporter\nHost metrics"]
    GRAF["Grafana\nDashboards + Alerting"]
    DIS["Discord\nWebhook notifications"]
  end

  N2 --> S
  S -->|eve.json / alerts| PTAIL
  PTAIL --> LOKI
  NODE --> PROM
  PROM --> GRAF
  LOKI --> GRAF
  GRAF -->|Alert rules| DIS

