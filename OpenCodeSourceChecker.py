import requests

# Envoyez une requête GET à l'URL de la page
RESPONSE = requests.get('https://www.example.com')

# Récupérez le code source de la page
PAGE_SOURCE = RESPONSE.text

# Recherchez le mot-clé dans le code source de la page
KEYWORD_INDEX = PAGE_SOURCE.find('keyword')

# Si le mot-clé est trouvé, affichez sa position
if KEYWORD_INDEX != -1:
  print(f'[+] Mot clé trouvé important, {KEYWORD_INDEX}')
else:
  print('[-] No Mot clé')
