import socket

# 서버 설정
HOST = '127.0.0.1'
PORT = 8889

# 소켓 생성 및 연결
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    # 사용자로부터 문자열 입력받음
    send_data = input('보낼 문자열을 입력하세요 (종료하려면 q를 입력하세요): ')

    if send_data == 'q':
        # q를 입력하면 종료
        break

    # 문자열을 서버로 전송
    client_socket.sendall(send_data.encode())

    # 서버에서 받은 데이터 출력
    received_data = client_socket.recv(1024)
    data_ascii = int(received_data.decode('utf-8'))
    print('Received ASCII code:', data_ascii)

# 소켓 연결 종료
client_socket.close()
