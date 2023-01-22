import socket

def port_scan(host, port_range):
    for port in range(port_range[0], port_range[1]):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f'Port {port} is open')
        else:
            print(f'Port {port} is closed')
        sock.close()

port_scan('192.168.127.48', (1, 65535))
