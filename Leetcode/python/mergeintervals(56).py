class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()  # sort based on start values

        # List to store final merged intervals
        merged = []

        # Traverse all intervals
        for interval in intervals:
            # If merged list is empty or current interval doesn't overlap
            if not merged or merged[-1][1] < interval[0]:
                # Append current interval as a new one
                merged.append(interval)
            else:
                # Overlapping: merge by extending the end
                merged[-1][1] = max(
                    merged[-1][1],
                    interval[1]
                )

        return merged
    def main():
        solution=Solution()
        print(solution.merge([[1,3],[2,6],[8,10],[10,15]]))