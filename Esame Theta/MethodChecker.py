print("Benvenuto in MethodChecker creato da CavoMagico.\n")

import requests

def check_http_methods(url):
    try:
        response = requests.options(url)
        allowed_methods = response.headers.get('Allow')

        if allowed_methods:
            methods_list = [method.strip().upper() for method in allowed_methods.split(',')]
            print(f"Metodi HTTP dichiarati dal server su {url}: {methods_list}")
            print("\nControllo attivo dei metodi HTTP in corso...\n")

            for method in methods_list:
                try:
                    test_response = requests.request(method, url)
                    print(f"[{method}] → Status Code: {test_response.status_code}")
                except requests.RequestException as e:
                    print(f"[{method}] → Errore nella richiesta: {e}")

            return methods_list
        else:
            print(f"Il server non ha specificato i metodi HTTP abilitati per {url}.")
            return []
    except requests.RequestException as e:
        print(f"Errore nella richiesta OPTIONS: {e}")
        return []

if __name__ == "__main__":
    path = input("Inserisci l'URL completo (es. https://www.esempio.com/): ")
    check_http_methods(path)
