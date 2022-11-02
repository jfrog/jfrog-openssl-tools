import socket
import ssl
import sys
import warnings
import enum

warnings.filterwarnings("ignore", category=DeprecationWarning)


TIMEOUT = 0.2


class Diag(enum.Enum):
    Error = -1
    Cert_not_required = 0
    Cert_required = 1


def check_server(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client = ssl.wrap_socket(client)

    try:
        client.connect((host, port))
    except Exception as e:
        print(e)
        return Diag.Error

    client.settimeout(TIMEOUT)
    try:
        client.read(1)

    except ssl.SSLError as err:
        if "CERTIFICATE_REQUIRED" in str(err):
            return Diag.Cert_required
    except TimeoutError:
        return Diag.Cert_not_required

    except Exception as e:
        return Diag.Error

    return Diag.Cert_not_required


def finding_report(host, port, status):
    res_string = {
        Diag.Cert_not_required: "Client certificate not required",
        Diag.Cert_required: "Client certificate required!",
        Diag.Error: "Could not connect",
    }
    print(f"{host}:{port} -> {res_string[status]}")


if __name__ == "__main__":
    try:
        host = sys.argv[1]
        port = int(sys.argv[2])
    except:
        print(f"Usage: {sys.argv[0]} <HOST_IP> <PORT>")
        exit(-1)
    res = check_server(host, port)
    finding_report(host, port, res)
    exit(0 if res == Diag.Cert_not_required else -1)
