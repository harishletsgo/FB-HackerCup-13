def isBalanced(message):
    minOpen = 0
    maxOpen = 0
 
    for i in xrange(len(message)):
        if message[i] == '(':
            maxOpen += 1
            if i != 0 and message[i-1] != ':':
                minOpen += 1
        elif message[i] == ')':
            minOpen = max(0, minOpen-1)
            if i != 0 and message[i-1] != ':':
                maxOpen -= 1
                if maxOpen < 0:
                    break
 
    if maxOpen >= 0 and minOpen == 0:
        return "YES"
    else:
        return "NO"