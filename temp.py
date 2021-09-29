import math 
import sys 
 
def search(a, target, low, high): 
    mid = low + (high - low) // 2 
    if a[mid] == target: 
        return mid
    else if a[mid] < target: 
        search(a, target, mid + 1, high)
    else 
        search(a, target, low, mid + 1)
    return -1
 


    
