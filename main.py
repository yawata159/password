import string

def meetsReqs(pw):
    stuf = ([c for c in pw if c in string.uppercase],[c for c in pw if c in string.lowercase],[c for c in pw if c in string.digits])
    return len(stuf[0]) > 0 and len(stuf[1]) > 0 and len(stuf[2]) > 0
