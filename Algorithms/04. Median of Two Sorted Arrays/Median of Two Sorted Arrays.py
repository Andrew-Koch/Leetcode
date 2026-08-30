class Solution:
    #Merge for 2 pre-sorted arrays:
    def merge(self, arr1, arr2):
        result = []
        i = j = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

        result.extend(arr1[i:])
        result.extend(arr2[j:])

        return result
    '''
    #Merge sort 2 input arrays. Not efficient for pre-sorted arrays:
    def mergesort(self, arr1, arr2):
        arr = arr1 + arr2
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.mergesort(arr[:mid], [])
        right = self.mergesort(arr[mid:], [])

        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result
    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Combine and sort arrays
        #combarr = self.mergesort(nums1, nums2)
        combarr = self.merge(nums1, nums2)
        arrlen = len(combarr)
        #If array length is uneven return middle element:
        if (arrlen%2!=0):
            return combarr[int(((arrlen+1)/2)-1)]
        #Else return sum of middle elements:
        else:
            return (combarr[int(arrlen/2)] + combarr[int(arrlen/2) - 1])/ 2
