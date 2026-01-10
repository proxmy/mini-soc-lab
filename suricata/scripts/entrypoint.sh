#!/bin/bash

echo "🔄 [SURICATA] Actualizando reglas (ET Open)..."
suricata-update --no-reload

echo "🚀 [SURICATA] Iniciando motor IDS..."
# Asegurar permisos para que Suricata pueda escribir logs
chown -R suricata:suricata /var/log/suricata
chown -R suricata:suricata /var/lib/suricata

# Ejecutar Suricata apuntando a la interfaz correcta
exec suricata -c /etc/suricata/suricata.yaml -i eth0
