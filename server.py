#!/usr/bin/python
# This runs on the computer(s) you want to read the file from
# Make sure to change out the HOST and PORT variables
# from http://115.28.181.12/en/questions/2c84b5155323dcc56a0e097dee3eddcab6a4f053eb5a560d182b73ddc76a7021/
HOST = '0.0.0.0'
PORT = 8000

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

import time, os


def GetSize(filename):
    # get file size
    return os.stat(filename)[6]


def tail(filename, seek):
    # Set the filename and open the file
    f = open(filename, 'r')

    # Find the size of the file and move to the end
    f.seek(seek)
    return f.read()


def CreateServer():
    # Create server
    server = SimpleXMLRPCServer((HOST, PORT),
                                requestHandler=SimpleXMLRPCRequestHandler)

    # register functions
    server.register_function(tail, 'tail')
    server.register_function(GetSize, 'GetSize')

    # Run the server's main loop
    server.serve_forever()

# start server
CreateServer()