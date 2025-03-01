import os

target_ip = "[target_ip]"  # Replace with TryHackMe IP
output = os.popen(f"nmap -sV {target_ip}").read()
print("Nmap Scan Results:")
print(output)

with open("/home/mohammad/Portfolio/day2_nmap_output.txt", "w") as f:
    f.write(output)

