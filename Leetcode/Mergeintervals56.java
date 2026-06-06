import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Mergeintervals56 {
    public int[][] merge(int[][] intervals) {
        // Edge case: if there are no intervals or just one, return as is
        if (intervals.length <= 1) {
            return intervals;
        }

        // 1. Sort intervals based on their start times using a lambda expression
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));  // Sort by start time

        // List to store final merged intervals dynamically
        List<int[]> merged = new ArrayList<>();

        // Initialize with the first interval
        merged.add(intervals[0]);

        // 2. Traverse all intervals starting from the second one
        for (int i = 1; i < intervals.length; i++) {
            int[] interval = intervals[i];
            int currentEnd = merged.get(merged.size() - 1)[1];
            int nextStart = interval[0];
            int nextEnd = interval[1];

            // If current interval's end is >= next interval's start, they overlap
            if (currentEnd >= nextStart) {
                // Merge by updating the end time of the current interval
                merged.get(merged.size() - 1)[1] = currentEnd > nextEnd ? currentEnd : nextEnd;  // Ternary
            } else {
                // No overlap: move to the next interval and add it to the list
                merged.add(interval);
            }
        }

        // 3. Convert the List back to a 2D primitive array
        return merged.toArray(new int[merged.size()][]);
    }


    public static void main(String[] args) {
        Mergeintervals56 solution = new Mergeintervals56();
        int[][] input = {{1, 3}, {2, 6}, {8, 10}, {10, 15}};
        
        int[][] result = solution.merge(input);
        
        // Print the result nicely
        System.out.println(Arrays.deepToString(result));
    }
}