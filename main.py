from modules import port_scanner
from modules import ftp_bruteforce
from modules import banner_grabber
from modules import ssh_bruteforce

def show_menu():
    print("=== Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. FTP Brute Forcer")
    print("3. Banner Grabber")
    print("4. SSH Brute Forcer")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Select an option: ")
        if choice == "1":
            target = input("Enter target IP address: ")
            port_scanner.scan_ports(target)
        elif choice == "2":
            target = input("Enter FTP target IP address: ")
            userlist = input("Enter path to username list file: ")
            passlist = input("Enter path to password list file: ")
            port = 2122
            ftp_bruteforce.ftp_bruteforce(target, userlist, passlist, port)
        elif choice == "3":
            ip = input("Enter target IP address: ")
            port = int(input("Enter port number: "))
            banner_grabber.grab_banner(ip, port)
        elif choice == "4":
            target = input("Enter SSH target IP address: ")
            port = int(input("Enter SSH port (usually 22): "))
            userlist = input("Enter path to username list file: ")
            passlist = input("Enter path to password list file: ")
            ssh_bruteforce.ssh_bruteforce(target, port, userlist, passlist)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
