VULNERABILITY_KEYWORDS = {
    "xss": "Cross Site Scripting",
    "sql injection": "SQL Injection",
    "idor": "Insecure Direct Object Reference",
    "ssrf": "Server Side Request Forgery",
    "csrf": "Cross Site Request Forgery",
    "rce": "Remote Code Execution",
    "authentication bypass": "Authentication Bypass",
    "privilege escalation": "Privilege Escalation",
    "information disclosure": "Sensitive Data Exposure"
}

def find_vulnerabilities(text):

    text = text.lower()

    found = []

    for key, name in VULNERABILITY_KEYWORDS.items():
        if key in text:
            found.append(name)

    return list(set(found))