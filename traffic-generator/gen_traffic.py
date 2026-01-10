import time
import requests
import random
import subprocess
import logging
import socket

# Configuración de objetivos (Nombres de servicio en docker-compose)
TARGET_WEB = "http://soc-grafana:3000"
TARGET_HOST = "soc-grafana"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [ATTACKER] - %(message)s')

def wait_for_service():
    logging.info("⏳ Esperando a que el SOC inicie...")
    time.sleep(20)

def simulate_user():
    """Simula navegación normal"""
    try:
        logging.info(f"👤 USER: Navegando en {TARGET_WEB}")
        requests.get(TARGET_WEB, timeout=2)
    except:
        pass

def simulate_nmap():
    """Simula escaneo de puertos (T1046)"""
    logging.info(f"⚔️ ATTACKER: Lanzando Nmap contra {TARGET_HOST}...")
    try:
        subprocess.run(["nmap", "-sS", "-p", "3000,9090", TARGET_HOST], stdout=subprocess.DEVNULL)
    except Exception as e:
        logging.error(f"Error ejecutando nmap: {e}")

def simulate_lfi():
    """Simula ataque web LFI (T1190)"""
    payloads = ["../../etc/passwd", "..%2F..%2Fwindows%2Fwin.ini"]
    logging.info("⚔️ ATTACKER: Probando exploits web...")
    for p in payloads:
        try:
            requests.get(f"{TARGET_WEB}/{p}", timeout=1)
        except:
            pass

if __name__ == "__main__":
    wait_for_service()
    logging.info("🚀 Generador de tráfico iniciado.")
    
    while True:
        action = random.choice(['user', 'user', 'user', 'nmap', 'lfi'])
        
        if action == 'user': simulate_user()
        elif action == 'nmap': simulate_nmap()
        elif action == 'lfi': simulate_lfi()
            
        time.sleep(random.randint(5, 15))
