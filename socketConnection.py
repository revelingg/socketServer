import socket



def socketFinder(ipaddr, startP, endP):
  openPorts = []
  for port in range(startP, endP +1):
    #creates the default socket using the ipv4 protocol and TCP for its connections
    
    socet =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socet.settimeout(5)

    #tries to connect to the ports and returns 0 if its successful
    add = (ipaddr, port)
    port = socet.connect_ex(add)
    if port == 0:
      openPorts.append(port)
      #adds the open ports to the port

      #tries to ping and send a message to the open ports, to ensure the data is all sent and recieved etc

      #if it fails display the error message
      try:
        socet.sendall(b"are we up rn")
        valid = socet.recv(1024)
        print(f"Port {port} is open and valid")
      except socket.error:
        print(f"This port {port} is open although it couldnt be pinged")
    
  socet.close()
  return openPorts
    
def main():
  ipaddr = "10.2.10.22"
  startP = 2000
  endP = 10000
  ports = socketFinder(ipaddr, startP, endP)
  for port in ports:
    
    print(f" This port is open {port}")


main()
