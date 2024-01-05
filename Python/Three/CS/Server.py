import socket
import time





def GatTime():
    # 获取当前时间
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def Sender(msg):
    return ("Server: " + msg).encode('utf-8')


def StartServer():
    Host = '127.0.0.1'
    Port = 9999
    MsgModule = False
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((Host, Port))
    server.listen(5)
    print("\nLog: Server started at {Host}:{Port}".format(
        Host=Host, Port=Port))
    print("Log: Waitting Connect...")
    while True:
        client_socket, client_address = server.accept()

        print("Log: " + str(client_address[0]) +
              ":" + str(client_address[1]) + " connected!")
        try:
            while True:
                data = client_socket.recv(1024)
                msg = data.decode('utf-8')
                if not data:
                    break
                # print("Client: " + msg)
                if MsgModule == True:
                    if msg == "Exit000":
                        MsgModule = False
                        print("Log: MsgModule exited!")
                        client_socket.sendall(Sender("MsgModule exited!"))
                    else:
                        client_socket.sendall(
                            Sender("Message from you: " + msg))
                else:

                    if msg == "Time":
                        print("Log: Time requested!")
                        client_socket.sendall(Sender(GatTime()))
                    elif msg == "MsgM":
                        MsgModule = True
                        print("Log: MsgModule started!")
                        client_socket.sendall(Sender("MsgModule started!"))
                    elif msg == "0":
                        client_socket.sendall(
                            Sender("Close Connection requested!"))
                        print("Log: Close Connection requested!")
                    elif msg == "x":
                        print("Log: Close Server requested!")
                        client_socket.sendall(
                            Sender("Close Server requested!\nServer: Connect Closed!"))
                        client_socket.close()
                        print("Log: All of connection closed!")
                        print("Log: Server Closed!")
                        server.close()
                        exit()

                    else:
                        print("Error: Error Code!")
                        client_socket.sendall(Sender("Error Code!"))
        except socket.timeout:
            pass
        except ConnectionResetError:
            print(
                "Log: " + str(client_address[0]) + ":" + str(client_address[1]) + " was reseted!")
        except Exception as e:
            print("Error: " + e + "!")
        finally:
            print("Log: " + str(client_address[0]) + ":" +
                  str(client_address[1]) + " was disconnected!")
            client_socket.close()


if __name__ == "__main__":
    StartServer()
