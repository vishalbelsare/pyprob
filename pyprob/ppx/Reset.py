# automatically generated by the FlatBuffers compiler, do not modify

# namespace: ppx

import flatbuffers

class Reset(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsReset(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Reset()
        x.Init(buf, n + offset)
        return x

    # Reset
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def ResetStart(builder): builder.StartObject(0)
def ResetEnd(builder): return builder.EndObject()
