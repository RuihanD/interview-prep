"""
Ques: A parenthesis string only consists of '(' and ')'. In a given input, the difference between the number of ')' and '(' is always one.
This means that there might be one more '(' than the number of ')' present in a string or vice versa.
Your task is to calculate the number of ways you can add a single ')' - or '(' depending on the string - to make the parenthesis string balanced and valid.
The definition of a valid balanced parentheses string is the same as the definition in this question: https://leetcode.com/problems/valid-parentheses/.

Examples:

If the given input string is '())', then the output is 3. This because we can add a single '(' in two ways: '(())', '(())' and '()()'.
If the given input string is ')((', then the output is 0. This is because there is no way to add a single ')' to the given parentheses string to make it valid and balanced.
Time Limit to Solve: 30 minutes
"""


def countValidOptions(s: str):
    length = len(s) + 1
    if length % 2 != 0: return 0
    n = length / 2

    # Helper function will generate all valid parenthesis combinations with n pairs
    def generateParenthesis(n):
        path = []
        res = []

# 2、对于一个「合法」的括号字符串组合 p，必然对于任何 0 <= i < len(p) 都有：子串 p[0..i] 中左括号的数量都大于或等于右括号的数量。
#
# 如果不跟你说这个性质，可能不太容易发现，但是稍微想一下，其实很容易理解，因为从左往右算的话，肯定是左括号多嘛，到最后左右括号数量相等，说明这个括号组合是合法的。
#
# 反之，比如这个括号组合 ))((，前几个子串都是右括号多于左括号，显然不是合法的括号组合。

        def backtracking(left, right):
            if left < right:
                return
            if left > n or right > n:
                return
            if left == n and right == n:
                res.append(''.join(path[:]))
                return

            path.append('(')
            backtracking(left + 1, right)
            path.pop()

            path.append(')')
            backtracking(left, right + 1)
            path.pop()

        backtracking(0, 0)
        return res

    valid_set = set(generateParenthesis(n))
    # Check all result possibilities against valid set
    result = 0
    for i in range(length):
        open = s[:i] + "(" + s[i:]
        close = s[:i] + ")" + s[i:]
        if open in valid_set or close in valid_set: result += 1

    return result

if __name__ == "__main__":
    s1 = '())'
    s2 = ')(('
    res1 = countValidOptions(s1)
    res2 = countValidOptions(s2)
    print(res1,res2)
