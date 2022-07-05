# Import the mock server
from xylophone.server.server import MockXyloServer

# Instantiate the mock server and specify the IP/host and port that it's going to be using.
server = MockXyloServer(host='localhost', port=8080)

# Just start the server
server.start()