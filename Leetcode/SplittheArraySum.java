class SplittheArraySum {
    static int maxOf(int []a)
    {
        int n = a.length;
        
        int max = 0;
        
        for(int i =0; i<n; i++)
        {
            max = Math.max(max, a[i]);
        }
        
        return max;
    }
    
    static int sumOf(int []a)
    {
        int n = a.length;
        int sum =0;
        
        for(int i =0; i<n; i++)
        {
            sum += a[i];
        }
        
        return sum;
    }
    
    static boolean isFesiable(int a[], int k, int res)
    {
        int student =1;
        
        int sum =0;
        
        for(int i =0; i<a.length; i++)
        {
            if(sum +a[i] > res)
            {
                student ++;
                sum =a[i];
            }else{
                sum += a[i];
            }
        }
        
        return student <= k;
    }
    public int splitArray(int[] a, int k) {
        int min = maxOf(a);
        int max = sumOf(a);
        
        int res = 0;
        
        while(min <= max)
        {
            int mid = (min+max)/2;
            
            if(isFesiable(a,k,mid))
            {
                res = mid;
                max = mid-1;
            }else{
                min = mid+1;
            }
            
            }
        return res;
    }
}