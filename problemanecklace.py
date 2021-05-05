
#same_necklace("abc", "cba") => false
def same_necklace (palabra1,palabra2):
    mark = False
    if (palabra1 == palabra2): 
        return True
    else:     
        for letra in palabra1:          
            palabra1 = palabra1.replace(letra,"",1)     
            palabra1 = palabra1 + letra 
            if palabra1 == palabra2: 

                mark = True

    return mark     


def circular(x,y):
    return len(x) == len(y) and x in y*2


print (circular("nicole","icolen")) 
print (circular("nicole", "lenico")) 
print (circular("nicole", "coneli")) 
print (circular("aabaaaaabaab", "aabaabaabaaa")) 
print (circular("abc", "cba")) 
print (circular("xxyyy", "xxxyy")) 
print (circular("xyxxz", "xxyxz") )
print (circular("x", "x") )
print( circular("x", "xx") )
print (circular("x", ""))
print (circular("", "") )
