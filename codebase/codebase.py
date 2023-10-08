"""
Suppose you are helping Two Sigma develop a build farm scheduler.
The build farm should build code bases according to their dependency constraints,
and should try to parallelize the build process as much as possible.
Your job is to make a build schedule that minimizes the total build time.

Input You are given a list of codebases (String) with estimated build times (PositiveInteger).
For example:
A:1, B:2, C:3, D:3, E:3
This means that codebase A takes 1 time unit to build, B takes 2, etc
You are also given the codebase dependencies.
For example:
B:A
C:A
D:A,B
E:B,C
This means codebase B depends on A, C depends on A, D depends on A and B etc.
A is not listed, so it doesn't depend on any other codebases.

Output Your function should return the optimal schedule as a list of strings in the below format:
${execution_time},${codebase1},${codebase2}...
*Note that the codebases don't need to follow any specific order.
We provide a helper function to ignore the ordering while testing.

For example, if the input conceptually looks like this:
{picture}
The output should be
1,A       >step 1: build [A] for 1 time unit
2,B,C     >step 2: build [B, C] for 2 time unit
1,C,D     >step 3: build [C D] for 1 time unit
2,D,E     >step 4: build [D, E] for 2 time unit
1,E       >step 5: build [E] for 1 time unit
"""

from collections import defaultdict

class Solution:
    class Task:
        def __init__(self, name, time_remain):
            self.name = name
            self.time_remain = time_remain

    @staticmethod
    def schedule(codebases, dependency):
        # {'A': 1, 'B': 2, 'C': 3, 'D': 3, 'E': 3} {'B': {'A'}, 'C': {'A'}, 'D': {'A', 'B'}, 'E': {'B', 'C'}}
        res = []
        tasks_no_dependency = []
        before_to_after = defaultdict(list)
        for cur, time in codebases.items():
            if cur not in dependency:
                cur_task = Solution.Task(cur, time)
                tasks_no_dependency.append(cur_task)
        for after, before_tasks in dependency.items():
            for before in before_tasks:
                before_to_after[before].append(after)
        while tasks_no_dependency:
            min_time = float('inf')
            cleared_tasks = []
            for task in tasks_no_dependency:
                min_time = min(min_time, task.time_remain)
                cleared_tasks.append(task)
            tasks_no_dependency = []
            curr_round = str(min_time) + ","
            for task in cleared_tasks:
                curr_round += task.name + ","
                task.time_remain = max(0, task.time_remain - min_time)
                if task.time_remain > 0:
                    tasks_no_dependency.append(task)
                else:
                    if task.name not in before_to_after:
                        continue
                    else:
                        for after_task in before_to_after[task.name]:
                            dependency[after_task].remove(task.name)
                            if len(dependency[after_task]) == 0:
                                new_task = Solution.Task(after_task, codebases[after_task])
                                tasks_no_dependency.append(new_task)
            res.append(curr_round)
        return res

    @staticmethod
    def run_test(codebases, dependency, expected):
        c = {}
        d = {}
        for codebase in codebases.split(" "):
            tokens = codebase.split(":")
            if len(tokens) != 2:
                continue
            c[tokens[0]] = int(tokens[1])

        for dep in dependency:
            tokens = dep.split(":")
            sub_tokens = tokens[1].split(",")
            d[tokens[0]] = set(sub_tokens)

        actual = Solution.schedule(c, d)
        assert len(expected) == len(actual)

        if len(expected) == 0:
            return

        for i in range(len(expected)):
            expected_tokens = expected[i].split(",")
            actual_tokens = actual[i].split(",")
            assert len(expected_tokens) == len(actual_tokens)
            assert expected_tokens[0] == actual_tokens[0]
            assert set(expected_tokens[1:]) == set(actual_tokens[1:])

    @staticmethod
    def main():
        codebases = "A:1 B:2 C:3 D:3 E:3"
        dependencies = [
            "B:A",
            "C:A",
            "D:A,B",
            "E:B,C",
        ]
        expected_output = [
            "1,A,",
            "2,B,C,",
            "1,C,D,",
            "2,D,E,",
            "1,E,",
        ]
        Solution.run_test(codebases, dependencies, expected_output)


if __name__ == "__main__":
    Solution.main()

