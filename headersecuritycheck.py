from requests import *

def check_security_headers(url):
  # Envoyer une requête GET à l'URL
  response = requests.get(url)

  # Vérifier la présence de l'en-tête X-XSS-Protection
  xss_protection = response.headers.get('X-XSS-Protection')
  if xss_protection:
    print('{+} X-XSS-Protection header found')
  else:
    print('{-} X-XSS-Protection header not found')

  # Vérifier la présence de l'en-tête X-Content-Type-Options
  content_type_options = response.headers.get('X-Content-Type-Options')
  if content_type_options:
    print('{+} X-Content-Type-Options header found')
  else:
    print('{-} X-Content-Type-Options header not found')

  # Vérifier la présence de l'en-tête Content-Security-Policy
  csp = response.headers.get('Content-Security-Policy')
  if csp:
    print('{+} Content-Security-Policy header found')
  else:
    print('{-} Content-Security-Policy header not found')

# Tester le script avec un URL
check_security_headers('https://www.example.com')
