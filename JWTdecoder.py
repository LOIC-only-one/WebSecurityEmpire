import jwt
# pip install jwt

# Remplacez "TOKEN" par votre JWT
TOKEN = "TOKEN"

# Décodez le JWT en utilisant la clé secrète
DECODED = jwt.decode(TOKEN, 'SECRET_KEY', algorithms='HS256')

# Affichez les informations de déclaration
print(DECODED)
