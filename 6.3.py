import socket
import sys
import time
import errno
import math
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 NotFound\n\n'

def process_start(s_sock,s_addr):
    s_sock.send(str.encode('Welcome to the server\n'))
    while True:
        data = str(s_sock.recv(2048).decode())
        op,val,val2 = data.split('.')
        if op == "log":
            print(str(s_addr) + " has choosen Log Function")
            line = "\n_______________________________________________________________\n"
            
            answer = "Log " + val + " with base " + val2 + " is : " + str(math.log(int(val),int(val2))) + line
            s_sock.send(str.encode(answer))
        elif op == "pow":
            print(str(s_addr) + " has choosen Power Function")
            line = "\n_______________________________________________________________\n"
            answer = "The value of " + val + " to the power of " + val2 + " is : " + str(math.pow(int(val),int(val2))) + line
            s_sock.send(str.encode(answer))
        elif op == "sq":
            print(str(s_addr) + " has choosen Square Root Function")
            line = "\n_______________________________________________________________\n"
            answer = "The Value of Square root of " + val + " is : " + str(math.sqrt(int(val))) + line
            s_sock.send(str.encode(answer))
        elif op == "exp":
            print(str(s_addr) + " has choosen Exponential Function")
            line = "\n_______________________________________________________________\n"
            answer = "The Value of Exponential of " + val + " is : " + str(math.exp(int(val))) + line
            s_sock.send(str.encode(answer))
        elif op == "ter":
            s_sock.close()
             
    s_sock.close()
        

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,s_addr))
                p.start()

            except socket.error:

                print('got a socket error')

    except Exception as e:        
        print('an exception occurred!')
        print(e)
        sys.exit(1)
    finally:
     	s.close()
