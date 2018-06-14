from struct import pack, unpack
from thrift.Thrift import TException
from thrift.transport.TTransport import *

class TFileTransport(TTransportBase, CReadableTransport):

    def __init__(self, fileName):
        self.fileName = fileName

    def isOpen(self):
        pass

    def open(self):
        self.fp = file(self.fileName, "wb")

    def close(self):
        self.fp.close()

    def read(self, sz):
        pass

    def write(self, buf):
        self.fp.write(buf)

    def flush(self):
        pass

    def getvalue(self):
        pass
