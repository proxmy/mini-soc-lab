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
