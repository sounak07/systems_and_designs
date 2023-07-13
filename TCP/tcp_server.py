import socket


def client_server() -> socket.socket:
    socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_add = ("localhost", 9991)
    socket_conn.bind(server_add)
    socket_conn.listen(5)
    print(f"Server is running {server_add}")
    return socket_conn


def receive_msg():
    client_socket = None
    try:
        socket_server = client_server()
        client_socket, _ = socket_server.accept()
        while True:
            rec_data = client_socket.recv(1024)
            print("Received response: {}".format(rec_data.decode("utf-8")))
            send_msg = "Server says Hi, message received"
            client_socket.sendall(send_msg.encode("utf-8"))
    except Exception as e:
        print(f"Error Server : {e}")
    finally:
        client_socket.close()


if __name__ == "__main__":
    receive_msg()
