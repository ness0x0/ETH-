import sys, json, time, requests
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RPC, utcnow
from keccak import sel
rpc=RPC(min_interval=0.5)
TF='0x4e1f41613c9084fdb9e34e11fae9412427480e56'
print('query_time_utc', utcnow())
addrs=[]
for i in range(8):
    try:
        r=rpc.call('eth_call',[{'to':TF,'data':sel('tokenURIAddresses(uint256)')+hex(i)[2:].rjust(64,'0')},'latest'],retries=2)
        a='0x'+r[-40:]; addrs.append(a); print('tokenURIAddresses',i,a)
    except Exception as e:
        print('idx',i,'end'); break
def bs(path):
    r=requests.get('https://eth.blockscout.com/api/v2/'+path,timeout=60); 
    return r.json() if r.status_code==200 else {'status':r.status_code}
for a in addrs+['0x7a822bce7b9fadd3ed4a533b48eb04eb22696405']:
    d=bs('addresses/'+a); time.sleep(1)
    tx=d.get('creation_transaction_hash') or d.get('creation_tx_hash')
    info={'is_contract':d.get('is_contract'),'name':d.get('name'),'creation_tx':tx,'creator':d.get('creator_address_hash')}
    if tx:
        t=bs('transactions/'+tx); info['created']=t.get('timestamp'); time.sleep(1)
    print(a, info)
