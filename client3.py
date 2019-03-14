import  socket

obj=socket.socket()

obj.connect(("127.0.0.1",8080))

ret_s=obj.recv(1024)
ret_str=str(ret_s,encoding="utf-8")
print(ret_str)

while True:
    l=input("please help me ?>>>\n")
    if l=="m":
        break
    else:
        obj.sendall(bytes(l,encoding="utf-8"))
        ret_s=obj.recv(1024)
        ret_str=str(ret_s,encoding="utf-8")
        print(ret_str)
