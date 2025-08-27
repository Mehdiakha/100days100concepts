import socket

def main():
    
    HOST = "0.0.0.0" # all interfaces
    PORT = 8080 # HTTP

    '''we need to first establish a tcp connection'''
    # create a socket object (ipv4, and tcp type)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #binding a socket endpoint
        s.bind((HOST, PORT))

        #socket listens for connections from clients
        s.listen(5)

        print(f"web server ready to servr...{HOST}:{PORT}")

        while True:
            conn ,addr = s.accept()
            with conn:
                try:
                    print(f"connection accepted by {addr}")
                    data = conn.recv(1024)
                    print(f"data received{data.decode()}")

                    response_body = "Hello Server"
                    response = (
                        "HTTP/1.1 200 OK\r\n"
                        f"Content-Length: {len(response_body)}\r\n"
                        "Content-Type: text/plain\r\n"
                        "Connection: close\r\n"
                        "\r\n"
                        f"{response_body}"
                    )

                    conn.sendall(response.encode("utf-8"))
                    
                    # Force close after sending response
                    print("Closing connection now.")
                    break

                except Exception as e:

                    print(f"Error occurred: {e}")

                    error_response = (
                    "HTTP/1.1 500 Internal Server Error\r\n"
                    "Content-length: 21 \r\n"
                    "\r\n"
                    "500 Internal Server Error"
                    )

                    conn.sendall(error_response.encode('utf-8'))

if __name__ == "__main__":
    main()


