def hourglassSum(arr):
    max_ =  float('-inf')
    for i in range(4):
        for j in range(4):
            current_mux=(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
            max_=max(max_,current_mux)
    return(max_)def hourglassSum(arr):
    
