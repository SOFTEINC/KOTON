import socket

def fast(s_p, e_p, d, t):
    for i in range(s_p, e_p):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(t)
        c = s.connect_ex((d, i))
        if c == 0 :
            print("the port " + str(i) + " is open in " + d)
        else:
            print("the port " + str(i) + " is close or filter " + d)
