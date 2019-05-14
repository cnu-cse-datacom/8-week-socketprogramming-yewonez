import socket
import os
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 8080))
print("socket bind complete")
data, addr = server_socket.recvfrom(1024)
base=os.path.basename(data.decode())
filesize, addr = server_socket.recvfrom(1024)
filesize = filesize.decode()
filesize = int(filesize)

print("file recv start from ", addr[0])
print(data)
print("File Name : ",base)
print("File Size : ",filesize)

server_socket.sendto("File transmit start...".encode(), addr)

with open(base,'wb') as ttt:
	transffered_data = 0	
	while(True):
		try:
			server_socket.settimeout(5)
			if transffered_data == filesize: break
			received_msg, _ = server_socket.recvfrom(1024)
			transffered_data += len(received_msg)
#			received_msg = received_msg.decode()
			ttt.write(received_msg)
			server_socket.settimeout(None)
			print("current_size / totalsize = ", transffered_data, "/", filesize,",", (transffered_data / filesize) * 100, "%")
		except socket.timeout:
			print("******OCCURED : timeout******")
			break
				

#HOST=''
#PORT=8080
#with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as ss:
#	ss.bind((HOST, PORT))
#	ss.listen(1)
#	conn, addr = ss.accept()
#	with conn:
#		print("Connected by ", addr)
#		data = conn.recv(1024)
#		conn.sendall(data)
