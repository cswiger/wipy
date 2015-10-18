import usocket as socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ai = socket.getaddrinfo("192.168.1.119", 8080)
print("Address infos:", ai)
addr = ai[0][4]

print("Connect address:", addr)
s.connect(addr)

# intended for fixed point 2 decimal places celcius
temp = 438  
# using a home installation of Phant - or use data.sparkfun.com
# http://192.168.1.119:8080/input/6WyWwGEg4yTq2ey3AjQEh6PogQxb.json?private_key=............................&data1=468
u = bytes('GET /input/6WyWwGEg4yTq2ey3AjQEh6PogQxb.json?private_key=............................&data1={} HTTP/1.0\n\n'.format(temp),'ascii')

s.sendall(u)
print(s.recv(4096))
s.close()

