import json
import re

# Función 1: Evaluar la seguridad de contraseñas
def evaluate_passwords(file_path='passwords.txt'):
    with open(file_path, 'r') as file:
        passwords = file.readlines()
    
    for password in passwords:
        password = password.strip()
        score = 0
        
        # Condiciones para aumentar el score
        if len(password) >= 8:
            score += 20
        if re.search(r'[A-Z]', password):
            score += 20
        if re.search(r'[a-z]', password):
            score += 20
        if re.search(r'\d', password):
            score += 20
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 20

        print(f"Password: {password} - Security Score: {score}%")

# Función 2: Comparar versiones de software
def check_software_updates(current_versions_file='software_versions.json', updates_file='software_update.json'):
    with open(current_versions_file, 'r') as file:
        current_versions = json.load(file)
    
    with open(updates_file, 'r') as file:
        updates = json.load(file)
    
    for software, current_version in current_versions.items():
        latest_version = updates.get(software)
        if latest_version:
            if current_version < latest_version:
                print(f"{software} is outdated. Current version: {current_version}, Latest version: {latest_version}")
            else:
                print(f"{software} is up to date. Current version: {current_version}")

# Función 3: Verificar sospechas de phishing en correos electrónicos
def check_email_for_phishing(file_path='email_log.txt'):
    phishing_indicators = {
        "urgent": 10,
        "immediate action": 10,
        "verify your account": 20,
        "click here": 20,
        "winner": 10,
        "free": 10,
        "prize": 10,
        "update your information": 20,
        "password": 10,
        "login": 10,
    }
    
    with open(file_path, 'r') as file:
        email_body = file.read().strip().lower()
    
    score = 0
    for indicator, value in phishing_indicators.items():
        if indicator in email_body:
            score += value
    
    score = min(score, 100)  # Ensure the score does not exceed 100%
    print(f"Phishing Score: {score}%")
