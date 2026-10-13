import sys
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RPC, utcnow
from keccak import sel
rpc=RPC(min_interval=0.5)
TF='0x4e1f41613c9084fdb9e34e11fae9412427480e56'
print('query_time_utc', utcnow())
for fn in ['MAX_SUPPLY()','maxSupply()','SUPPLY()','OWNER_ALLOTMENT()','PRICE()','price()','earlyMintActive()','mintingPaused()','tokenCounter()','dreamers()','seed()','totalSupply()','REROLL_PRICE()','renderer()','tokenToStatus(uint256)']:
    data=sel(fn)+('0'*64 if '(uint256)' in fn else '')
    try:
        r=rpc.call('eth_call',[{'to':TF,'data':data},'latest'],retries=2)
        print(fn, r if len(r)>66 else (int(r,16) if r!='0x' else r))
    except Exception as e:
        print(fn,'ERR',str(e)[:80])
