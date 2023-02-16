# Proxy Server
from socket import *
import time as t

server = socket() # create the socket by default

default_port = 6900 # As I searched, I can use some ports in limited range, so I chose 6900 randomly
# It is acceptable. I used this source:
# https://www.sciencedirect.com/topics/computer-science/registered-port#:~:text=Ports%200%20through%201023%20are,be%20used%20dynamically%20by%20applications.

host = gethostname() # getting the host which is the laptop that the server code is running on
IP_add = gethostbyname(host) # getting the IP address from the host 
# I learned about gethostname() and gethostbyname() from this from this source:
# https://manpages.ubuntu.com/manpages/jammy/man1/sge_hostnameutils.1.html#:~:text=gethostname%20and%20gethostbyname%20are%20used,address%20(dotted%20decimal%20notation).

server.bind((IP_add,default_port)) # binding 


server.listen(1) # server begins listening for incoming TCP requests


client,addr = server.accept() # server waits on accept for incoming requests
# A new socket is also created on return

request = client.recv(4096).decode() # read the bytes

temp = request # saving the request in another variable

IP_address = temp.split()[4]  # getting the IP address form the user input knowing it is the fifth word for sure

print("Received the request from client. IP address is:",IP_address,"at time:",t.ctime())   
# For getting the exact time, I used this source to learn about it:
# https://www.geeksforgeeks.org/python-time-ctime-method/

destination = socket() # creating the destination server

try:
    destination.connect((IP_address,80)) # port 80 is famous for hosting HTTP services
    print("Sending the client's request to the destination server at time:",t.ctime())
    destination.send(request.encode()) # sending to the destination server
except error: # in case we got an error
    E = "Error! Could not reach the destination server." # error message
    client.send(E.encode()) # sending it encoded
    print(E) # printing the error on the server also

response = destination.recv(4096).decode() #receiving the response from destination
print("The response was received at time:",t.ctime())

client.send(response.encode()) # sending the response back to the client
print("The response is sent to the client at time:",t.ctime())

destination.close() # closing the destination socket
server.close()  # closing the server socket


    
     
        
        
    
    
