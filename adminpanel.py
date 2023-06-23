#!/usr/bin/env python
# -*- Coded By ALPERALL -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Site adresini giriniz \n(ör.: örneksite.com yada www.örneksite.com ): ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "AKTİF => ",req_link

def Credit():
	Space(9); print "#####################################"
	Space(9); print "#   <<<   Admin Panel Bulucu  >>>   #"
	Space(9); print "#        Alperall tarafından kodlandı          #"
	Space(9); print "# instagram:alper_all               #"
	Space(9); print "#####################################"

Credit()
findAdmin()
