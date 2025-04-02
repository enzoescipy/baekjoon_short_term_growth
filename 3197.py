import string

from sympy import true
from tomlkit import item


class State:
    ice = False
    ice_str = "X"
    water = True
    water_str = "."
    
    @classmethod
    def str_to(cls, target):
        if (target == cls.ice_str):
            return cls.ice
        elif(target == cls.water_str):
            return cls.water
        else:
            return None

class Tester:
    def __init__(self):
        self.cases = []
        
    @staticmethod
    def purify_string_matrix(string_mat):
        res = []
        splitted = string_mat.split("\n")
        swan_pos = []
        for i in range(len(splitted)):
            items = list(splitted[i])
            symbolic_line = []
            for j in range(len(items)):
                item_res = State.str_to(items[j])
                if item_res == None:
                    swan_pos.append((i,j))
                    item_res = True
                symbolic_line.append(item_res)
            res.append(symbolic_line)
        
        return (swan_pos, res)
    
    @staticmethod
    def revert_purify(matrix):
        res = ""
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if (matrix[i][j] == False):
                    res += "X"
                else:
                    res += "."
            res += "\n"
        return res
    
    @staticmethod
    def pprint(matrix):
        print("[")
        for line in matrix:
            print(line)
        print("]")
        
    @staticmethod
    def deepcopy(matrix):
        res = []
        for line in matrix:
            res.append(line[:])
        return res
    
    def add_case(self, case):
        self.cases.append(case)
    
    def run_cases(self, func):
        print("========case running ========")
        for case in self.cases:
            print("case : ", case[0])
            print(Tester.revert_purify((case[1])))
            res = func(case)
            print("res : ", res)
    
    def compare_cases(self, ans_func, target_func):
        print("========compare running ========")
        for case in self.cases:
            print("ans : ", ans_res[0])
            print(Tester.revert_purify((ans_res[1])))
            print("target : ", target_res[0])
            print(Tester.revert_purify((target_res[1])))
            
            ans_res = ans_func(case)
            target_res = target_func(case)
            print("is equal? : ", ans_res == target_res)

def main_brute(case):
    # case is the (swan_pos, pond)
    # swan_pos is row to column position of the swan
    # pond is the True/False array which False means swan can't cross that point
    
    swan_pos, pond = case
    
    # pond_copy = Tester.deepcopy(pond)
    def pond_arify(pond):
        """
        make pond area visible by nominating each points.
        WARNING : this function change the pond directly. 
        e.g) [
            [T,T,F],
            [T,F,T],
            [F,T,F],
        ]
        ->
             [
            [0,0,F],
            [0,F,1],
            [F,1,1],
        ]
        """
        rows = len(pond)
        cols = len(pond[0])
        
        def mark(i, j, num):
            # mark position i, j in the pond. if already marked, return.
            if (type(pond[i][j]) == type(True) and pond[i][j] == True):
                pond[i][j] = num
                # print("assign")
            else:
                # print("ret")
                return
            
            # mark the 4-direction around self, and iterate
            targets = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]
            for target in targets:
                if 0 <= target[0] and target[0] < rows and 0 <= target[1] and target[1] < cols:
                    mark(target[0], target[1], num)
                
            
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                count += 1
                if type(pond[i][j]) != type(True) or pond[i][j] != True:
                    continue
                else:
                    mark(i, j, count)
                    count += 1
    
    def pond_melt(pond):
        """
        melt the pond.
        """           
        rows = len(pond)
        cols = len(pond[0])
                
        melted = []
        for i in range(rows):
            for j in range(cols):
                val = pond[i][j]
                if val == True:
                    continue
                
                targets = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]
                for target in targets:
                    if (0 <= target[0] and target[0] < rows and 0 <= target[1] and target[1] < cols):
                        target_val = pond[target[0]][target[1]]
                        if target_val == True:
                            melted.append((i, j))
                            break
        
        for melt in melted:
            pond[melt[0]][melt[1]] = True
    
    ans = 0  
    while True:
        pond_copy = Tester.deepcopy(pond)
        pond_arify(pond_copy)
        swan1 = swan_pos[0]
        swan2 = swan_pos[1]
        if pond_copy[swan1[0]][swan1[1]] == pond_copy[swan2[0]][swan2[1]]:
            return ans
        else:
            ans += 1
        pond_melt(pond)
        

if __name__ == "__main__":
    tester = Tester()
    
    tester.add_case(Tester.purify_string_matrix(    "...XXXXXX..XX.XXX\n"+
                                                    "....XXXXXXXXX.XXX\n"+
                                                    "...XXXXXXXXXXXX..\n"+
                                                    "..XXXXX.LXXXXXX..\n"+
                                                    ".XXXXXX..XXXXXX..\n"+
                                                    "XXXXXXX...XXXX...\n"+
                                                    "..XXXXX...XXX....\n"+
                                                    "....XXXXX.XXXL..."))
    
    tester.run_cases(main_brute)