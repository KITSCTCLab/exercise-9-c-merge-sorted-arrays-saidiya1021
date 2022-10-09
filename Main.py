from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
  x = nums1[0:m]
  y = nums2[0:n]
  nums1=x+y
  nums1 = merge_sort(nums1)
  return nums1
  
def merge_sort(mylist):
  if len(mylist) > 1:
        mid = len(mylist) // 2
        left = mylist[:mid]
        right = mylist[mid:]
        
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i]<=right[j]:
              mylist[k] = left[i]
              i += 1
            else:
                mylist[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            mylist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            mylist[k]=right[j]
            j += 1
            k += 1
  return myList


# Do not change the following code
nums1 = []
nums2 = []
for item in input().split(', '):
  nums1.append(int(item))
for item in input().split(', '):
  nums2.append(int(item))
m = int(input())
n = int(input())
merge(nums1, m, nums2, n)
print(nums1)
