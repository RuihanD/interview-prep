"""
Currency Exchange
calculate the max exchange rate with at most k steps (1,n-1) from c1 to currency c2
    max exchange rate for k+1 steps from c1 to c2 = Max(rate(c, c2)* max exchange rate from c1 to c in at most k steps, k steps c1 to c2) (c2 will be unused currency in previous k steps)
rate1*rate2> originalRate
memo[k, current] max exchenge rate from original currency to current currency with k steps = memo[k-1, whatever currency that not used]*rate(current/whatever currency), memo[k-1, current]
"""
from collections import defaultdict, deque
from typing import List
curPoint = 1
resPoint = float('-inf')

def max_transaction_rate(currencies, table, target, currency_at_hand):
    currencyToIdx = defaultdict()
    Len = len(currencies)
    for i in range(Len):
        currencyToIdx[currencies[i]] = i

    def dfs(cur, curLevel, visited):
        global curPoint
        global resPoint
        if curLevel >= Len:
            if cur == currencyToIdx[target]:
                resPoint = max(resPoint, curPoint)
            return
        for nxt in range(Len):
            if nxt == cur or nxt in visited:
                continue
            visited.add(nxt)
            rate = table[cur][nxt]
            curPoint *= rate
            dfs(nxt, curLevel + 1, visited)
            curPoint /= rate
            visited.remove(nxt)
        return

    visited = set()
    currency_at_hand_idx = currencyToIdx[currency_at_hand]
    dfs(currency_at_hand_idx, 0, visited)
    return

def main():
    currencies = ["USD", "CAD", "EUR", "CNY"]
    table = [[1, 1.3, 1, 6.49],
             [0.72, 1, 0.9, 5.5],
             [1.1, 1.1, 1, 7.3],
             [0.18, 0.2, 0.136, 1]]
    max_transaction_rate(currencies, table, "CNY", "USD")
    print(resPoint)

if __name__ == "__main__":
    main()
