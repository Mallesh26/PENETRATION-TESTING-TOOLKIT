# PENETRATION TESTING TOOLKIT
*COMPANY*:CODTECH IT SOLUTIONS
*NAME*:Mudavath Mallesh Nayak
*INTERN ID*:CT04DL263
*DOMAIN*: Cyber Security & Ethical Hacking
*DURATION*:4 Weeks
*MENTOR*:NEELA SANTOSH KUMAR

## DESCRIPTION ##
Penetration Testing Toolkit (Python-Based)

This project is a modular penetration testing toolkit built using Python, designed for ethical hacking and security testing of network services. It provides essential tools commonly used during security assessments, all bundled in an easy-to-use command-line interface.

Key Features:
Port Scanner
Scans a target IP address for open TCP ports and identifies active services. It uses socket connections to check which ports are open, helping assess the attack surface.

FTP Brute Forcer
Performs a dictionary attack on an FTP server using a list of usernames and passwords. If successful credentials are found, it reports them and logs the result.

SSH Brute Forcer
Attempts to gain SSH access to a target system using a brute-force method. It uses the paramiko library to connect and authenticate via SSH. Successful and failed login attempts are printed and logged.

Banner Grabber
Connects to a specified port and captures the service banner, which can reveal software versions and help identify potential vulnerabilities.

Logging
Each module logs the results (successful logins, errors, and failures) to a centralized log file, results.txt, for analysis and reporting.

File Structure:
main.py – Entry point of the toolkit

modules/ – Contains separate Python files for each feature (port_scanner.py, ftp_bruteforce.py, ssh_bruteforce.py, banner_grabber.py)

usernames.txt & passwords.txt – Wordlists used for brute-force attacks

results.txt – Log file capturing the outcome of each operation

Usage:
Run main.py, choose an option from the menu, and input the required target and file paths. The program will execute the chosen module and display the results in the terminal as well as the log file.

This toolkit is educational and intended for use in legal penetration testing and cybersecurity research.


