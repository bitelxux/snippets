import random

def best(stocks):
    min_val = min(stocks[0], stocks[1])
    max_proffit = stocks[1] - stocks[0] if stocks[1] > stocks[0] else 0
    for val in stocks[2:]:
        max_proffit = max(max_proffit, val - min_val)
        min_val = min(val, min_val)
    return max_proffit

def tests():
    stocks = [[12, 1, 3, 6, 10, 10, 9, 8, 8],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]

    for stock in stocks:
        best_proffit = best(stock)
        print "%s -> %d" %(stock, best_proffit)
       
if __name__ == "__main__":
    tests()
