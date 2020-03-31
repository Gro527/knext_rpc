# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname('__file__'), os.path.pardir)))
sys.path.append(os.path.dirname(__file__)+'/../')
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift_gen.py3.knowledge_extraction.ExtractionService import Client
from thrift_gen.py3.knowledge_extraction.ttypes import ExtReq, BadCaseReq


__HOST = 'localhost'
__PORT = 9000



tsocket = TSocket.TSocket(__HOST, __PORT)
transport = TTransport.TBufferedTransport(tsocket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = Client(protocol)

req = ExtReq('习近平访问特朗普。','guhaoping')
transport.open()
print('client-requets')
res = client.get_extraction(req)
# print(client.do_format(data).text)
print('server-answer', res)

transport.close()