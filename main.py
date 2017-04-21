import string

meetsReqs = lambda pw: (lambda l: all(len(n) > 0 for n in l))(([c for c in pw if c in string.uppercase],[c for c in pw if c in string.lowercase],[c for c in pw if c in string.digits]))

def isGoodPassword(pw):
	lenReq = len(pw) * 3/4 if len(pw) < 8 else 6
	otherReq = [any(c.isupper() for c in pw), any(c.islower() for c in pw), any(c.isdigit() for c in pw), any(c in string.punctuation for c in pw)]
	otherReq = reduce(lambda a,b: int(a) + int(b), otherReq)
	return lenReq + otherReq