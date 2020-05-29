import socket


propot = input('proxy server: ')
if len(propot) != 0: #'server4.operamini.com:80'
   proxy  = propot.split(':')[0]
   port   = propot.split(':')[1]

else:
     propot = 'server4.operamini.com:80'
     proxy  = propot.split(':')[0]
     port   = propot.split(':')[1]

bug    = input('bughost: ')


payload = ['CONNECT {} HTTP/1.1\r\nHost: {}\r\n\r\n'.format(propot,bug),'GET {} HTTP/1.1\r\nHost: {}\r\n\r\n'.format(propot,bug)]


def sockcek():
        print ('')
        for pay in payload:
            try:
                   sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                   sock.settimeout(10)
                   sock.connect((proxy,int(port)))
                   sock.sendall(pay.encode())
                   res = sock.recv(9000).decode('utf-8').split('\r\n')
                   print('\n**********succes**********\n{}'.format(repr(pay)))
                   print('\nResponse:')
                   #print(res)
                   for i in res:
                         if '<' in i:break
                         print(i)
            except socket.timeout:
                   print('\n**********timeout**********\n{}'.format(repr(pay)))
            except KeyboardInterrupt:
                   sock.close()
                   exit('bye')
            except Exception as err:print(err)


sockcek()

