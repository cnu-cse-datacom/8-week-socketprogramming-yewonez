import socket
from time import sleep
from os.path import getsize
FLAGS = None

class SenderSocket():

	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	def socket_send(self):
		HOST = FLAGS.ip
		PORT = FLAGS.port
		
		filename = input("input your file name: ")
		self.socket.connect((HOST,PORT))
		self.socket.sendall(filename.encode())
		filesize = str(getsize(filename))
		self.socket.sendall(filesize.encode())
		filesize = int(filesize)

		data, r = self.socket.recvfrom(1024)
		if not r:
			print("File[%s]: Cannot connect server" %filename)
		
		transffered_data = 0
		with open(filename,'rb') as ssf:
			print(data.decode())
			while(True):
				little_msg = ssf.read(1024)
				if not little_msg: break
				transffered_data += len(little_msg)
				self.socket.sendto(little_msg, (FLAGS.ip,FLAGS.port))
				print("current_size / totalsize = ", transffered_data, "/", filesize,",", (transffered_data / filesize) * 100, "%")

	def main(self):
		self.socket_send()

if __name__=='__main__':
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--ip', type=str, default='localhost')
	parser.add_argument('-p', '--port', type=int, default=8080)

	FLAGS, _= parser.parse_known_args()

	sender_socket = SenderSocket()
	sender_socket.main()
