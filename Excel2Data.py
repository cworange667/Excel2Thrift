import sys
import glob
sys.path.append('gen-py')


from thrift import Thrift

from pathfinding.ttypes import *  
from ExcelBase.ttypes import *  

from TFileTransport import TFileTransport  
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol



transport = TFileTransport("testData.bytes")
protocol = TBinaryProtocol.TBinaryProtocol(transport)

pf = pathfinding()
pf.id = 1000

pf.content = []
ele = tpv(1,2,3)
pf.content.append(ele)

print pf.content[0].type
print pf.content[0].param
print pf.content[0].val

pf.position = [1]
pf.position[0] = tpv()
pf.position[0].type = 5
pf.position[0].param = 6
pf.position[0].val = 7


transport.open()
pf.write(protocol)
transport.close()
