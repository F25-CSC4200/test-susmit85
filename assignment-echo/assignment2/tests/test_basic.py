import re, socket, subprocess, sys, time

HOST, PORT = "127.0.0.1", 5001

def start_server():
    p = subprocess.Popen([sys.executable, "assignment2/server.py"])
    time.sleep(0.5)
    return p

def stop_server(p):
    try:
        p.terminate()
        p.wait(timeout=1)
    except Exception:
        p.kill()

def send(msg):
    with socket.create_connection((HOST, PORT), timeout=2) as s:
        s.sendall((msg + "\n").encode("utf-8"))
        return s.recv(4096).decode("utf-8").strip()

def test_echo_and_time():
    p = start_server()
    try:
        out = send("Hello")
        assert out.startswith("Hello|")
        assert re.search(r"\b\d{2}:\d{2}:\d{2}\b", out)
    finally:
        stop_server(p)

def test_nonascii():
    p = start_server()
    try:
        out = send("こんにちは")
        assert out.startswith("こんにちは|")
    finally:
        stop_server(p)
