import base64

b64text = open(r"..\..\tmp\enc_flag").read()

while not b64text.startswith("picoCTF"):
    b64text = str(base64.b64decode(b64text).decode().strip())
   
print(b64text)