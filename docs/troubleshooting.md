# 🧰 Troubleshooting & Lessons Learned

This document lists **real issues encountered during development** and how they were resolved.

---

## Grafana dashboards disappeared after restart
**Cause**
- Grafana container had no persistent volume

**Fix**
- Added Docker volume for `/var/lib/grafana`

---

## Prometheus / Loki not visible in Grafana
**Cause**
- Datasources not provisioned automatically

**Fix**
- Added Grafana provisioning files under:
  - `grafana/provisioning/datasources`
  - `grafana/provisioning/dashboards`

---

## Suricata started but no alerts appeared
**Cause**
- Wrong network interface selected

**Fix**
- Identified correct interface using:
```bash
ip -br link

