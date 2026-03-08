import subprocess

def run_subfinder(domain):
    command = ["subfinder", "-d", domain]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def run_ffuf(domain):
    command = [
        "ffuf",
        "-u", f"https://{domain}/FUZZ",
        "-w", "wordlist.txt"
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout