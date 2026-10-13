import sys, collections
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RPC, utcnow, TRANSFER_TOPIC
rpc=RPC(min_interval=0.3)
ZERO='0x'+'0'*64
W='0x282bdd42f4eb70e7a9d9f40c8fea0825b7f68c5d'
print('query_time_utc', utcnow())
for a,b,lab in [(16_086_000,16_530_000,'Dec22-Jan23'),(18_250_000,18_690_000,'Oct-Nov23'),(22_950_000,23_210_000,'Aug25'),(24_990_000,25_300_000,'May-Jun26')]:
    M=rpc.get_logs(W,[TRANSFER_TOPIC,ZERO],a,b,step=500_000)
    c=collections.Counter(l['topics'][2][-40:] for l in M)
    print(lab,'wraps',len(M),'distinct wrappers',len(c),'top',c.most_common(4))
