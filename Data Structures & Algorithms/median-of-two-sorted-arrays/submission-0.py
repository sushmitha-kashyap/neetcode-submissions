class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        smaller_array = nums1
        larger_array = nums2
        total_length = len(nums1) + len(nums2)
        half = total_length // 2

        if len(smaller_array) > len(larger_array):
            smaller_array, larger_array = larger_array, smaller_array

        left = 0
        right = len(smaller_array) - 1

        while True:

            smaller_partition = (left + right) // 2
            larger_partition = half - smaller_partition - 2

            smaller_left = (
                smaller_array[smaller_partition]
                if smaller_partition >= 0
                else float("-infinity")
            )

            smaller_right = (
                smaller_array[smaller_partition + 1]
                if (smaller_partition + 1) < len(smaller_array)
                else float("infinity")
            )

            larger_left = (
                larger_array[larger_partition]
                if larger_partition >= 0
                else float("-infinity")
            )

            larger_right = (
                larger_array[larger_partition + 1]
                if (larger_partition + 1) < len(larger_array)
                else float("infinity")
            )

            if smaller_left <= larger_right and larger_left <= smaller_right:

                if total_length % 2:
                    return min(smaller_right, larger_right)

                return (
                    max(smaller_left, larger_left)
                    + min(smaller_right, larger_right)
                ) / 2

            elif smaller_left > larger_right:
                right = smaller_partition - 1

            else:
                left = smaller_partition + 1