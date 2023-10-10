"""
Currency Exchange
calculate the max exchange rate with at most k steps (1,n-1) from c1 to currency c2
    max exchange rate for k+1 steps from c1 to c2 = Max(rate(c, c2)* max exchange rate from c1 to c in at most k steps, k steps c1 to c2) (c2 will be unused currency in previous k steps)
rate1*rate2> originalRate
memo[k, current] max exchenge rate from original currency to current currency with k steps = memo[k-1, whatever currency that not used]*rate(current/whatever currency), memo[k-1, current]
"""

def max_transaction_rate(currencies, table, target, currency_at_hand):
    names = {currency: i for i, currency in enumerate(currencies)}
    # print(names)
    # memo = [[0.0 for _ in range(len(currencies))] for _ in range(len(currencies))]
    #
    # current = names[currency_at_hand]
    # for i in range(len(currencies)):
    #     memo[1][i] = table[current][i]
    #
    # exchanged = set()
    # target_curr = names[target]
    # exchanged.add(current)
    #
    # for j in range(2, len(table)):
    #     for i in range(len(table)):
    #         if i not in exchanged:
    #             exchanged.add(i)
    #             memo[j][i] = max(memo[j-1][i], memo[j-1][current] * table[current][i])
    #             exchanged.remove(i)
    #
    # return memo[len(table)-1][target_curr]

if __name__ == "__main__":
    currencies = ["USD", "CAD", "EUR", "CNY"]
    table = [[1, 1.3, 1, 6.49],
             [0.72, 1, 0.9, 5.5],
             [1.1, 1.1, 1, 7.3],
             [0.18, 0.2, 0.136, 1]]

    result = max_transaction_rate(currencies, table, "CNY", "USD")
    print(result)
