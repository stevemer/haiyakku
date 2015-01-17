def stripit(msg):
    print ''.join([c for c in msg if c.isalnum()])


stripit("hello,bother)(these")
