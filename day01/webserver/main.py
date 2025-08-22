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

        while True:
            
            print('web server ready to serve ...')

            #establish a connection
            conn, addr = s.accept()

            try:
                print(f"connected by addr: {addr}")
                data = conn.recv(1024)
                print(f"received: {data.decode()}")
                

                response_body = "Hello World"
                response = "HTTP/1.1 200 OK \r\n"
                f"Content-length: {len(response_body)}\r\n"
                "\r\n"
                f"{response_body}"

                conn.sendall(response.encode("utf-8"))

            except Exception as e:
                
                print(f"Error: {e}")

                "HTTP/1.1 500 Internal Server Error\r\n"
                "Content-length: 21\r\n"
                "\r\n"
                "5OO Internal Server Error"


if __name__ == "__main__":
    main()


