def simple_recursion(n):
    if n < 0:
        print "Breaking, n is negative"
    else:
        print "Keep going"
        simple_recursion(n - 1)

simple_recursion(5)
