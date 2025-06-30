def merge_intervals(intervals):
    # BF Approach
    # merge =[]
    # intervals.sort()
    # n = len(intervals)
    # for i in range(n):
    #     start,end = intervals[i][0],intervals[i][1]
    #     if merge and end <= merge[-1][1]:
    #       continue
    #     for j in range(i+1,n):
    #        if (intervals[j][0] <= end):
    #           end = max(intervals[j][1],end)
    #     merge.append([start,end])
    # return merge

    #Optimal Approach
     merge = []
     intervals.sort()
     n = len(intervals)
     for i in range(n):
        if not(merge) or intervals[i][0] > merge[-1][1]:
           merge.append(intervals[i])
        else:
           merge[-1][1] = max(merge[-1][1],intervals[i][1])
     return merge

def main():
  """
  Main function to test the merge_intervals function.
  """
  intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
  merged_intervals = merge_intervals(intervals)
  print(f"Original intervals: {intervals}")
  print(f"Merged intervals: {merged_intervals}")

if __name__ == "__main__":
  main()