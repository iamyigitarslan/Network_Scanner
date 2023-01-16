from time import sleep
from scapy.all import ARP, Ether, srp

def scanner(path):

    target_ip = "192.168.0.1/24"
# IP Address for the destination
# create ARP packet
    arp = ARP(pdst=target_ip)
# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# stack them
    packet = ether/arp

    result = srp(packet, timeout=10, verbose=0)[0]

# a list of clients, we will fill this in the upcoming loop
    clients = []

    for sent, received in result:
    # for each response, append ip and mac address to `clients` list
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})


    with open(path, "a") as external_file:

        for client in clients:
            print(client['mac'], file=external_file)
            #print("{:16}    {}".format(client['ip'], client['mac']))

    external_file.close()

def removeDubs(path):
    lines_seen = set() # holds lines already seen

    with open(path, "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i not in lines_seen:
                f.write(i)
                lines_seen.add(i)
        f.truncate()

def compare():
                                           
    f1 = open("D:/Bitirme/Bitirme/Network_Scanner/external.txt", "r")  
    f2 = open("D:/Bitirme/Bitirme/Network_Scanner/temp.txt", "r") 
    a=[]
    b=0

    external= f1.readlines()
    temp= f2.readlines()
    x=len(external)

    
    external.sort()
    temp.sort()
  
    for i in temp:
        for j in external:
            if i != j:
                b+=1
            if b==x:
                a.append(i)
        b=0
    
    print(a)
            
    # closing files
    f1.close()                                       
    f2.close()

#-----------

i=0

for i in range(15):
    scanner("$YOUR_PROJECT_FOLDER/external.txt")

removeDubs("$YOUR_PROJECT_FOLDER/external.txt")

for i in range(5):
    
    scanner("$YOUR_PROJECT_FOLDER/temp.txt")
    removeDubs("$YOUR_PROJECT_FOLDER/temp.txt")
    compare()
    sleep(1)


