import socket

def slow(host, timeout):
    for i in range(1, 1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        ht = s.connect_ex((host, i))
        if ht == 0 :
            print("the port " + str(i) + " is open in " + host)
        else :
            print("the port " + str(i) + " is close or filter in " + host)
        
