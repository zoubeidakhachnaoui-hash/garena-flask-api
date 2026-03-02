import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import urllib3
import logging
import json
import re
import base64
from datetime import datetime
from flask import Flask, request, jsonify

#H4RDIXXXXX IS HERE?

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.basicConfig(level=logging.INFO)
log=logging.getLogger(__name__)

app = Flask(__name__)

key=bytes([89,103,38,116,99,37,68,69,117,104,54,37,90,99,94,56])
iv=bytes([54,111,121,90,68,114,50,50,69,51,121,99,104,106,77,37])

url="https://loginbp.ggpolarbear.com/MajorLogin"
pl="1a13323032362d30312d31342031353a32363a303922096672656520666972653a07312e3132302e33420a694f532031352e382e324a0848616e6468656c64520e4f72616e67652054756e697369615a045749464960b60a68ee0572033332367a0d61726d3634207c2030207c20328001d00f8a010d4170706c6520413130204750559201054d6574616c9a012a4170706c657c34373633423036462d314146422d343931462d394331392d374643463842383039323330a2010e3130322e3135322e36332e313338aa010570742d6272b201203035633264306538623230366234643765396230323862383432626132636132ba010134c2010848616e6468656c64ca01096950686f6e65392c33ea014033323162663665316664366365376232326434396436353538633130636531353830306266623335396465373663643034326565626634323139646334616265f00101f003a1ee01f803bd1bb00402c80402e00401ea0409494f53446576696365f00403f804019a0507312e3132302e31a80503b205054d6574616cb805ff7fc00504e005cac802ea0503696f73f205484b7173485438436a38696d333257705a4464592f6e51315877434c3655692f3237486e796b32783432694172687a646130754f445664746c5136464530542f52497a6e6c70413d3d9006019a060134a2060134b2060e600017127213595821545f120d10090909090909090909"

def eNcApi(h):
    #H4RDIXXXXX IS HERE?
    try:
        b=bytes.fromhex(h)
        c=AES.new(key,AES.MODE_CBC,iv)
        r=c.encrypt(pad(b,AES.block_size))
        return r.hex()
    except Exception as e:
        log.error(str(e))
        raise

def gEtJwt(t):
    #H4RDIXXXXX IS HERE?
    p=r'eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+'
    m=re.findall(p,t)
    if m:
        return m[0]
    return None

def dEcJwt(t):
    #H4RDIXXXXX IS HERE?
    try:
        s=t.split('.')
        if len(s)!=3:
            return None
        p=s[1]
        n=4-len(p)%4
        if n!=4:
            p+='='*n
        d=base64.urlsafe_b64decode(p)
        return json.loads(d)
    except Exception as e:
        log.error(str(e))
        return None

@app.route('/xg', methods=['GET'])
def login_api():
    #H4RDIXXXXX IS HERE?
    try:
        uid = request.args.get('uid')
        pas = request.args.get('Pw')
        
        if not uid or not pas:
            return jsonify({"error": "Missing uid or Pw parameter"}), 400

        gu="https://100067.connect.garena.com/oauth/guest/token/grant"

        gh={
        "Host":"100067.connect.garena.com",
        "User-Agent":"GarenaMSDK/4.0.19P4(G011A ;Android 9;en;US;)",
        "Content-Type":"application/x-www-form-urlencoded"
        }

        gd={
        "uid":uid,
        "password":pas,
        "response_type":"token",
        "client_type":"2",
        "client_id":"100067"
        }

        r=requests.post(gu,headers=gh,data=gd,timeout=10)
        r.raise_for_status()
        j=r.json()

        at=j["access_token"]
        oi=j["open_id"]

        ob="05c2d0e8b206b4d7e9b028b842ba2ca2"
        tb="321bf6e1fd6ce7b22d49d6558c10ce15800bfb359de76cd042eebf4219dc4abe"

        pb=bytes.fromhex(pl)

        mp=pb.replace(ob.encode(),oi.encode())
        mp=mp.replace(tb.encode(),at.encode())

        ep=eNcApi(mp.hex())

        h={
        "X-Unity-Version":"2018.4.11f1",
        "ReleaseVersion":"OB52",
        "Content-Type":"application/x-www-form-urlencoded",
        "X-GA":"v1 1",
        "User-Agent":"Dalvik/2.1.0",
        "Host":"loginbp.ggpolarbear.com",
        "Connection":"Keep-Alive",
        "Accept-Encoding":"gzip"
        }

        rs=requests.post(url,headers=h,data=bytes.fromhex(ep),verify=False,timeout=15)

        tk=gEtJwt(rs.text)

        result = {
            "access_token": at,
            "open_id": oi,
            "jwt": tk,
            "decoded_jwt": dEcJwt(tk) if tk else None
        }

        return jsonify(result)

    except Exception as e:
        log.error(str(e))
        return jsonify({"error": str(e)}), 500

if __name__=="__main__":
    #H4RDIXXXXX IS HERE?
    app.run(host='0.0.0.0', port=5000)
