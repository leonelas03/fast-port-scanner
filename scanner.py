import socket
import concurrent.futures
import time

# Pede o IP ao utilizador
alvo_input = input("🎯 Introduz o IP alvo (ex: 192.168.1.5) ou prime ENTER para localhost: ")

if alvo_input.strip() == "":
    ALVO = "127.0.0.1"
else:
    ALVO = alvo_input

PORTOS_A_TESTAR = range(1, 1025) 

def testar_porto(porto):
    """Tenta ligar a um porto TCP. Retorna o porto se estiver aberto."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        resultado = s.connect_ex((ALVO, porto))
        s.close()
        
        if resultado == 0:
            return porto
        return None
    except:
        return None

def main():
    print("-" * 50)
    print(f"[*] A iniciar scan super rápido ao IP: {ALVO}")
    print("-" * 50)
    
    inicio = time.time()
    portos_abertos = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        resultados = executor.map(testar_porto, PORTOS_A_TESTAR)

    for porto in resultados:
        if porto is not None:
            print(f"[+] Porto Aberto encontrado: {porto}")
            portos_abertos.append(porto)

    tempo_total = time.time() - inicio
    print("-" * 50)
    print(f"[*] Scan concluído em {tempo_total:.2f} segundos.")
    print(f"[*] Total de portos abertos: {len(portos_abertos)}")

if __name__ == "__main__":
    main()