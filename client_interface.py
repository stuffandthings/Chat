import socket
import sys

def client_interface(username, host, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((host, port))
	sock.sendall(username)
	received = sock.recv(4096)
	sys.stdout.write(received)
	sys.stdout.flush()
	print '\n'
	
	while 1:
		sys.stdout.write("["+username+"] ")
		sys.stdout.flush()
		msg_to_send = sys.stdin.readline()
		sock.sendall(msg_to_send)
	
	sock.close()
	
if __name__ == "__main__":
	username = sys.argv[1]
	host = sys.argv[2]
	port = sys.argv[3]
	
	client_interface(username, host, port)
	