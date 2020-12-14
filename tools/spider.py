import requests
from random import random as rnd
from time import sleep

import pathlib

class FalseResponse:
    def __init__(self,code,content):
        self.status_code = code
        self.content = content

def get(url, cache=True):
    # Check the cache
    p = pathlib.Path.cwd() / 'cache' / 'spider' / pathlib.Path(url)
    if(cache and p.exists()):
        with open(p,'r') as fh:
            res = fh.read().replace("\\r\\n",'')
        print('[\033[38;2;0;250;0mCACHE\033[0m]',url)
        return FalseResponse(200,res)
    
    p.parent.mkdir(parents=True, exist_ok=True)
    # Or make the petition
    t = rnd()*5+2
    print('[\033[38;2;250;250;0m{:4.2f}\033[0m] {}'.format(t, url))
    sleep(t)
    res = requests.get(url,timeout=10)
    with open(p,'w') as fh:
        fh.write(str(res.content))
        print('\tCached')
    if(res.status_code == 429): # too many requests
        print('TOO MANY REQUESTS: ABORTING')
        exit()
    return res


