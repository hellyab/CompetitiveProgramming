def largestRectangle(h):
    h.sort()
    n = len(h)
    max_ = 0
    for height in h:
        if  max_ - (height * n) < 0:
            max_ = height * n
        n -= 1
        
    print(max_) 

largestRectangle([8979, 4570, 6436, 5083, 7780, 3269, 5400, 7579, 2324, 2116])