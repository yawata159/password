import string

meetsReqs = lambda pw: (lambda l: all(len(n) > 0 for n in l))(([c for c in pw if c in string.uppercase],[c for c in pw if c in string.lowercase],[c for c in pw if c in string.digits]))

isGoodPassword = lambda pw: (len(pw) * 3/4 if len(pw) < 8 else 6) + reduce(lambda a,b: int(a) + int(b), [any(c.isupper() for c in pw), any(c.islower() for c in pw), any(c.isdigit() for c in pw), any(c in string.punctuation for c in pw)])

print isGoodPassword('asdf4sd')
