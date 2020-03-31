# -*- coding: utf-8 -*-

import os
import sys
import re
import json
cur_path =os.path.abspath(os.path.join(os.path.dirname('__file__'), os.path.pardir))
sys.path.append(cur_path)
sys.path.append(os.path.dirname(__file__)+'/../')

from thrift_gen.py3.knowledge_extraction import ExtractionService
from thrift_gen.py3.knowledge_extraction.ttypes import ExtReq, ExtRsp, BadCaseReq, BadCaseRsp, Knowledge
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from knext_rpc_server.extraction_libs.open_entity_relation_extraction.code.core.nlp import NLP
from knext_rpc_server.extraction_libs.open_entity_relation_extraction.code.core.extractor import Extractor


__HOST = 'localhost'
__PORT = 9000


class ExtractionHandler(object):
    def __init__(self):
        self.nlp = NLP()
        self.extractor = Extractor()
        
    def get_sentences(self, text):
        return re.split('[。？！；]|\n', text)
    
    def handle(self, lines, outpath):
        if os.path.isfile(outpath):
            os.remove(outpath)
        for line in lines:
            # 卡句子长度
            if len(line) < 6:
                continue
            # 分词
            lemmas = self.nlp.segment(line)

            # 词性标注
            postags = self.nlp.postag(lemmas)

            # 命名实体识别
            netags = self.nlp.netag(postags)

            # 依存句法分析
            sentence = self.nlp.parse(netags)

            # 抽取三元组
            self.extractor.extract(line, sentence, outpath, 1)

        res = []
        with open(outpath, 'r') as f:
            for line in f.readlines():
                kn = json.loads(line)
                if len(kn.get('knowledge',[])) == 3:
                    res.append(Knowledge(kn[0], kn[1], kn[2]))
        
        return res
            
    
    def get_extraction(self, req):
        rsp = ExtRsp()
        rsp.text = req.text
        rsp.server_info = '47.94.210.236'
        #FIXME: 调用模型获取kn
        rsp.kn = self.handle(req.text, 'out/1.txt')
        
        return rsp
    
    def set_badcase(self, req):
        return BadCaseRsp('ok', '47.94.210.236')

if __name__ == '__main__':
    handler = ExtractionHandler()

    processor = ExtractionService.Processor(handler)
    transport = TSocket.TServerSocket(__HOST, __PORT)
    # 传输方式，使用buffer
    tfactory = TTransport.TBufferedTransportFactory()
    # 传输的数据类型：二进制
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # 创建一个thrift 服务
    rpcServer = TServer.TSimpleServer(processor,transport, tfactory, pfactory)

    print('Starting the rpc server at', __HOST,':', __PORT)
    rpcServer.serve()
    print('done')