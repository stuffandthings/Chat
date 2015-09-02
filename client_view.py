import socket
import sys

def client_view(host, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((host, port))
	sock.sendall('CLIENT VIEW')
	sys.stdout.write(sock.recv(4096))
	print '\n'
	sys.stdout.flush()

	while 1:
		message = sock.recv(4096)
		sys.stdout.write(message)
	
	s.close()

if __name__ == "__main__":
	host = sys.argv[1]
	port = sys.argv[2]
	
	client_view(host, port)