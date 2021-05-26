import socket

def fast(s_p, e_p, d):
    t = input("pls set time out : ")
    for i in range(int(s_p), int(e_p)):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(int(t))
        c = s.connect_ex((d, i))
        if c == 0 :
            print("the port " + str(i) + " is open in " + d)
        else:
            print("the port " + str(i) + " is close or filter " + d)


