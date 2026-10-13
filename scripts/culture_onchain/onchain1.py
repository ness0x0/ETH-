import sys, json, datetime as dt
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RPC, utcnow
from keccak import sel
rpc=RPC(min_interval=0.4)
def call(to, data, block='latest'):
    try: return rpc.call('eth_call',[{'to':to,'data':data},block],retries=3)
    except Exception as e: return 'ERR '+str(e)[:200]
def u(x): return x[2:].rjust(64,'0') if isinstance(x,str) else hex(x)[2:].rjust(64,'0')
def dec_str(h):
    try:
        b=bytes.fromhex(h[2:]); off=int.from_bytes(b[:32],'big'); ln=int.from_bytes(b[off:off+32],'big'); return b[off+32:off+32+ln].decode(errors='ignore')
    except Exception as e: return h
print('query_time_utc', utcnow())
bn=rpc.block_number(); print('latest_block', bn)
AB='0x059edd72cd353df5106d2b9cc5ab83a52287ac3a'
r=call(AB, sel('projectTokenInfo(uint256)')+u(0))
print('AB projectTokenInfo(0)', r if r.startswith('ERR') else [int(r[2+64*i:2+64*(i+1)],16) for i in range(7)])
r=call(AB, sel('ownerOf(uint256)')+u(9999)); print('AB ownerOf(9999)', r)
r=call(AB, sel('ownerOf(uint256)')+u(9998)); print('AB ownerOf(9998)', r)
for name,addr in [('V1wrapNew','0x282bdd42f4eb70e7a9d9f40c8fea0825b7f68c5d'),('V1wrapOld','0xf4a4644e818c2843ba0aabea93af6c80b5984114'),('V1orig','0x6Ba6f2207e343923BA692e5Cae646Fb0F566DB8D'),('Terraforms','0x4e1f41613c9084fdb9e34e11fae9412427480e56'),('MoonCatAcclimated','0xc3f733ca98e0dad0386979eb96fb1722a1a05e69'),('CurioWrapper','0x73da73ef3a6982109c4d5bdb0db9dd3e3783f313')]:
    out={}
    for fn in ['name()','symbol()','totalSupply()','owner()']:
        r=call(addr, sel(fn))
        if fn in ('name()','symbol()') and not r.startswith('ERR') and len(r)>2: r=dec_str(r)
        elif fn=='totalSupply()' and not r.startswith('ERR') and len(r)>2: r=int(r,16)
        out[fn]=r
    print(name, addr, out)
# V1 original: balanceOf wrappers
V1='0x6Ba6f2207e343923BA692e5Cae646Fb0F566DB8D'
for w in ['0x282bdd42f4eb70e7a9d9f40c8fea0825b7f68c5d','0xf4a4644e818c2843ba0aabea93af6c80b5984114']:
    r=call(V1, sel('balanceOf(address)')+u(w)); print('V1 balanceOf',w, int(r,16) if not r.startswith('ERR') else r)
