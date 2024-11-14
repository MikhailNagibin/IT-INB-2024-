print('IP:', socket.gethostbyname(socket.gethostname()))
mac = ':'.join(['{:02x}'.format((getnode() >> elements) & 0xff) for elements in range(0, 2*6, 2)][::-1]).upper()
print('MAC:', mac)