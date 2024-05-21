import re

def load_phishing_indicators(file_path='phishing_indicators.txt'):
    indicators = {}
    with open(file_path, 'r') as file:
        for line in file:
            indicator, value = line.strip().split(':')
            indicators[indicator.strip()] = int(value.strip())
    return indicators

def check_email_for_phishing(file_path='email_log.txt', indicators_file='phishing_indicators.txt'):
    phishing_indicators = load_phishing_indicators(indicators_file)
    
    with open(file_path, 'r') as file:
        email_body = file.read().strip().lower()
    
    score = 0
    for indicator, value in phishing_indicators.items():
        if re.search(r'\b' + re.escape(indicator) + r'\b', email_body):
            score += value
    
    score = min(score, 100)  # Ensure the score does not exceed 100%
    print(f"Phishing Score: {score}%")

# Ejemplo de uso:
# check_email_for_phishing('email_log.txt', 'phishing_indicators.txt')
