import numpy as np
import cv2


def decode(IEnc):
    expected = "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ=="
    bits = 8
    places = np.array([2**(bits-1-i) for i in range(bits)])

    IDec = IEnc.flatten()

    i = 0
    s = ""
    while i <= 64:
        print(f"IDec[{i}:{i+bits}]",IDec[i:i+bits])
        c = IDec[i:i+bits] % 2
        if len(c) < bits:
            break 
        print("char in bin",c, "expected_char in bin", bin(ord(expected[i//8]))[2:])
        c = np.sum(places*c)
        print("char ord",c,"expected",ord(expected[i//8]))

        s += chr(c)
        i += bits
    return s
    
img = cv2.imread(r"..\..\tmp\red.png",-1)
print(img[0,:4,:])
print("img.shape",img.shape)
print(decode(img[:,:,:]))