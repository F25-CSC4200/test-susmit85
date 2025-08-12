import socket, sys

HOST, PORT = "127.0.0.1", 5001

def main():
    msg = sys.argv[1] if len(sys.argv) > 1 else "Hello"
    with socket.create_connection((HOST, PORT), timeout=2) as s:
        s.sendall((msg + "\n").encode("utf-8"))
        data = s.recv(4096).decode("utf-8")
        print(data.strip())

if __name__ == "__main__":
    main()
