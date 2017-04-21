import string
import os

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
    rating = 1
    if pw in words or pw == 'correcthorsebatterystaple':
        return 1
    #TODO: this is currently wrong.
    if uppers > 0: rating += uppers/2
    if lowers > 0: rating += lowers/2
    if nums > 0: rating += nums/2
    if symbs > 0: rating += symbs/2
    rating = min(10,rating)
    return rating

if __name__ == '__main__':
    meaning = ["Garbage", "Very bad", "Very bad", "Very bad", "Very bad", "Bad", "Decent", "Pretty good", "Good", "Very Good"]
    score = isGoodPassword2('OKwatDOuWANT')
    print "{}: {}".format(score, meaning[int(score-1)])
