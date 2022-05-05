import ssl
import urllib
import urllib.parse
from OpenSSL import crypto # pip install pyopenssl
# Alipay, a trusted payment provider
url = 'https://global.alipay.com'
addr = urllib.parse.urlsplit(url).hostname
port = 443
cert = ssl.get_server_certificate((addr, port), ssl_version=3)
cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
#print(cert)
issuer = cert.get_issuer()
print(issuer.get_components())
subject = cert.get_subject()
components = dict(subject.get_components()) # convert to dict
print(components)