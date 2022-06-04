def minimumLoss(price):
    n = len(price) # gives length of price list
    loss = max(price) # gives maximum element
    xerox = price.copy() # gives a copy of list
    xerox.sort(reverse = True) #sorts it in reverse order
    for i in range (n-1):
        if(xerox[i]-xerox[i+1]<loss and price.index(xerox[i])<price.index(xerox[i+1])): # we sort in descending order then check if difference between i and i+1 is smaller than max. And we also check if index of i+1 is larger in "price" because we have to buy house first and then sell it at a price where loss is minimum
            loss = xerox[i]-xerox[i+1]
    return loss