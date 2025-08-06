class StockSpanner:

    def __init__(self):
        self.stack = []
        self.idx = 0

    def next(self, price: int) -> int:
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()
        self.idx +=1
        if self.stack:
            span = self.idx - self.stack[-1][1]
        else:
            span = self.idx - 0
        self.stack.append([price,self.idx])
        return span

# Example Usage (for testing your implementation):
if __name__ == "__main__":
    spanner = StockSpanner()
    
    # Test Case 1: Example from description
    prices1 = [100, 80, 60, 70, 60, 75, 85]
    expected_spans1 = [1, 1, 1, 2, 1, 4, 6]
    actual_spans1 = []
    
    print("--- Test Case 1 ---")
    for i, price in enumerate(prices1):
        span = spanner.next(price)
        actual_spans1.append(span)
        print(f"Price: {price}, Span: {span}")
    
    print(f"Expected Spans: {expected_spans1}")
    print(f"Actual Spans:   {actual_spans1}")

    # Test Case 2: Strictly increasing prices
    spanner2 = StockSpanner() # Re-initialize for a new test
    prices2 = [10, 20, 30, 40, 50]
    expected_spans2 = [1, 2, 3, 4, 5]
    actual_spans2 = []
    
    print("--- Test Case 2 ---")
    for price in prices2:
        span = spanner2.next(price)
        actual_spans2.append(span)
        print(f"Price: {price}, Span: {span}")
    
    print(f"Expected Spans: {expected_spans2}")
    print(f"Actual Spans:   {actual_spans2}")
   

    # Test Case 3: Strictly decreasing prices
    spanner3 = StockSpanner() # Re-initialize for a new test
    prices3 = [50, 40, 30, 20, 10]
    expected_spans3 = [1, 1, 1, 1, 1]
    actual_spans3 = []
    
    print("--- Test Case 3 ---")
    for price in prices3:
        span = spanner3.next(price)
        actual_spans3.append(span)
        print(f"Price: {price}, Span: {span}")
    
    print(f"Expected Spans: {expected_spans3}")
    print(f"Actual Spans:   {actual_spans3}")
   

    # Test Case 4: Prices with duplicates
    spanner4 = StockSpanner() # Re-initialize for a new test
    prices4 = [30, 30, 30, 30, 30]
    expected_spans4 = [1, 2, 3, 4, 5]
    actual_spans4 = []
    
    print("--- Test Case 4 ---")
    for price in prices4:
        span = spanner4.next(price)
        actual_spans4.append(span)
        print(f"Price: {price}, Span: {span}")
    
    print(f"Expected Spans: {expected_spans4}")
    print(f"Actual Spans:   {actual_spans4}")