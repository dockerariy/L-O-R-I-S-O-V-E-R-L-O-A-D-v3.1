import time
import random
import sys
import os

# ANSI Color Codes for that pro terminal look
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear_screen():
    os.system('clear')

def print_banner():
    banner = f"""{RED}{BOLD}
    ██████╗ ██████╗  ██████╗ ███████╗
    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
    ██║  ██║██║  ██║██║   ██║███████╗
    ██║  ██║██║  ██║██║   ██║╚════██║
    ██████╔╝██████╔╝╚██████╔╝███████║
    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
    {CYAN}>>> L O R I S   O V E R L O A D  v3.1{RESET}
    {YELLOW}>>> Coded by: dockerariy (GitHub){RESET}
    """
    print(banner)

def generate_fake_ip():
    return f"{random.randint(11, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

def loading_animation():
    print(f"{CYAN}[*] Initializing botnets...{RESET}")
    time.sleep(1)
    print(f"{CYAN}[*] Bypassing WAF rules...{RESET}")
    time.sleep(1.5)
    print(f"{CYAN}[*] Establishing anonymous proxies...{RESET}")
    time.sleep(1)
    print(f"{GREEN}[+] Setup complete. Ready to strike.{RESET}\n")
    time.sleep(0.5)

def main():
    clear_screen()
    print_banner()
    
    # Fake inputs to make it look interactive
    try:
        target = input(f"{YELLOW}Enter Target IP / Domain: {RESET}")
        port = input(f"{YELLOW}Enter Target Port (e.g., 80, 443): {RESET}")
        threads = input(f"{YELLOW}Enter Thread Count (1000-9999): {RESET}")
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Operation aborted by user.{RESET}")
        sys.exit()

    print("\n")
    loading_animation()
    
    print(f"{RED}{BOLD}>>> INITIATING LAYER 7 ATTACK ON {target}:{port} <<<{RESET}\n")
    time.sleep(1)

    # The fake attack loop
    try:
        packet_count = 0
        while True:
            # Generate fake log data
            fake_ip = generate_fake_ip()
            bytes_sent = random.randint(1024, 8192)
            ping = random.randint(12, 140)
            
            # Randomize the output style slightly for realism
            if random.random() > 0.1:
                log = f"{GREEN}[+] {time.strftime('%H:%M:%S')} | Injecting {bytes_sent} bytes from {fake_ip} | Status: 200 OK | Latency: {ping}ms{RESET}"
            else:
                log = f"{YELLOW}[!] {time.strftime('%H:%M:%S')} | Re-routing node {fake_ip} | Status: CONNECTION DROP | Retrying...{RESET}"
            
            print(log)
            sys.stdout.flush() # Forces the terminal to print immediately
            
            packet_count += 1
            
            # Sleep for a tiny fraction of a second to make the text scroll fast but readable
            time.sleep(random.uniform(0.01, 0.05))

    except KeyboardInterrupt:
        print(f"\n\n{RED}{BOLD}>>> ATTACK HALTED <<<{RESET}")
        print(f"{CYAN}Total packets simulated: {packet_count}{RESET}")
        print(f"{YELLOW}Cleaning up tracks... Done.{RESET}")
        sys.exit()

if __name__ == "__main__":
    main()
