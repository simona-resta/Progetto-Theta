import socket
from datetime import datetime

def scan_ports(target_ip, start_port, end_port):
    print(f"\nInizio scansione di {target_ip} dalla porta {start_port} alla {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # timeout breve per velocizzare
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"Porta {port}: APERTA")
                open_ports.append(port)
            else:
                print(f"Porta {port}: chiusa")

    print(f"\nScansione completata. Porte aperte trovate: {open_ports}")

if __name__ == "__main__":
    print("Benvenuto nello Scanner di Porte TCP di CavoMagico!\n")
    
    target = input("Inserisci l'indirizzo IP da scansionare: ")
    
    try:
        start = int(input("Inserisci la porta iniziale: "))
        end = int(input("Inserisci la porta finale: "))
        
        if start > end or start < 1 or end > 65535:
            print("Intervallo di porte non valido. Le porte devono essere tra 1 e 65535.")
        else:
            start_time = datetime.now()
            scan_ports(target, start, end)
            end_time = datetime.now()
            print(f"\nDurata scansione: {end_time - start_time}")
    
    except ValueError:
        print("Devi inserire numeri validi per le porte.")
