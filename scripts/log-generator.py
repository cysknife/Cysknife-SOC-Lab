#!/usr/bin/env python3
"""
Cysknife SOC Lab - Log Generator
Generates realistic cybersecurity logs for training purposes
"""

import random
import time
import json
import logging
from datetime import datetime, timedelta
import socket
import threading

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class LogGenerator:
    def __init__(self):
        self.internal_ips = [
            "192.168.1.10", "192.168.1.20", "192.168.1.30", "192.168.1.40",
            "10.0.0.5", "10.0.0.10", "10.0.0.15", "10.0.0.20"
        ]
        self.external_ips = [
            "203.0.113.1", "203.0.113.5", "198.51.100.1", "198.51.100.10",
            "192.0.2.1", "192.0.2.10", "172.16.0.1", "172.16.0.10"
        ]
        self.users = ["admin", "jsmith", "mjones", "awilson", "kanderson", "root", "service_account"]
        self.attacker_ips = ["203.0.113.100", "198.51.100.200", "192.0.2.200"]
        
    def generate_windows_event_logs(self):
        """Generate Windows Event Log entries"""
        events = [
            # Successful logins
            {"event_id": 4624, "user": random.choice(self.users), 
             "ip": random.choice(self.internal_ips), "status": "SUCCESS"},
            # Failed logins (brute force)
            {"event_id": 4625, "user": "admin", 
             "ip": random.choice(self.attacker_ips), "status": "FAILED"},
            # Account management
            {"event_id": 4720, "user": random.choice(self.users),
             "target": random.choice(self.users), "status": "ACCOUNT_CREATED"},
            # Process creation
            {"event_id": 4688, "process": "cmd.exe", 
             "user": random.choice(self.users), "status": "CREATED"},
        ]
        
        for event in events:
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "source": "windows_event_log",
                "event_id": event["event_id"],
                "user": event["user"],
                "ip_address": event["ip"],
                "status": event["status"],
                "computer": "DC01" if random.random() > 0.5 else "WS01"
            }
            self.send_to_siem(log_entry)
    
    def generate_web_server_logs(self):
        """Generate Apache/Nginx web server logs"""
        paths = ["/login", "/admin", "/api/users", "/wp-admin", "/phpmyadmin", "/config"]
        methods = ["GET", "POST", "PUT", "DELETE"]
        status_codes = [200, 200, 200, 302, 400, 401, 403, 404, 500]
        
        for _ in range(random.randint(5, 15)):
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "source": "web_server",
                "ip": random.choice(self.external_ips + self.internal_ips),
                "method": random.choice(methods),
                "path": random.choice(paths),
                "status": random.choice(status_codes),
                "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            self.send_to_siem(log_entry)
    
    def generate_security_events(self):
        """Generate security-specific events"""
        security_events = [
            # Brute force attack
            {"type": "brute_force", "source_ip": random.choice(self.attacker_ips),
             "target": "SSH Service", "attempts": random.randint(5, 50)},
            # SQL Injection attempt
            {"type": "sql_injection", "source_ip": random.choice(self.attacker_ips),
             "endpoint": "/login", "payload": "' OR '1'='1"},
            # Phishing email
            {"type": "phishing", "source_ip": random.choice(self.attacker_ips),
             "subject": "Urgent: Account Verification Required"},
            # Malware detection
            {"type": "malware", "file": "invoice.exe",
             "detection": "Trojan.GenericKD.12345"},
            # Data exfiltration
            {"type": "data_exfil", "source_ip": random.choice(self.attacker_ips),
             "bytes_transferred": random.randint(1000000, 100000000)},
        ]
        
        for event in security_events:
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "source": "security_events",
                "event_type": event["type"],
                "severity": "HIGH" if event["type"] in ["malware", "data_exfil"] else "MEDIUM",
                **event
            }
            self.send_to_siem(log_entry)
    
    def send_to_siem(self, log_entry):
        """Send log entry to SIEM (Splunk HTTP Event Collector)"""
        try:
            # For training purposes, we'll also write to local file
            with open("/logs/cysknife_logs.jsonl", "a") as f:
                f.write(json.dumps(log_entry) + "\n")
            
            # In real scenario, this would send to Splunk HEC
            # socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((self.siem_ip, self.siem_port))
            
            logger.info(f"Generated {log_entry['source']} event: {log_entry.get('event_type', 'N/A')}")
            
        except Exception as e:
            logger.error(f"Error sending log: {e}")
    
    def run_continuous(self):
        """Run log generation continuously"""
        logger.info("Starting Cysknife SOC Lab Log Generator...")
        
        while True:
            try:
                # Generate different types of logs
                self.generate_windows_event_logs()
                time.sleep(random.randint(1, 3))
                
                self.generate_web_server_logs()
                time.sleep(random.randint(1, 3))
                
                self.generate_security_events()
                time.sleep(random.randint(2, 5))
                
                # Occasionally generate more intense attack scenarios
                if random.random() > 0.7:
                    self.generate_attack_campaign()
                
            except KeyboardInterrupt:
                logger.info("Log generator stopped by user")
                break
            except Exception as e:
                logger.error(f"Error in log generation: {e}")
                time.sleep(5)
    
    def generate_attack_campaign(self):
        """Generate a coordinated attack campaign"""
        logger.info("🚨 Generating attack campaign scenario...")
        
        attack_steps = [
            {"step": 1, "action": "Reconnaissance", "description": "Port scanning and service discovery"},
            {"step": 2, "action": "Initial Access", "description": "Phishing email with malicious attachment"},
            {"step": 3, "action": "Execution", "description": "Malware execution on endpoint"},
            {"step": 4, "action": "Persistence", "description": "Create backdoor account"},
            {"step": 5, "action": "Privilege Escalation", "description": "Exploit vulnerability for admin access"},
            {"step": 6, "action": "Credential Access", "description": "Dump password hashes"},
            {"step": 7, "action": "Lateral Movement", "description": "Move to other systems"},
            {"step": 8, "action": "Exfiltration", "description": "Data exfiltration to external server"},
        ]
        
        for step in attack_steps:
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "source": "attack_campaign",
                "campaign_id": f"CAMPAIGN_{random.randint(1000, 9999)}",
                "attack_step": step["step"],
                "action": step["action"],
                "description": step["description"],
                "attacker_ip": random.choice(self.attacker_ips),
                "severity": "CRITICAL"
            }
            self.send_to_siem(log_entry)
            time.sleep(1)

if __name__ == "__main__":
    generator = LogGenerator()
    generator.run_continuous()