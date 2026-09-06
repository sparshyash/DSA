from collections import Counter

def cntSpecialNum(arr):
        # code here
        
        if not arr:
            return 0
        
        count_ans =0 
        
        
        max_val=max(arr)
        
        freq=Counter(arr)
        
        
        isspecial=[False]*(max_val+1)
        
        for val,count in freq.items():
            
            start =val if freq[val]>1 else 2*val
            
            for multiple in range(start,max_val+1,val):
                
                isspecial[multiple]=True
                
        for num in arr:
            if isspecial[num]:
                count_ans+=1
        return count_ans
if __name__=="__main__":
    arr=[1,2,3,4,5,6]
    print(cntSpecialNum(arr))
