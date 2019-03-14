import  socket
import  os

obj=socket.socket()
obj.connect(("127.0.0.1",8080))#连接socket
ret_bytes=obj.recv(1024)
ret_str=str(ret_bytes,encoding="utf-8")

print(ret_str)

size=os.stat("2.jpg").st_size

obj.sendall(bytes(str(size),encoding="utf-8"))

obj.recv(1024)
print("=========================")
with open("2.jpg","rb") as f:
    for line in f:
        obj.sendall(line)