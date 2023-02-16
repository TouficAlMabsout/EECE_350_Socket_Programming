# Client
from socket import *
import time as t
import uuid # to get the MAC address (later in the code I will put the source)

n = str(input("Enter the IP address of the website you want to access: ")) # get the website IP address

client = socket() # create the socket by default
default_port = 6900 # the port I am using (explained in server code)
host=gethostname() # explained in server code
IP_address = gethostbyname(host) # explained in server code
client.connect((IP_address,default_port)) # connecting to the proxy server

request = "GET / HTTP/1.1\r\nHost: "+n+"\r\n\r\n" # this is the request that I will send
# it follows this syntax according to the example on moodle

start = t.time() # starting time to measure later on the RTT

print("The request to open",n,"is:",request,"It is sent to the server at time:",t.ctime())
client.send(request.encode()) # sending the request

reply = client.recv(4096).decode() # getting the reply back from the proxy server
print("The response is received from the server. The response is:",reply+".","It is received at time:",t.ctime())

end = t.time() # end time
delta = round(end-start,2) # the RTT

client.close() # closing the socket

print("The total round-trip time is:",delta,"seconds.")

MAC_address = uuid.getnode() # method to get the MAC address
# I used this source to learn about it:
# https://www.geeksforgeeks.org/extracting-mac-address-using-python/

print("MAC address is:",MAC_address)









        