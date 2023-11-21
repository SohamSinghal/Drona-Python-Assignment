import socket

receiver_ip = '127.0.0.1'  
receiver_port = 12345 
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    receiver_socket.bind((receiver_ip, receiver_port))
    print("Receiver is ready.")

    receiver_socket.listen(1)

    connection, sender_address = receiver_socket.accept()
    print(f"Connected to sender at {sender_address}")

    while True:
        received_message = connection.recv(1024)
        if not received_message:
            break
        print(f"Received: {received_message.decode()}")

except socket.error as e:
    print(f"Socket error: {e}")

finally:
    connection.close()
    receiver_socket.close()
