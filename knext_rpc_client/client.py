# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname('__file__'), os.path.pardir)))
sys.path.append(os.path.dirname(__file__)+'/../')
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift_gen.py2.knowledge_extraction.ExtractionService import Client
from thrift_gen.py2.knowledge_extraction.ttypes import ExtReq, BadCaseReq

class ExtractionClient(object):
    def __init__(self, host='47.94.210.236', port=9000):
        super(ExtractionClient, self).__init__()
        self._host = host
        self._port = port
        self.tsocket = TSocket.TSocket(self._host, self._port)
        self.transport = TTransport.TBufferedTransport(self.tsocket)
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = Client(self.protocol)

    def get_extraction(self, text, caller='unknown'):
        req = ExtReq(text, caller)
        self.transport.open()
        res = self.client.get_extraction(req)
        self.transport.close()
        kn = res.kn
        res_kn = []
        for k in kn:
            res_kn.append({
                'subject': k.subject,
                'relation': k.relation,
                'object': k.object
            })
        return {
            'text': res.text,
            'kn': res_kn,
            'server_info': res.server_info
        }


if __name__ == '__main__':
    client = ExtractionClient()
    res = client.get_extraction('习近平访问特朗普。高科访问中国。习近平在上海观察。习近平对埃及进行国事访问。')
    print res['kn']