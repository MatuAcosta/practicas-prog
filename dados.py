
list = [6,6,6,6,6]
sum = [0,0,0,0,0, 0]
valor = 0
def numeros(vector):    
    for i in vector:
    
        
        if (i == 1):
            sum[0] = sum[0] + 1
        elif(i == 2): 
            sum[1] = sum[1] + 2
        elif(i == 3): 
            sum[2] = sum[2] + 3
        elif(i == 4): 
            sum[3] = sum[3] + 4
        elif(i == 5): 
            sum[4] = sum[4] + 5
        elif(i == 6): 
            sum[5] = sum[5] + 6
        
    valor = max(sum)
    print(valor)        

numeros(list)