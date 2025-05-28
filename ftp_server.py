from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer

def run_ftp_server():
    authorizer = DummyAuthorizer()
    # Add user: username='ftpuser', password='ftp'
    authorizer.add_user("ftpuser", "ftp", ".", perm="elradfmw")
    # Optional: allow anonymous access
    authorizer.add_anonymous(".", perm="elr")

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(("0.0.0.0", 2122), handler)
    print("FTP Server started on port 2122...")
    server.serve_forever()

if __name__ == "__main__":
    run_ftp_server()
