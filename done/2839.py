
class Tester:
    def __init__(self) -> None:
        self.test_cases = []
        
    def add_test(self, weight:int):
        self.test_cases.append(weight)
        
    def run_test(self, runner):
        for case in self.test_cases:
            res = runner(case)
            
            print(res)

def main(max_weight:int):
    subproblem = [-1 for i in range(max_weight + 1)] # index : input weight, value : total bag. (if not satisfied, value is -1.)
    subproblem[0] = 0
    for weight in range(max_weight + 1):
        if weight == 0:
            continue
        # search for the subproblem
        bag_candidate_3 = -1
        bag_candidate_5 = -1
        if (weight - 3 >= 0):
            bag_candidate_3 = subproblem[weight - 3]
        if (weight - 5 >= 0):
            bag_candidate_5 = subproblem[weight - 5]
        
        # determine the value
        res = 0
        if (bag_candidate_3 == -1 and bag_candidate_5 == -1):
            res = -1
        elif (bag_candidate_3 != -1 and bag_candidate_5 != -1):
            res = bag_candidate_5 + 1
        else:
            res = bag_candidate_5
            if (res < 0):
                res = bag_candidate_3
            res += 1
            
        
        subproblem[weight] = res
    
    return subproblem[-1]


if __name__ == "__main__":
    # tester = Tester()
    
    # tester.add_test(18)
    # tester.add_test(4)
    # tester.add_test(6)
    # tester.add_test(9)
    # tester.add_test(11)
    
    # tester.run_test(main)

    max_weight = int(input())

    subproblem = [-1 for i in range(max_weight + 1)] # index : input weight, value : total bag. (if not satisfied, value is -1.)
    subproblem[0] = 0
    for weight in range(max_weight + 1):
        if weight == 0:
            continue
        # search for the subproblem
        bag_candidate_3 = -1
        bag_candidate_5 = -1
        if (weight - 3 >= 0):
            bag_candidate_3 = subproblem[weight - 3]
        if (weight - 5 >= 0):
            bag_candidate_5 = subproblem[weight - 5]
        
        # determine the value
        res = 0
        if (bag_candidate_3 == -1 and bag_candidate_5 == -1):
            res = -1
        elif (bag_candidate_3 != -1 and bag_candidate_5 != -1):
            res = bag_candidate_5 + 1
        else:
            res = bag_candidate_5
            if (res < 0):
                res = bag_candidate_3
            res += 1
            
        
        subproblem[weight] = res

    print(subproblem[-1])
