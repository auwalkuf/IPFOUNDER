import socket
print("use \"exit\" to go back".upper())

'''This is a function that will take a domain name as input and print out the ip address of the domain!'''

def ip_founder(domain):
   
   ip=socket.gethostbyname(domain)
   
   return f"\nThe Ip Address Of {domain} Is [{ip}]"

while True:
        try:
            DomainName=input("\nENTER DOMAIN NAME: ").lower()
            if DomainName=="exit":
                break
                
            print(ip_founder(DomainName))
        except socket.gaierror:
            print("\nINVALID DOMAIN!!")
        
        except KeyboardInterrupt:
           print("\n exiting program")
           
   
