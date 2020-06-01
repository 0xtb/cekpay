import socket
from os import system as cmd

# warna
b='\033[1;34m'
g='\033[2;32m'
pu='\033[1;35m'
cy='\033[1;36m'
r='\033[1;31m'
w='\033[2;37m'
y='\033[2;33m'
bl = '\033[30m'


bnr = '''{}
 _______  _______  ___   _  _______  _______  __   __
|       ||       ||   | | ||       ||   _   ||  | |  |
|       ||    ___||   |_| ||    _  ||  |_|  ||  |_|  |
|       ||   |___ |      _||   |_| ||       ||       |
|      _||    ___||     |_ |    ___||       ||_     _|
|     |_ |   |___ |    _  ||   |    |   _   |  |   |
|_______||_______||___| |_||___|    |__| |__|  |___|

    Github  : https://github.com/bangtebe/cekpay
    Author  : bangtebe
    Tools   : cek bug
    Version : 1.0
'''.format(b)

#print('{}aku\n{}aku\n{}aku\n{}aku\n{}aku\n{}aku\n{}aku'.format(b,g,cy,r,w,y,pu))


class cekaY():
         def __init__(self):
               propot = input('{}proxy server{} :{} '.format(b,r,g))
               if len(propot) != 0:
                   proxy  = propot.split(':')[0]
                   port   = propot.split(':')[1]

               else:
                      propot = 'server4.operamini.com:80'
                      proxy  = propot.split(':')[0]
                      port   = propot.split(':')[1]

               bug    = input('{}bughost      {}:{} '.format(b,r,g))


               payload = {
               'Method Normal':'CONNECT {} HTTP/1.0\r\nHost: {}\r\n\r\n'.format(propot,bug),
               'Method Normal GET':'GET http://{} HTTP/1.1\r\nHost: {}\r\n\r\n'.format(bug,bug),
               'Method Front Inject':'GET http://{}/ HTTP/1.1[crlf]Host: {}\r\n\r\nCONNECT {} HTTP/1.0\r\n\r\n'.format(bug,bug,propot),
               'Method Back Inject':'CONNECT {} HTTP/1.1\r\n\r\nGET http://{}/ HTTP/1.0\r\nHost: {}\r\n\r\n'.format(propot,bug,bug),
               'Method Front Query':'CONNECT {}@{}\r\nGET http://{}/ HTTP/1.0\r\nHost: {}\r\n\r\n'.format(bug,propot,bug,bug),
               'Method Back Query':'CONNECT {}@{}\r\nGET http://{}/ HTTP/1.0\r\nHost: {}\r\n\r\n'.format(propot,bug,bug,bug),
                }

               for pay in payload:
                      try:
                           sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                           sock.settimeout(5)
                           sock.connect((proxy,int(port)))
                           sock.sendall(payload[pay].encode())
                           res = sock.recv(9000).decode('utf-8').split('\r\n')
                           print('\n\n{}[ {}info{} ] {}{}'.format(w,r,w,b,pay))
                           print('{}[ {}info{} ] {}using proxy {}{}{}'.format(w,r,w,b,bl,propot,w))
                           print('\n{}{}'.format(b,repr(payload[pay])))
                           print('\n{}[ {}response {}] {}{}{}'.format(w,r,w,g,res[0],w))
                           '''for i in res:
                                  if '<' in i:break
                                  print(i)'''
                      except socket.timeout:
                                   print('\n\n{}[ {}info{} ] {}{}'.format(w,r,w,b,pay))
                                   print('{}[ {}info{} ] {}using proxy {}{}{}'.format(w,r,w,b,bl,propot,w))
                                   print('\n{}{}'.format(b,repr(payload[pay])))
                                   print('\n{}[ {}response {}] {}TIMEOUT!!{}'.format(w,r,w,r,w))
                      except KeyboardInterrupt:
                                   sock.close()
                                   exit('\n{}bye'.format(r))
                      except Exception as err:print(err)


def main():
       cmd('clear')
       print(bnr)
       cekaY()


if __name__ == '__main__':
  main()
