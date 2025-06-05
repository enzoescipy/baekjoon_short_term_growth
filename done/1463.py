class Tester:
    def __init__(self) -> None:
        self.test_cases = []
        
    def add_case(self, case):
        self.test_cases.append(case)
        
    def run_cases(self, runner):
        for case in self.test_cases:
            res = runner(case)
            
            print(res)

def main_runner(case:int):
    memorizer = [0 for i in range(case)] # index : input, value : output # WARN : input is start at 1!!
    
    for c in range(1,  case+ 1):
        if (c == 1):
            memorizer[c - 1] = 0
            continue
        
        val_1 = c - 1
        val_2 = c % 3
        val_3 = c % 2
        
        candidate = []
                
        if (val_1 > 0):
            val_1 = memorizer[val_1 - 1]
            candidate.append(val_1)

        if (val_2 == 0):
            val_2 = memorizer[int(c / 3 - 1)]
            candidate.append(val_2)

        if (val_3 == 0):
            val_3 = memorizer[int(c / 2 - 1)]
            candidate.append(val_3)
            
        
        memorizer[c-1] = min(candidate) + 1
    
    return memorizer[-1]
        
        

if __name__ == "__main__":
    # tester = Tester()
    # # for i in range(1, 10):
    # #     tester.add_case(i)
    
    # tester.add_case(20)
    
    # tester.run_cases(main_runner)
    
    case = int(input())

    memorizer = [0 for i in range(case)] # index : input, value : output # WARN : input is start at 1!!

    for c in range(1,  case+ 1):
        if (c == 1):
            memorizer[c - 1] = 0
            continue
        
        val_1 = c - 1
        val_2 = c % 3
        val_3 = c % 2
        
        candidate = []
                
        if (val_1 > 0):
            val_1 = memorizer[val_1 - 1]
            candidate.append(val_1)

        if (val_2 == 0):
            val_2 = memorizer[int(c / 3 - 1)]
            candidate.append(val_2)

        if (val_3 == 0):
            val_3 = memorizer[int(c / 2 - 1)]
            candidate.append(val_3)
            
        
        memorizer[c-1] = min(candidate) + 1

    print(memorizer[-1])