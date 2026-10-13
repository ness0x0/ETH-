import sys
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RPC, utcnow
from keccak import sel
rpc=RPC(min_interval=0.4)
P='0xC2C5f8aAD3428551c8ABb9C4Be62724Ea36C3717'
print('query_time_utc', utcnow())
def dec_str(h):
    b=bytes.fromhex(h[2:]); off=int.from_bytes(b[:32],'big'); ln=int.from_bytes(b[off:off+32],'big'); return b[off+32:off+32+ln].decode(errors='ignore')
for fn in ['version()','signedByTDR()','locked()','segmentCounter()','owner()','runeNames(uint256)']:
    data=sel(fn)+('0'*63+'1' if 'uint256' in fn else '')
    try:
        r=rpc.call('eth_call',[{'to':P,'data':data},'latest'],retries=2)
        print(fn, dec_str(r) if fn in ('version()','runeNames(uint256)') else ('0x'+r[-40:] if fn=='owner()' else int(r,16)))
    except Exception as e: print(fn,'ERR',str(e)[:100])
# Terraforms data proxies: implementation slots
slot='0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc'
for a in ['0xb51a3bb80d50a3153c1b63b0e38fc200676f5ba5','0x8af860c8f157f4e3b6a54913bfa6bb96ab2605c2','0xfcA647387E28e73E291DD90e7b09fA32bCBB2604','0x331512a28a4cf80221af949b5d43041ff0fc7f01']:
    r=rpc.call('eth_getStorageAt',[a,slot,'latest']); print('impl of',a,'0x'+r[-40:])
