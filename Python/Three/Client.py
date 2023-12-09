import socket

Host = 'localhost'
Port = 5000

MsgModule = False
info = "Client: Please Enter Your Order : "

def RecvP(Client):
    print(Client.recv(1024).decode())


if __name__ == '__main__':

    Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Connect To {H} : {P} ...".format(H=Host, P=Port))
    Client.connect((Host, Port))
    print("Connect Successful!")
    print(
        ''' 
    =========================================
    Order List :
        0 : Close the connection
        1 : Get Time From Server
        2 : Specific message (Type "Eixt" To exit this module)
    =========================================
''')
    while True:
        Input_Data = input(info)
        if Input_Data :
            if MsgModule == True:
                if Input_Data == "Exit":
                    MsgModule = False
                    info = "Client: Please Enter Your Order : "
                    Client.sendall("Exit000".encode())
                    RecvP(Client)
                else:
                    Client.sendall(Input_Data.encode())
                    RecvP(Client)
            else:
                if Input_Data == "1":
                    Client.sendall("Time".encode())
                    RecvP(Client)
                elif Input_Data == "2":
                    MsgModule = True
                    info = "Client: Please Enter Your Message : "
                    Client.sendall("MsgM".encode())
                    RecvP(Client)
                elif Input_Data == "0":
                    Client.close()
                    print("Log: Close Connection!")
                    exit()
                else:
                    Client.sendall(Input_Data.encode())
                    RecvP(Client)
        else:
            print("Error: Not Input anything!")