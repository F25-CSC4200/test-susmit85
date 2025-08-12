# Assignment 2: TCP Echo Server/Client

**Goal:** Implement a TCP server and client where the server echoes the message plus a timestamp.

## Requirements
- Server binds to 127.0.0.1:5001
- Server reads one line from client and replies `<payload>|<HH:MM:SS>`
- Client sends a message from command line and prints server reply

Run server:
```bash
python assignment2/server.py
```

Run client:
```bash
python assignment2/client.py "Hello"
```

Run tests:
```bash
pytest assignment2/tests/test_basic.py
```
