# Simple HTTPS Server

this script is essentially python -m http.server but with HTTPS 

```
openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -subj "/" -keyout key.pem -out cert.pem
python simple-https-server.py
```
