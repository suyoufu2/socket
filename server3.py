import  socketserver

class Myserver(socketserver.BaseRequestHandler):

    def handle(self):
        conn=self.request()
        conn.sendall(bytes("你好，请问需要什么帮助",encoding="utf-8"))
        while True:
            t_bytes = conn.recv(1024)
            t_str=str(t_bytes,encoding="utf-8")
            if t_str=="m":
                break
            conn.sendall(bytes(t_str+"hello sir",encoding="utf-8"))
if __name__ =="__main__":
    server=socketserver.ThreadingTCPServer(("127.0.0.1",8080),Myserver)
    server.serve_forever()