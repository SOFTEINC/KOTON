import socket, time, ping, speed, slow, fast

print("""

install this modules (socket, time, speedtest)

[*] 1- ping scan            2- port scan


[*] 3- speed test           4- exit



""")


insert = input("Option > ")

if insert == "1" :
    host = input("pls insert host > ")
    print()
    timeout = input("pls insert time out > ")
    print()
    ping.ping(host, int(timeout))
elif insert == "2" :
    print("""

    [*] 1- fast mode (in the range)             2- slow mode (range 1:1000)

    
    """)
    i2 = input("Option > ")
    if i2 == "1" :
        print()
        start = input("pls insert start port > ")
        print()
        end = input("pls insert end port > ")
        print()
        host_1 = input("pls insert host > ")
        print()
        timeout_1 = input("pls insert time out > ")
        print()
        fast.fast(int(start), int(end), host_1, int(timeout_1))
    elif i2 == "2" :
        print()
        host_2 = input("pls insert host > ")
        print()
        timeout_2 = input("pls insert time out > ")
        print()
        slow.slow(host_2, int(timeout_2))
        print()
    else :
        print("insert the corect option ")
        exit()
elif insert == "3" :
    speed.speed()
elif insert == "4" :
    exit()
