import socket

receiver_ip = '127.0.0.1'  
receiver_port = 12345  

sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sender_socket.connect((receiver_ip, receiver_port))
    print("Connected to the receiver.")

    while True:
        message = input("Enter message to send (type 'exit' to quit): ")
        sender_socket.sendall(message.encode())

        if message.lower() == 'exit':
            break

except socket.error as e:
    print(f"Socket error: {e}")

finally:
    sender_socket.close()
