import string
import os
import numpy

meetsReqs = lambda pw: (lambda l: all(len(n) > 0 for n in l))(([c for c in pw if c in string.uppercase],[c for c in pw if c in string.lowercase],[c for c in pw if c in string.digits]))

isGoodPassword = lambda pw: (len(pw) * 3/4 if len(pw) < 8 else 6) + reduce(lambda a,b: int(a) + int(b), [any(c.isupper() for c in pw), any(c.islower() for c in pw), any(c.isdigit() for c in pw), any(c in string.punctuation for c in pw)])

def readDict():
    if os.path.isfile("/usr/share/dict/words"):
        print "Dictionary supported."
        with open("/usr/share/dict/words") as f:
            return [x.strip() for x in f.readlines()]
    else:
        print "Dictionary not supported. Results may be unreliable."

def isGoodPassword2(pw):
    words = readDict()
    uppers = len([c for c in pw if c.isupper()])
    lowers = len([c for c in pw if c.islower()])
    nums = len([c for c in pw if c.isdigit()])
    symbs = len([c for c in pw if not c.isupper() and not c.islower() and not c.isdigit()])
    rating = 0
    if pw.lower() in words or pw == 'correcthorsebatterystaple':
        return 1
    rating += len(pw)*0.7
    rating -= numpy.std([uppers,lowers,nums,symbs])*0.2
    rating = int(round(min(10,max(1,rating))))
    return rating

if __name__ == '__main__':
    meaning = ["Garbage", "Very bad", "Very bad", "Very bad", "Very bad", "Bad", "Decent", "Pretty good", "Good", "Very Good"]
    score = isGoodPassword2('OKwatDOuWANT')
    print "{}: {}".format(score, meaning[score-1])
