import socket
import threading
import sys

class server(threading.Thread):
	def __init__(self, host, port):
		threading.Thread.__init__(self)
		
		self.user_list = {}
		self.host = host
		self.port = port
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((self.host, self.port))
		self.sock.listen(15)
	
	def send_to_all(self, message):
		for usr, conn in self.user_list.iteritems():
			conn.sendall(message)
			
	def client_thread(self, username, connection, address):
		self.user_list[username] = connection
		while 1:
			message = connection.recv(4096)
			msg_to_send = "[" + username + "] " + message
			self.send_to_all(msg_to_send)
		connection.close()
		
	def start_server(self):
		print "Server started!"
		while 1:
			connection, address = self.sock.accept()
			message = connection.recv(4096)
			username = message
			if username in self.user_list:
				connection.sendall("Username already taken.")
			else:
				connection.sendall("Connected as: " + username)
				self.send_to_all(username + " has joined the chat server.")
				threading.Thread(target=self.client_thread, args=(username, connection, address)).start()
		
		self.sock.close()
	
if __name__ == "__main__":
	host = sys.argv[1]
	port = sys.argv[2]
	
	print "Starting server..."
	master_server = server(host, port)
	master_server.start_server()