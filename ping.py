import socket, time

def ping(host, timeout):
    while True :
        t = time.time()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        th = s.connect_ex((host, 80))
        if th == 0 :
            print("ping in " + host + " is up Time = " + str(t))
        else :
            print("Error in connection")
            exit()

