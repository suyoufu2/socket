import  socketserver
#服务端

class Myserver(socketserver.BaseRequestHandler):

    def handle(self):
        conn = self.request#连接请求
        #以字节的形式向socket
        conn.sendall(bytes("你好，我是机器人",encoding="utf-8"))
        while True:
            ret_bytes = conn.recv(1024)
            ret_str = str(ret_bytes,encoding="utf-8")
            if ret_str == "q":
                break
            if ret_str=="请问你是":
                conn.sendall( bytes("我是机器人，请问您需要什么帮助吗？",encoding="utf-8"))
            if ret_str=="我需要你的帮助":
                conn.sendall(bytes( "好的，很高兴为你服务，小AI帮你解决各类小问题", encoding="utf-8"))
            conn.sendall(bytes("您好，您可以询问的问题有：请问你是，我需要你的帮助",encoding="utf-8"))

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("127.0.0.1",8080),Myserver)
    server.serve_forever()#server.close()