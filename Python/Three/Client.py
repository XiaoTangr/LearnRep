import socket




def RecvP(Client):
    print(Client.recv(1024).decode())


def StartClient():
    

    Host = 'localhost'
    Port = 5000

    MsgModule = False


    sureinfo = '''
======================================================
=   Are You Sure to Close Server?                    =
=   This will disconnect and cannot be recovered!    =
=----------------------------------------------------=
=      'Y' to Sure      |      'N' to cancel.        =
======================================================
'''

    startInfo = ''' 
=====================================================================
=    Order List :                                                   =
=        0 : Close the connection                                   =
=        1 : Get Time From Server                                   =
=        2 : Specific message (Type "Eixt" To exit this module)     =
=        x : Close Server!                                          =
=====================================================================
'''



    info = "Client: Please Enter Your Order : "


    Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    print("Log: Connect To {H} : {P} ...".format(H=Host, P=Port))
    Client.connect((Host, Port))
    print("Log: Connect Successful!")
    print(startInfo)
    while True:
        Input_Data = input(info)
        if Input_Data:
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
                    Client.sendall("0".encode())
                    RecvP(Client)
                    print("Info: Connect closed!")
                    print("Client: Exitting...")
                    Client.close()
                    exit()
                elif Input_Data == "x":
                    print(sureinfo)
                    sure = input("Y/N: ")
                    if sure == "Y":
                        Client.sendall("x".encode())
                        RecvP(Client)
                        print("Info: Connect closed!")
                        print("Client: Exitting...")
                        Client.close()
                        exit()
                    elif sure == "N":
                        print("Log: Operation Cancel!")
                    else:
                        print("Error: Error Word!(Operation Cancel!)")
                else:
                    Client.sendall(Input_Data.encode())
                    RecvP(Client)
        else:
            print("Error: Not Input anything!")


if __name__ == '__main__':
    StartClient()