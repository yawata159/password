import string

meetsReqs = lambda pw: (lambda l: all(len(n) > 0 for n in l))(([c for c in pw if c in string.uppercase],[c for c in pw if c in string.lowercase],[c for c in pw if c in string.digits]))
