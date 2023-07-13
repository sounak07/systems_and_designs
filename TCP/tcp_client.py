import socket
import logging


def client_server() -> socket.socket:
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_add = ("localhost", 9991)
    socket_client.connect(server_add)

    return socket_client


def send_msg():
    socket_conn = client_server()
    msg = ""
    try:
        while msg != "STOP":
            msg = input("Enter your message : ")
            socket_conn.sendall(msg.encode("utf-8"))
            response = socket_conn.recv(1024)
            print("Received response: {}".format(response.decode("utf-8")))
    except Exception as e:
        print(f"Error Client : {e}")
    finally:
        socket_conn.close()


if __name__ == "__main__":
    send_msg()
