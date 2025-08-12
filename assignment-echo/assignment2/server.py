import socket, time

HOST, PORT = "127.0.0.1", 5001

def handle(conn):
    data = conn.recv(4096)
    if not data:
        return
    try:
        msg = data.decode("utf-8").rstrip("\r\n")
    except UnicodeDecodeError:
        msg = ""
    stamp = time.strftime("%H:%M:%S")
    reply = f"{msg}|{stamp}\n".encode("utf-8")
    conn.sendall(reply)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        conn, _ = s.accept()
        with conn:
            handle(conn)

if __name__ == "__main__":
    main()
