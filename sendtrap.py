import socket
import sys

host = "131.160.163.181"
port = 162

trap = open(sys.argv[1]).read()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.settimeout( 2 )
sock.sendto("%s" %(trap), (host, port))
sock.close()


