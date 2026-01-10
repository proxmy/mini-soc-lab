FROM python:3.9-slim

# Instalamos herramientas de red reales
RUN apt-get update && apt-get install -y nmap curl iputils-ping && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY gen_traffic.py .
RUN pip install requests

CMD ["python", "-u", "gen_traffic.py"]
