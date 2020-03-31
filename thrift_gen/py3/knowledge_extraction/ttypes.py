#
# Autogenerated by Thrift Compiler (0.13.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class ExtReq(object):
    """
    Attributes:
     - text
     - caller

    """


    def __init__(self, text=None, caller=None,):
        self.text = text
        self.caller = caller

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.text = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 255:
                if ftype == TType.STRING:
                    self.caller = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ExtReq')
        if self.text is not None:
            oprot.writeFieldBegin('text', TType.STRING, 1)
            oprot.writeString(self.text.encode('utf-8') if sys.version_info[0] == 2 else self.text)
            oprot.writeFieldEnd()
        if self.caller is not None:
            oprot.writeFieldBegin('caller', TType.STRING, 255)
            oprot.writeString(self.caller.encode('utf-8') if sys.version_info[0] == 2 else self.caller)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.text is None:
            raise TProtocolException(message='Required field text is unset!')
        if self.caller is None:
            raise TProtocolException(message='Required field caller is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Knowledge(object):
    """
    Attributes:
     - subject
     - relation
     - object

    """


    def __init__(self, subject=None, relation=None, object=None,):
        self.subject = subject
        self.relation = relation
        self.object = object

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.subject = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.relation = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.object = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Knowledge')
        if self.subject is not None:
            oprot.writeFieldBegin('subject', TType.STRING, 1)
            oprot.writeString(self.subject.encode('utf-8') if sys.version_info[0] == 2 else self.subject)
            oprot.writeFieldEnd()
        if self.relation is not None:
            oprot.writeFieldBegin('relation', TType.STRING, 2)
            oprot.writeString(self.relation.encode('utf-8') if sys.version_info[0] == 2 else self.relation)
            oprot.writeFieldEnd()
        if self.object is not None:
            oprot.writeFieldBegin('object', TType.STRING, 3)
            oprot.writeString(self.object.encode('utf-8') if sys.version_info[0] == 2 else self.object)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.subject is None:
            raise TProtocolException(message='Required field subject is unset!')
        if self.relation is None:
            raise TProtocolException(message='Required field relation is unset!')
        if self.object is None:
            raise TProtocolException(message='Required field object is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ExtRsp(object):
    """
    Attributes:
     - text
     - kn
     - server_info

    """


    def __init__(self, text=None, kn=None, server_info=None,):
        self.text = text
        self.kn = kn
        self.server_info = server_info

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.text = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.kn = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = Knowledge()
                        _elem5.read(iprot)
                        self.kn.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 255:
                if ftype == TType.STRING:
                    self.server_info = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ExtRsp')
        if self.text is not None:
            oprot.writeFieldBegin('text', TType.STRING, 1)
            oprot.writeString(self.text.encode('utf-8') if sys.version_info[0] == 2 else self.text)
            oprot.writeFieldEnd()
        if self.kn is not None:
            oprot.writeFieldBegin('kn', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.kn))
            for iter6 in self.kn:
                iter6.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.server_info is not None:
            oprot.writeFieldBegin('server_info', TType.STRING, 255)
            oprot.writeString(self.server_info.encode('utf-8') if sys.version_info[0] == 2 else self.server_info)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.text is None:
            raise TProtocolException(message='Required field text is unset!')
        if self.kn is None:
            raise TProtocolException(message='Required field kn is unset!')
        if self.server_info is None:
            raise TProtocolException(message='Required field server_info is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class BadCaseReq(object):
    """
    Attributes:
     - badcases
     - caller

    """


    def __init__(self, badcases=None, caller=None,):
        self.badcases = badcases
        self.caller = caller

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.badcases = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in range(_size7):
                        _elem12 = Knowledge()
                        _elem12.read(iprot)
                        self.badcases.append(_elem12)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 255:
                if ftype == TType.STRING:
                    self.caller = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('BadCaseReq')
        if self.badcases is not None:
            oprot.writeFieldBegin('badcases', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.badcases))
            for iter13 in self.badcases:
                iter13.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.caller is not None:
            oprot.writeFieldBegin('caller', TType.STRING, 255)
            oprot.writeString(self.caller.encode('utf-8') if sys.version_info[0] == 2 else self.caller)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.badcases is None:
            raise TProtocolException(message='Required field badcases is unset!')
        if self.caller is None:
            raise TProtocolException(message='Required field caller is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class BadCaseRsp(object):
    """
    Attributes:
     - retcode
     - server_info

    """


    def __init__(self, retcode=None, server_info=None,):
        self.retcode = retcode
        self.server_info = server_info

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.retcode = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 255:
                if ftype == TType.STRING:
                    self.server_info = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('BadCaseRsp')
        if self.retcode is not None:
            oprot.writeFieldBegin('retcode', TType.STRING, 1)
            oprot.writeBinary(self.retcode)
            oprot.writeFieldEnd()
        if self.server_info is not None:
            oprot.writeFieldBegin('server_info', TType.STRING, 255)
            oprot.writeString(self.server_info.encode('utf-8') if sys.version_info[0] == 2 else self.server_info)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.retcode is None:
            raise TProtocolException(message='Required field retcode is unset!')
        if self.server_info is None:
            raise TProtocolException(message='Required field server_info is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(ExtReq)
ExtReq.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'text', 'UTF8', None, ),  # 1
    None,  # 2
    None,  # 3
    None,  # 4
    None,  # 5
    None,  # 6
    None,  # 7
    None,  # 8
    None,  # 9
    None,  # 10
    None,  # 11
    None,  # 12
    None,  # 13
    None,  # 14
    None,  # 15
    None,  # 16
    None,  # 17
    None,  # 18
    None,  # 19
    None,  # 20
    None,  # 21
    None,  # 22
    None,  # 23
    None,  # 24
    None,  # 25
    None,  # 26
    None,  # 27
    None,  # 28
    None,  # 29
    None,  # 30
    None,  # 31
    None,  # 32
    None,  # 33
    None,  # 34
    None,  # 35
    None,  # 36
    None,  # 37
    None,  # 38
    None,  # 39
    None,  # 40
    None,  # 41
    None,  # 42
    None,  # 43
    None,  # 44
    None,  # 45
    None,  # 46
    None,  # 47
    None,  # 48
    None,  # 49
    None,  # 50
    None,  # 51
    None,  # 52
    None,  # 53
    None,  # 54
    None,  # 55
    None,  # 56
    None,  # 57
    None,  # 58
    None,  # 59
    None,  # 60
    None,  # 61
    None,  # 62
    None,  # 63
    None,  # 64
    None,  # 65
    None,  # 66
    None,  # 67
    None,  # 68
    None,  # 69
    None,  # 70
    None,  # 71
    None,  # 72
    None,  # 73
    None,  # 74
    None,  # 75
    None,  # 76
    None,  # 77
    None,  # 78
    None,  # 79
    None,  # 80
    None,  # 81
    None,  # 82
    None,  # 83
    None,  # 84
    None,  # 85
    None,  # 86
    None,  # 87
    None,  # 88
    None,  # 89
    None,  # 90
    None,  # 91
    None,  # 92
    None,  # 93
    None,  # 94
    None,  # 95
    None,  # 96
    None,  # 97
    None,  # 98
    None,  # 99
    None,  # 100
    None,  # 101
    None,  # 102
    None,  # 103
    None,  # 104
    None,  # 105
    None,  # 106
    None,  # 107
    None,  # 108
    None,  # 109
    None,  # 110
    None,  # 111
    None,  # 112
    None,  # 113
    None,  # 114
    None,  # 115
    None,  # 116
    None,  # 117
    None,  # 118
    None,  # 119
    None,  # 120
    None,  # 121
    None,  # 122
    None,  # 123
    None,  # 124
    None,  # 125
    None,  # 126
    None,  # 127
    None,  # 128
    None,  # 129
    None,  # 130
    None,  # 131
    None,  # 132
    None,  # 133
    None,  # 134
    None,  # 135
    None,  # 136
    None,  # 137
    None,  # 138
    None,  # 139
    None,  # 140
    None,  # 141
    None,  # 142
    None,  # 143
    None,  # 144
    None,  # 145
    None,  # 146
    None,  # 147
    None,  # 148
    None,  # 149
    None,  # 150
    None,  # 151
    None,  # 152
    None,  # 153
    None,  # 154
    None,  # 155
    None,  # 156
    None,  # 157
    None,  # 158
    None,  # 159
    None,  # 160
    None,  # 161
    None,  # 162
    None,  # 163
    None,  # 164
    None,  # 165
    None,  # 166
    None,  # 167
    None,  # 168
    None,  # 169
    None,  # 170
    None,  # 171
    None,  # 172
    None,  # 173
    None,  # 174
    None,  # 175
    None,  # 176
    None,  # 177
    None,  # 178
    None,  # 179
    None,  # 180
    None,  # 181
    None,  # 182
    None,  # 183
    None,  # 184
    None,  # 185
    None,  # 186
    None,  # 187
    None,  # 188
    None,  # 189
    None,  # 190
    None,  # 191
    None,  # 192
    None,  # 193
    None,  # 194
    None,  # 195
    None,  # 196
    None,  # 197
    None,  # 198
    None,  # 199
    None,  # 200
    None,  # 201
    None,  # 202
    None,  # 203
    None,  # 204
    None,  # 205
    None,  # 206
    None,  # 207
    None,  # 208
    None,  # 209
    None,  # 210
    None,  # 211
    None,  # 212
    None,  # 213
    None,  # 214
    None,  # 215
    None,  # 216
    None,  # 217
    None,  # 218
    None,  # 219
    None,  # 220
    None,  # 221
    None,  # 222
    None,  # 223
    None,  # 224
    None,  # 225
    None,  # 226
    None,  # 227
    None,  # 228
    None,  # 229
    None,  # 230
    None,  # 231
    None,  # 232
    None,  # 233
    None,  # 234
    None,  # 235
    None,  # 236
    None,  # 237
    None,  # 238
    None,  # 239
    None,  # 240
    None,  # 241
    None,  # 242
    None,  # 243
    None,  # 244
    None,  # 245
    None,  # 246
    None,  # 247
    None,  # 248
    None,  # 249
    None,  # 250
    None,  # 251
    None,  # 252
    None,  # 253
    None,  # 254
    (255, TType.STRING, 'caller', 'UTF8', None, ),  # 255
)
all_structs.append(Knowledge)
Knowledge.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'subject', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'relation', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'object', 'UTF8', None, ),  # 3
)
all_structs.append(ExtRsp)
ExtRsp.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'text', 'UTF8', None, ),  # 1
    (2, TType.LIST, 'kn', (TType.STRUCT, [Knowledge, None], False), None, ),  # 2
    None,  # 3
    None,  # 4
    None,  # 5
    None,  # 6
    None,  # 7
    None,  # 8
    None,  # 9
    None,  # 10
    None,  # 11
    None,  # 12
    None,  # 13
    None,  # 14
    None,  # 15
    None,  # 16
    None,  # 17
    None,  # 18
    None,  # 19
    None,  # 20
    None,  # 21
    None,  # 22
    None,  # 23
    None,  # 24
    None,  # 25
    None,  # 26
    None,  # 27
    None,  # 28
    None,  # 29
    None,  # 30
    None,  # 31
    None,  # 32
    None,  # 33
    None,  # 34
    None,  # 35
    None,  # 36
    None,  # 37
    None,  # 38
    None,  # 39
    None,  # 40
    None,  # 41
    None,  # 42
    None,  # 43
    None,  # 44
    None,  # 45
    None,  # 46
    None,  # 47
    None,  # 48
    None,  # 49
    None,  # 50
    None,  # 51
    None,  # 52
    None,  # 53
    None,  # 54
    None,  # 55
    None,  # 56
    None,  # 57
    None,  # 58
    None,  # 59
    None,  # 60
    None,  # 61
    None,  # 62
    None,  # 63
    None,  # 64
    None,  # 65
    None,  # 66
    None,  # 67
    None,  # 68
    None,  # 69
    None,  # 70
    None,  # 71
    None,  # 72
    None,  # 73
    None,  # 74
    None,  # 75
    None,  # 76
    None,  # 77
    None,  # 78
    None,  # 79
    None,  # 80
    None,  # 81
    None,  # 82
    None,  # 83
    None,  # 84
    None,  # 85
    None,  # 86
    None,  # 87
    None,  # 88
    None,  # 89
    None,  # 90
    None,  # 91
    None,  # 92
    None,  # 93
    None,  # 94
    None,  # 95
    None,  # 96
    None,  # 97
    None,  # 98
    None,  # 99
    None,  # 100
    None,  # 101
    None,  # 102
    None,  # 103
    None,  # 104
    None,  # 105
    None,  # 106
    None,  # 107
    None,  # 108
    None,  # 109
    None,  # 110
    None,  # 111
    None,  # 112
    None,  # 113
    None,  # 114
    None,  # 115
    None,  # 116
    None,  # 117
    None,  # 118
    None,  # 119
    None,  # 120
    None,  # 121
    None,  # 122
    None,  # 123
    None,  # 124
    None,  # 125
    None,  # 126
    None,  # 127
    None,  # 128
    None,  # 129
    None,  # 130
    None,  # 131
    None,  # 132
    None,  # 133
    None,  # 134
    None,  # 135
    None,  # 136
    None,  # 137
    None,  # 138
    None,  # 139
    None,  # 140
    None,  # 141
    None,  # 142
    None,  # 143
    None,  # 144
    None,  # 145
    None,  # 146
    None,  # 147
    None,  # 148
    None,  # 149
    None,  # 150
    None,  # 151
    None,  # 152
    None,  # 153
    None,  # 154
    None,  # 155
    None,  # 156
    None,  # 157
    None,  # 158
    None,  # 159
    None,  # 160
    None,  # 161
    None,  # 162
    None,  # 163
    None,  # 164
    None,  # 165
    None,  # 166
    None,  # 167
    None,  # 168
    None,  # 169
    None,  # 170
    None,  # 171
    None,  # 172
    None,  # 173
    None,  # 174
    None,  # 175
    None,  # 176
    None,  # 177
    None,  # 178
    None,  # 179
    None,  # 180
    None,  # 181
    None,  # 182
    None,  # 183
    None,  # 184
    None,  # 185
    None,  # 186
    None,  # 187
    None,  # 188
    None,  # 189
    None,  # 190
    None,  # 191
    None,  # 192
    None,  # 193
    None,  # 194
    None,  # 195
    None,  # 196
    None,  # 197
    None,  # 198
    None,  # 199
    None,  # 200
    None,  # 201
    None,  # 202
    None,  # 203
    None,  # 204
    None,  # 205
    None,  # 206
    None,  # 207
    None,  # 208
    None,  # 209
    None,  # 210
    None,  # 211
    None,  # 212
    None,  # 213
    None,  # 214
    None,  # 215
    None,  # 216
    None,  # 217
    None,  # 218
    None,  # 219
    None,  # 220
    None,  # 221
    None,  # 222
    None,  # 223
    None,  # 224
    None,  # 225
    None,  # 226
    None,  # 227
    None,  # 228
    None,  # 229
    None,  # 230
    None,  # 231
    None,  # 232
    None,  # 233
    None,  # 234
    None,  # 235
    None,  # 236
    None,  # 237
    None,  # 238
    None,  # 239
    None,  # 240
    None,  # 241
    None,  # 242
    None,  # 243
    None,  # 244
    None,  # 245
    None,  # 246
    None,  # 247
    None,  # 248
    None,  # 249
    None,  # 250
    None,  # 251
    None,  # 252
    None,  # 253
    None,  # 254
    (255, TType.STRING, 'server_info', 'UTF8', None, ),  # 255
)
all_structs.append(BadCaseReq)
BadCaseReq.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'badcases', (TType.STRUCT, [Knowledge, None], False), None, ),  # 1
    None,  # 2
    None,  # 3
    None,  # 4
    None,  # 5
    None,  # 6
    None,  # 7
    None,  # 8
    None,  # 9
    None,  # 10
    None,  # 11
    None,  # 12
    None,  # 13
    None,  # 14
    None,  # 15
    None,  # 16
    None,  # 17
    None,  # 18
    None,  # 19
    None,  # 20
    None,  # 21
    None,  # 22
    None,  # 23
    None,  # 24
    None,  # 25
    None,  # 26
    None,  # 27
    None,  # 28
    None,  # 29
    None,  # 30
    None,  # 31
    None,  # 32
    None,  # 33
    None,  # 34
    None,  # 35
    None,  # 36
    None,  # 37
    None,  # 38
    None,  # 39
    None,  # 40
    None,  # 41
    None,  # 42
    None,  # 43
    None,  # 44
    None,  # 45
    None,  # 46
    None,  # 47
    None,  # 48
    None,  # 49
    None,  # 50
    None,  # 51
    None,  # 52
    None,  # 53
    None,  # 54
    None,  # 55
    None,  # 56
    None,  # 57
    None,  # 58
    None,  # 59
    None,  # 60
    None,  # 61
    None,  # 62
    None,  # 63
    None,  # 64
    None,  # 65
    None,  # 66
    None,  # 67
    None,  # 68
    None,  # 69
    None,  # 70
    None,  # 71
    None,  # 72
    None,  # 73
    None,  # 74
    None,  # 75
    None,  # 76
    None,  # 77
    None,  # 78
    None,  # 79
    None,  # 80
    None,  # 81
    None,  # 82
    None,  # 83
    None,  # 84
    None,  # 85
    None,  # 86
    None,  # 87
    None,  # 88
    None,  # 89
    None,  # 90
    None,  # 91
    None,  # 92
    None,  # 93
    None,  # 94
    None,  # 95
    None,  # 96
    None,  # 97
    None,  # 98
    None,  # 99
    None,  # 100
    None,  # 101
    None,  # 102
    None,  # 103
    None,  # 104
    None,  # 105
    None,  # 106
    None,  # 107
    None,  # 108
    None,  # 109
    None,  # 110
    None,  # 111
    None,  # 112
    None,  # 113
    None,  # 114
    None,  # 115
    None,  # 116
    None,  # 117
    None,  # 118
    None,  # 119
    None,  # 120
    None,  # 121
    None,  # 122
    None,  # 123
    None,  # 124
    None,  # 125
    None,  # 126
    None,  # 127
    None,  # 128
    None,  # 129
    None,  # 130
    None,  # 131
    None,  # 132
    None,  # 133
    None,  # 134
    None,  # 135
    None,  # 136
    None,  # 137
    None,  # 138
    None,  # 139
    None,  # 140
    None,  # 141
    None,  # 142
    None,  # 143
    None,  # 144
    None,  # 145
    None,  # 146
    None,  # 147
    None,  # 148
    None,  # 149
    None,  # 150
    None,  # 151
    None,  # 152
    None,  # 153
    None,  # 154
    None,  # 155
    None,  # 156
    None,  # 157
    None,  # 158
    None,  # 159
    None,  # 160
    None,  # 161
    None,  # 162
    None,  # 163
    None,  # 164
    None,  # 165
    None,  # 166
    None,  # 167
    None,  # 168
    None,  # 169
    None,  # 170
    None,  # 171
    None,  # 172
    None,  # 173
    None,  # 174
    None,  # 175
    None,  # 176
    None,  # 177
    None,  # 178
    None,  # 179
    None,  # 180
    None,  # 181
    None,  # 182
    None,  # 183
    None,  # 184
    None,  # 185
    None,  # 186
    None,  # 187
    None,  # 188
    None,  # 189
    None,  # 190
    None,  # 191
    None,  # 192
    None,  # 193
    None,  # 194
    None,  # 195
    None,  # 196
    None,  # 197
    None,  # 198
    None,  # 199
    None,  # 200
    None,  # 201
    None,  # 202
    None,  # 203
    None,  # 204
    None,  # 205
    None,  # 206
    None,  # 207
    None,  # 208
    None,  # 209
    None,  # 210
    None,  # 211
    None,  # 212
    None,  # 213
    None,  # 214
    None,  # 215
    None,  # 216
    None,  # 217
    None,  # 218
    None,  # 219
    None,  # 220
    None,  # 221
    None,  # 222
    None,  # 223
    None,  # 224
    None,  # 225
    None,  # 226
    None,  # 227
    None,  # 228
    None,  # 229
    None,  # 230
    None,  # 231
    None,  # 232
    None,  # 233
    None,  # 234
    None,  # 235
    None,  # 236
    None,  # 237
    None,  # 238
    None,  # 239
    None,  # 240
    None,  # 241
    None,  # 242
    None,  # 243
    None,  # 244
    None,  # 245
    None,  # 246
    None,  # 247
    None,  # 248
    None,  # 249
    None,  # 250
    None,  # 251
    None,  # 252
    None,  # 253
    None,  # 254
    (255, TType.STRING, 'caller', 'UTF8', None, ),  # 255
)
all_structs.append(BadCaseRsp)
BadCaseRsp.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'retcode', 'BINARY', None, ),  # 1
    None,  # 2
    None,  # 3
    None,  # 4
    None,  # 5
    None,  # 6
    None,  # 7
    None,  # 8
    None,  # 9
    None,  # 10
    None,  # 11
    None,  # 12
    None,  # 13
    None,  # 14
    None,  # 15
    None,  # 16
    None,  # 17
    None,  # 18
    None,  # 19
    None,  # 20
    None,  # 21
    None,  # 22
    None,  # 23
    None,  # 24
    None,  # 25
    None,  # 26
    None,  # 27
    None,  # 28
    None,  # 29
    None,  # 30
    None,  # 31
    None,  # 32
    None,  # 33
    None,  # 34
    None,  # 35
    None,  # 36
    None,  # 37
    None,  # 38
    None,  # 39
    None,  # 40
    None,  # 41
    None,  # 42
    None,  # 43
    None,  # 44
    None,  # 45
    None,  # 46
    None,  # 47
    None,  # 48
    None,  # 49
    None,  # 50
    None,  # 51
    None,  # 52
    None,  # 53
    None,  # 54
    None,  # 55
    None,  # 56
    None,  # 57
    None,  # 58
    None,  # 59
    None,  # 60
    None,  # 61
    None,  # 62
    None,  # 63
    None,  # 64
    None,  # 65
    None,  # 66
    None,  # 67
    None,  # 68
    None,  # 69
    None,  # 70
    None,  # 71
    None,  # 72
    None,  # 73
    None,  # 74
    None,  # 75
    None,  # 76
    None,  # 77
    None,  # 78
    None,  # 79
    None,  # 80
    None,  # 81
    None,  # 82
    None,  # 83
    None,  # 84
    None,  # 85
    None,  # 86
    None,  # 87
    None,  # 88
    None,  # 89
    None,  # 90
    None,  # 91
    None,  # 92
    None,  # 93
    None,  # 94
    None,  # 95
    None,  # 96
    None,  # 97
    None,  # 98
    None,  # 99
    None,  # 100
    None,  # 101
    None,  # 102
    None,  # 103
    None,  # 104
    None,  # 105
    None,  # 106
    None,  # 107
    None,  # 108
    None,  # 109
    None,  # 110
    None,  # 111
    None,  # 112
    None,  # 113
    None,  # 114
    None,  # 115
    None,  # 116
    None,  # 117
    None,  # 118
    None,  # 119
    None,  # 120
    None,  # 121
    None,  # 122
    None,  # 123
    None,  # 124
    None,  # 125
    None,  # 126
    None,  # 127
    None,  # 128
    None,  # 129
    None,  # 130
    None,  # 131
    None,  # 132
    None,  # 133
    None,  # 134
    None,  # 135
    None,  # 136
    None,  # 137
    None,  # 138
    None,  # 139
    None,  # 140
    None,  # 141
    None,  # 142
    None,  # 143
    None,  # 144
    None,  # 145
    None,  # 146
    None,  # 147
    None,  # 148
    None,  # 149
    None,  # 150
    None,  # 151
    None,  # 152
    None,  # 153
    None,  # 154
    None,  # 155
    None,  # 156
    None,  # 157
    None,  # 158
    None,  # 159
    None,  # 160
    None,  # 161
    None,  # 162
    None,  # 163
    None,  # 164
    None,  # 165
    None,  # 166
    None,  # 167
    None,  # 168
    None,  # 169
    None,  # 170
    None,  # 171
    None,  # 172
    None,  # 173
    None,  # 174
    None,  # 175
    None,  # 176
    None,  # 177
    None,  # 178
    None,  # 179
    None,  # 180
    None,  # 181
    None,  # 182
    None,  # 183
    None,  # 184
    None,  # 185
    None,  # 186
    None,  # 187
    None,  # 188
    None,  # 189
    None,  # 190
    None,  # 191
    None,  # 192
    None,  # 193
    None,  # 194
    None,  # 195
    None,  # 196
    None,  # 197
    None,  # 198
    None,  # 199
    None,  # 200
    None,  # 201
    None,  # 202
    None,  # 203
    None,  # 204
    None,  # 205
    None,  # 206
    None,  # 207
    None,  # 208
    None,  # 209
    None,  # 210
    None,  # 211
    None,  # 212
    None,  # 213
    None,  # 214
    None,  # 215
    None,  # 216
    None,  # 217
    None,  # 218
    None,  # 219
    None,  # 220
    None,  # 221
    None,  # 222
    None,  # 223
    None,  # 224
    None,  # 225
    None,  # 226
    None,  # 227
    None,  # 228
    None,  # 229
    None,  # 230
    None,  # 231
    None,  # 232
    None,  # 233
    None,  # 234
    None,  # 235
    None,  # 236
    None,  # 237
    None,  # 238
    None,  # 239
    None,  # 240
    None,  # 241
    None,  # 242
    None,  # 243
    None,  # 244
    None,  # 245
    None,  # 246
    None,  # 247
    None,  # 248
    None,  # 249
    None,  # 250
    None,  # 251
    None,  # 252
    None,  # 253
    None,  # 254
    (255, TType.STRING, 'server_info', 'UTF8', None, ),  # 255
)
fix_spec(all_structs)
del all_structs
