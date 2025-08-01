import socket
import click

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

MESSAGE = "Hello from pingport, running on host {h} at port {p}"


# TODO: add TCP/UDP flag
# TODO: add IPv4 vs IPv6
@click.command()
@click.option("--host", default=HOST, type=str, required=False, help="host for server")
@click.option("--port", default=PORT, type=int, required=False, help="port for server")
def start_server(host: str, port: int) -> None:
    print(f"Starting pingport server on {host} at {port} ...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                conn.sendall(MESSAGE.format(h=host, p=port))
