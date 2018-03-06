response = requests.get("https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=Example")
print(response.status_code)


