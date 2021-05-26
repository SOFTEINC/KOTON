import fast_mode
import socket


print("""

1 : fast mode

2 : slow mode

""")

f_s = int(input("select (fast / slow) mode >> "))

if f_s == 2 :
    domain = input("pls input domain name >> ")

    start = 1

    end = 1000

    time = input("pls insert time out : ")

    for i in range(start, end):
        connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect.settimeout(int(time))
        ooc = connect.connect_ex((domain, i))
        if ooc == 0 :
            print("the port " + str(i) + " open in " + domain)
        else:
            print("the port " + str(i) + " close or filter in " + domain)
elif f_s == 1  :
    s_p = input("pls insert start port : ")
    e_p = input("pls insert end port : ")
    d = input("pls input domain name >> ")
    fast_mode.fast(s_p, e_p, d)

