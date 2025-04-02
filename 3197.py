import string


class State:
    ice = 0
    ice_str = "X"
    water = 1
    water_str = "."
    swan = 2
    swan_str = "L"
    
    @classmethod
    def str_to(cls, target):
        if (target == cls.ice_str):
            return cls.ice
        elif(target == cls.water_str):
            return cls.water
        elif(target == cls.swan_str):
            return cls.swan
        else:
            return None

class Tester:
    def __init__(self):
        self.cases = []
        
    @staticmethod
    def purify_string_matrix(string_mat):
        res = []
        splitted = string_mat.split("\n")
        for line in splitted:
            items = list(line)
            symbolic_line = []
            for item in items:
                symbolic_line.append(State.str_to(item))
            res.append(symbolic_line)
        
        return res
    
    def add_case(self, case):
        self.cases.append(case)
    
    def run_cases(self, func):
        print("========case running ========")
        for case in self.cases:
            res = func(case)
            print("case : ")
            print(case)
            print("res : ", res)
    
    def compare_cases(self, ans_func, target_func):
        print("========compare running ========")
        for case in self.cases:
            ans_res = ans_func(case)
            target_res = target_func(case)
            print("ans : ")
            print(ans_res)
            print("target : ")
            print(target_res)
            
            print("is equal? : ", ans_res == target_res)

def main_brute(case):
    return str(case)


if __name__ == "__main__":
    tester = Tester()
    
    tester.add_case(Tester.purify_string_matrix(    "...XXXXXX..XX.XXX\n"+
                                                    "....XXXXXXXXX.XXX\n"+
                                                    "...XXXXXXXXXXXX..\n"+
                                                    "..XXXXX.LXXXXXX..\n"+
                                                    ".XXXXXX..XXXXXX..\n"+
                                                    "XXXXXXX...XXXX...\n"+
                                                    "..XXXXX...XXX....\n"+
                                                    "....XXXXX.XXXL...\n"))
    
    tester.run_cases(main_brute)