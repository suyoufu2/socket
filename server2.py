import  socket
#服务端
sk=socket.socket()#创建socket对象
sk.bind(("127.0.0.1",8080))#绑定ip地址和端口
sk.listen(5)#监听该端口号

while True:
    conn,address=sk.accept()#接收来自客户端的请求连接和地址号
    conn.sendall("欢迎光临，我是AI",encoding="utf-8")
    size=conn.recv(1024)#从socket中读取字符,最多能接收1024字符
    size_str=str(size,encoding="utf-8")
    file_size=int(size_str)
    conn.sendall(bytes("开始传送",encoding="utf-8"))
    has_size=0
    f=open("1.png","wb")
    while True:
        if file_size == has_size:
            break
        data=conn.recv(1024)
        f.write(data)
        has_size+=len(data)
    f.close()