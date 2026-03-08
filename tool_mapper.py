TOOL_MAP = {
    "Cross Site Scripting": ["Burp Suite", "Dalfox", "XSStrike"],
    "SQL Injection": ["sqlmap", "Burp Suite"],
    "Insecure Direct Object Reference": ["Burp Suite", "Postman"],
    "Server Side Request Forgery": ["Burp Collaborator"],
    "Remote Code Execution": ["Metasploit"],
    "Sensitive Data Exposure": ["Burp Suite", "Wireshark"]
}

def recommend_tools(vulns):

    recommendations = {}

    for vuln in vulns:
        tools = TOOL_MAP.get(vuln, ["Manual Testing"])
        recommendations[vuln] = tools

    return recommendations