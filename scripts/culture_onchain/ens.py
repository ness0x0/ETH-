import sys
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RPC, utcnow, TRANSFER_TOPIC
from keccak import keccak256, sel
rpc=RPC(min_interval=0.4)
REG='0x00000000000C2E074eC69A0dFb2997BA6C7d2e1e'
def namehash(name):
    node=b'\x00'*32
    for label in reversed(name.split('.')):
        node=keccak256(node+keccak256(label.encode()))
    return node
def rev(addr):
    node=namehash(addr.lower()[2:]+'.addr.reverse').hex()
    r=rpc.call('eth_call',[{'to':REG,'data':sel('resolver(bytes32)')+node},'latest'])
    res='0x'+r[-40:]
    if int(res,16)==0: return None
    r=rpc.call('eth_call',[{'to':res,'data':sel('name(bytes32)')+node},'latest'])
    b=bytes.fromhex(r[2:]); 
    if len(b)<64: return None
    off=int.from_bytes(b[:32],'big'); ln=int.from_bytes(b[off:off+32],'big'); return b[off+32:off+32+ln].decode(errors='ignore')
print('query_time_utc', utcnow())
for a in sys.argv[1:]:
    try: print(a, rev(a))
    except Exception as e: print(a,'ERR',str(e)[:100])
