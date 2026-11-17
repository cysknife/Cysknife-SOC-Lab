#!/usr/bin/env python3
"""
Cysknife SOC Lab - Attack Simulator
Simulates specific attack scenarios for training
"""

import time
import random
from datetime import datetime

class AttackSimulator:
    def __init__(self):
        self.attacker_ip = "203.0.113.100"
        
    def simulate_brute_force(self):
        """Simulate SSH brute force attack"""
        print("🔐 Simulating SSH Brute Force Attack...")
        
        usernames = ["admin", "root", "user", "test", "oracle"]
        
        for i in range(20):
            username = random.choice(usernames)
            print(f"  Attempt {i+1}: {username}:{random.randint(1000, 9999)}")
            time.sleep(0.1)
    
    def simulate_sql_injection(self):
        """Simulate SQL injection attack"""
        print("💉 Simulating SQL Injection Attack...")
        
        payloads = [
            "' OR '1'='1",
            "'; DROP TABLE users; --",
            "' UNION SELECT username, password FROM users --",
            "1' OR '1'='1' --",
            "admin'--",
        ]
        
        endpoints = ["/login", "/search", "/products", "/users"]
        
        for i in range(10):
            endpoint = random.choice(endpoints)
            payload = random.choice(payloads)
            print(f"  {endpoint}?q={payload}")
            time.sleep(0.2)
    
    def simulate_phishing_campaign(self):
        """Simulate phishing email campaign"""
        print("📧 Simulating Phishing Campaign...")
        
        subjects = [
            "Urgent: Account Verification Required",
            "Password Reset Request",
            "Package Delivery Notification",
            "Security Alert: Suspicious Activity"
        ]
        
        for i in range(5):
            subject = random.choice(subjects)
            recipient = f"user{i+1}@company.com"
            print(f"  Email to {recipient}: {subject}")
            time.sleep(0.3)

if __name__ == "__main__":
    simulator = AttackSimulator()
    
    print("🎯 Cysknife SOC Lab - Attack Simulator")
    print("=" * 50)
    
    while True:
        print("\nSelect attack to simulate:")
        print("1. Brute Force Attack")
        print("2. SQL Injection")
        print("3. Phishing Campaign")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == "1":
            simulator.simulate_brute_force()
        elif choice == "2":
            simulator.simulate_sql_injection()
        elif choice == "3":
            simulator.simulate_phishing_campaign()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")