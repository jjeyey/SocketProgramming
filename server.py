// 문자 하나를 처리하는 소켓 프로그래밍의 클라이언트 서버 코드임.

import socket

# 서버 설정
HOST = '127.0.0.1'
PORT = 8889

# 소켓 생성 및 연결
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

# 클라이언트로부터 연결 요청이 올 때까지 대기
print('서버 대기 중...')
client_socket, addr = server_socket.accept()
print('Connected by', addr)

while True:
    # 클라이언트로부터 데이터 받아옴
    data = client_socket.recv(1024)

    if not data:
        # 데이터가 없으면 연결 종료
        break

    # bytes를 str 타입으로 변환 후, 다시 bytes 타입으로 변환하여 ord 함수 적용
    data_str = data.decode('utf-8')
    data_ascii = ord(data_str)

    # 변환된 아스키 코드 값을 클라이언트로 전송
    client_socket.sendall(str(data_ascii).encode('utf-8'))

    # 서버 측에서 전송된 아스키 코드 값을 출력
    print('Received ASCII code:', data_ascii)

# 소켓 연결 종료
client_socket.close()
server_socket.close()
