import socket
import time


Host = '127.0.0.1'
Port = 5000
MsgModule = False
SendMsg = "Server: "


def GatTime():
    # 获取当前时间
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def Sender(msg):
    return ("Server: "+ msg).encode('utf-8')


if __name__ == "__main__":

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((Host, Port))
    server.listen(5)
    print("\nLog: Server started at {Host}:{Port}".format(Host=Host, Port=Port))

    SendMsg = "Server: "
    print("Log: Waitting Connect...")
    while True:
        client_socket, client_address = server.accept()
        print(f"客户端 {client_socket.fileno()} 已连接")

        try:
            while True:
                data = client_socket.recv(1024)
                msg = data.decode('utf-8')
                if not data:
                    break
                print("Client: " + msg)
                if MsgModule == True:
                    if msg == "Exit000":
                        MsgModule = False
                        print("Log: MsgModule exited!")
                        client_socket.sendall(Sender("MsgModule exited!"))
                    else:
                        client_socket.sendall(Sender("Message from you: " + msg))
                else:
                    if msg == "Time":
                        print("Log: Time requested!")
                        client_socket.sendall(Sender(GatTime()))
                    elif msg == "MsgM":
                        MsgModule = True
                        print("Log: MsgModule started!")
                        client_socket.sendall(Sender("MsgModule started!"))
                    else:
                        print("Error: Error Code!")
                        client_socket.sendall(Sender("Error Code!"))
        except socket.timeout:
            pass
        except ConnectionResetError:
            print(f"客户端 {client_socket.fileno()} 被重置")
        except Exception as e:
            print(f"发生错误: {e}")
        finally:
            print(f"客户端 {client_socket.fileno()} 已断开连接")
            client_socket.close()