import socket
import uuid
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
MAC = uuid.getnode()
print(" IP:", ip, "\n", "MAC:", MAC)

for ab in range(100):
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")