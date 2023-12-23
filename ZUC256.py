import time

S0=[[0x3e, 0x72, 0x5b, 0x47, 0xca, 0xe0, 0x00, 0x33, 0x04, 0xd1, 0x54, 0x98, 0x09, 0xb9, 0x6d, 0xcb], [0x7b, 0x1b, 0xf9, 0x32, 0xaf, 0x9d, 0x6a, 0xa5, 0xb8, 0x2d, 0xfc, 0x1d, 0x08, 0x53, 0x03, 0x90], [0x4d, 0x4e, 0x84, 0x99, 0xe4, 0xce, 0xd9, 0x91, 0xdd, 0xb6, 0x85, 0x48, 0x8b, 0x29, 0x6e, 0xac], [0xcd, 0xc1, 0xf8, 0x1e, 0x73, 0x43, 0x69, 0xc6, 0xb5, 0xbd, 0xfd, 0x39, 0x63, 0x20, 0xd4, 0x38], [0x76, 0x7d, 0xb2, 0xa7, 0xcf, 0xed, 0x57, 0xc5, 0xf3, 0x2c, 0xbb, 0x14, 0x21, 0x06, 0x55, 0x9b], [0xe3, 0xef, 0x5e, 0x31, 0x4f, 0x7f, 0x5a, 0xa4, 0x0d, 0x82, 0x51, 0x49, 0x5f, 0xba, 0x58, 0x1c], [0x4a, 0x16, 0xd5, 0x17, 0xa8, 0x92, 0x24, 0x1f, 0x8c, 0xff, 0xd8, 0xae, 0x2e, 0x01, 0xd3, 0xad], [0x3b, 0x4b, 0xda, 0x46, 0xeb, 0xc9, 0xde, 0x9a, 0x8f, 0x87, 0xd7, 0x3a, 0x80, 0x6f, 0x2f, 0xc8], [0xb1, 0xb4, 0x37, 0xf7, 0x0a, 0x22, 0x13, 0x28, 0x7c, 0xcc, 0x3c, 0x89, 0xc7, 0xc3, 0x96, 0x56], [0x07, 0xbf, 0x7e, 0xf0, 0x0b, 0x2b, 0x97, 0x52, 0x35, 0x41, 0x79, 0x61, 0xa6, 0x4c, 0x10, 0xfe], [0xbc, 0x26, 0x95, 0x88, 0x8a, 0xb0, 0xa3, 0xfb, 0xc0, 0x18, 0x94, 0xf2, 0xe1, 0xe5, 0xe9, 0x5d], [0xd0, 0xdc, 0x11, 0x66, 0x64, 0x5c, 0xec, 0x59, 0x42, 0x75, 0x12, 0xf5, 0x74, 0x9c, 0xaa, 0x23], [0x0e, 0x86, 0xab, 0xbe, 0x2a, 0x02, 0xe7, 0x67, 0xe6, 0x44, 0xa2, 0x6c, 0xc2, 0x93, 0x9f, 0xf1], [0xf6, 0xfa, 0x36, 0xd2, 0x50, 0x68, 0x9e, 0x62, 0x71, 0x15, 0x3d, 0xd6, 0x40, 0xc4, 0xe2, 0x0f], [0x8e, 0x83, 0x77, 0x6b, 0x25, 0x05, 0x3f, 0x0c, 0x30, 0xea, 0x70, 0xb7, 0xa1, 0xe8, 0xa9, 0x65], [0x8d, 0x27, 0x1a, 0xdb, 0x81, 0xb3, 0xa0, 0xf4, 0x45, 0x7a, 0x19, 0xdf, 0xee, 0x78, 0x34, 0x60]]
S1=[[0x55, 0xc2, 0x63, 0x71, 0x3b, 0xc8, 0x47, 0x86, 0x9f, 0x3c, 0xda, 0x5b, 0x29, 0xaa, 0xfd, 0x77], [0x8c, 0xc5, 0x94, 0x0c, 0xa6, 0x1a, 0x13, 0x00, 0xe3, 0xa8, 0x16, 0x72, 0x40, 0xf9, 0xf8, 0x42], [0x44, 0x26, 0x68, 0x96, 0x81, 0xd9, 0x45, 0x3e, 0x10, 0x76, 0xc6, 0xa7, 0x8b, 0x39, 0x43, 0xe1], [0x3a, 0xb5, 0x56, 0x2a, 0xc0, 0x6d, 0xb3, 0x05, 0x22, 0x66, 0xbf, 0xdc, 0x0b, 0xfa, 0x62, 0x48], [0xdd, 0x20, 0x11, 0x06, 0x36, 0xc9, 0xc1, 0xcf, 0xf6, 0x27, 0x52, 0xbb, 0x69, 0xf5, 0xd4, 0x87], [0x7f, 0x84, 0x4c, 0xd2, 0x9c, 0x57, 0xa4, 0xbc, 0x4f, 0x9a, 0xdf, 0xfe, 0xd6, 0x8d, 0x7a, 0xeb], [0x2b, 0x53, 0xd8, 0x5c, 0xa1, 0x14, 0x17, 0xfb, 0x23, 0xd5, 0x7d, 0x30, 0x67, 0x73, 0x08, 0x09], [0xee, 0xb7, 0x70, 0x3f, 0x61, 0xb2, 0x19, 0x8e, 0x4e, 0xe5, 0x4b, 0x93, 0x8f, 0x5d, 0xdb, 0xa9], [0xad, 0xf1, 0xae, 0x2e, 0xcb, 0x0d, 0xfc, 0xf4, 0x2d, 0x46, 0x6e, 0x1d, 0x97, 0xe8, 0xd1, 0xe9], [0x4d, 0x37, 0xa5, 0x75, 0x5e, 0x83, 0x9e, 0xab, 0x82, 0x9d, 0xb9, 0x1c, 0xe0, 0xcd, 0x49, 0x89], [0x01, 0xb6, 0xbd, 0x58, 0x24, 0xa2, 0x5f, 0x38, 0x78, 0x99, 0x15, 0x90, 0x50, 0xb8, 0x95, 0xe4], [0xd0, 0x91, 0xc7, 0xce, 0xed, 0x0f, 0xb4, 0x6f, 0xa0, 0xcc, 0xf0, 0x02, 0x4a, 0x79, 0xc3, 0xde], [0xa3, 0xef, 0xea, 0x51, 0xe6, 0x6b, 0x18, 0xec, 0x1b, 0x2c, 0x80, 0xf7, 0x74, 0xe7, 0xff, 0x21], [0x5a, 0x6a, 0x54, 0x1e, 0x41, 0x31, 0x92, 0x35, 0xc4, 0x33, 0x07, 0x0a, 0xba, 0x7e, 0x0e, 0x34], [0x88, 0xb1, 0x98, 0x7c, 0xf3, 0x3d, 0x60, 0x6c, 0x7b, 0xca, 0xd3, 0x1f, 0x32, 0x65, 0x04, 0x28], [0x64, 0xbe, 0x85, 0x9b, 0x2f, 0x59, 0x8a, 0xd7, 0xb0, 0x25, 0xac, 0xaf, 0x12, 0x03, 0xe2, 0xf2]]
D=[ 0x22, 0x2F, 0x24, 0x2A, 0x6D, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x52, 0x10, 0x30]

S=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Key_result=[]
keylen=20
X=[0,0,0,0]
R1=0
R2=0
W=0
Z=0
m32=pow(2,32)

test_times = 1

def ZUC256_MAKEU31(a, b, c, d):
    return ((a << 23) | (b << 16) | (c << 8) | (d))

def BitReconstruction():
    X[0]=add2(S[15],S[14])
    X[1]=add(S[11],S[9])
    X[2]=add(S[7],S[5])
    X[3]=add(S[2],S[0])

def LFSRWithInitMode(u):
    v=(2**15*S[15]+2**17*S[13]+2**21*S[10]+2**20*S[4]+(1+2**8)*S[0])%(2**31-1)
    S.append((v+u)%(2**31-1))
    if S[16] == 0:
        S[16]=2**31-1
    S.pop(0)

def LFSRWithWorkMode():
    S.append((2 ** 15 * S[15] + 2 ** 17 * S[13] + 2 ** 21 * S[10] + 2 ** 20 * S[4] + (1 + 2 ** 8) * S[0]) % (2 ** 31 - 1))
    if S[16] == 0:
        S[16] = 2 ** 31 - 1
    S.pop(0)

def F(X0,X1,X2):
    global R1, R2, W
    W=mod32(X0 ^ R1, R2)
    W1=mod32(R1,X1)
    W2=R2 ^ X2
    print(hex(W1))
    print(hex(W2))
    R1=S_(L1(((W1<<16) | (W2>>16)) & 0xffffffff))
    R2=S_(L2(((W2<<16) | (W1>>16)) & 0xffffffff))

def L1(X):
    return X ^ rot(X,2) ^ rot(X,10)^ rot(X,18) ^ rot (X,24) & 0xffffffff
def L2(X):
    return X ^ rot (X,8) ^ rot (X,14) ^ rot(X,22) ^ rot(X,30) & 0xffffffff
def S_(X):
    bit8=[0,0,0,0]
    result=[0,0,0,0]
    bit8[0]=X>>24
    bit8[1]=(X>>16)&0xff
    bit8[2]=(X>>8)&0xff
    bit8[3]=X&0xff
    for i in range(4):
        row = bit8[i] >> 4 
        nuw = bit8[i] & 0xf
        if i == 0 or i == 2:
            result[i]=S0[row] [nuw]
        else:
            result[i]=S1[row] [nuw]
        ans = (result[0] << 24) | (result[1] << 16) | (result[2] << 8) | result[3] 
    return ans

def rot(X,i):
    return ((X<<i)& 0xffffffff)|(X>>(32-i))
def mod32 (R,X):
    return (R + X)%m32
def H(X):
    bits=(X>>15) & 0xffff
    return bits
def L(X):
    bits = X & 0xffff
    return bits

def add (W1, W2):
    W1h=L(W1) << 16 
    W2l=H(W2)
    all=W1h|W2l
    return all

def add2 (W1, W2):
    W1h = H(W1) << 16
    W2l = L(W2)
    all= W1h | W2l
    return all

def init(key,iv):
    global R1, R2, W, S

    S[0] = ZUC256_MAKEU31(key[0], D[0], key[21], key[16])
    S[1] = ZUC256_MAKEU31(key[1], D[1], key[22], key[17])
    S[2] = ZUC256_MAKEU31(key[2], D[2], key[23], key[18])
    S[3] = ZUC256_MAKEU31(key[3], D[3], key[24], key[19])
    S[4] = ZUC256_MAKEU31(key[4], D[4], key[25], key[20])
    S[5] = ZUC256_MAKEU31(iv[0], (D[5] | iv[17]), key[5], key[26])
    S[6] = ZUC256_MAKEU31(iv[1], (D[6] | iv[18]), key[6], key[27])
    S[7] = ZUC256_MAKEU31(iv[10], (D[7] | iv[19]), key[7], iv[2])
    S[8] = ZUC256_MAKEU31(key[8], (D[8] | iv[20]), iv[3], iv[11])
    S[9] = ZUC256_MAKEU31(key[9], (D[9] | iv[21]), iv[12], iv[4])
    S[10] = ZUC256_MAKEU31(iv[5], (D[10] | iv[22]), key[10], key[28])
    S[11] = ZUC256_MAKEU31(key[11], (D[11] | iv[23]), iv[6], iv[13])
    S[12] = ZUC256_MAKEU31(key[12], (D[12] | iv[24]), iv[7], iv[14])
    S[13] = ZUC256_MAKEU31(key[13], D[13], iv[15], iv[8])
    S[14] = ZUC256_MAKEU31(key[14], (D[14] | (key[31] >> 4)), iv[16], iv[9])
    S[15] = ZUC256_MAKEU31(key[15], (D[15] | (key[31] & 0x0F)), key[30], key[29])
    R1=0
    R2=0
    for i in range(32):
        BitReconstruction()
        F(X[0], X[1], X[2])
        LFSRWithInitMode(W >> 1)
    BitReconstruction()
    F(X[0], X[1], X[2])
    W=0
    LFSRWithWorkMode()

def calc():
    for i in range(keylen):
        BitReconstruction()
        F(X[0], X[1], X[2])
        Key_result.append(W^X[3])
        LFSRWithWorkMode()


if __name__ == '__main__':            
    key=[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    iv=[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]   

            
    start = time.time()
    for x in range(test_times):
        Key_result = []
        init(key, iv)
        calc()
    end = time.time()
    timer = end - start
    if_success = False

    Success_key_result = [0x58d03ad6,0x2e032ce2,0xdafc683a,0x39bdcb03,0x52a2bc67,
            0xf1b7de74,0x163ce3a1,0x01ef5558,0x9639d75b,0x95fa681b,
            0x7f090df7,0x56391ccc,0x903b7612,0x744d544c,0x17bc3fad,
            0x8b163b08,0x21787c0b,0x97775bb8,0x4943c6bb,0xe8ad8afd]
            
    if Key_result == Success_key_result:
        if_success = True

    if if_success:
        str = "Success"
    else:
        str = "Failed"

    print(timer)
    print(str)