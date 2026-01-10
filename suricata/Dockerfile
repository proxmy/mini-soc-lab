FROM jasonish/suricata:latest

# Instalar dependencias si faltan
RUN dnf install -y python3-pip || true

# Copiar script de arranque
COPY scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
