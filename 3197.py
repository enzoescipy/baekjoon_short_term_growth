from operator import index
import random
import time

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
        NSMULTIPLY = 1000000000
        ans_acc_t = 0
        tar_acc_t = 0
        for case in self.cases:
            
            print("case : ", case[0])
            print(Tester.revert_purify((case[1])))
            
            # run brute
            t_ans = time.perf_counter()
            ans_res = ans_func((Tester.deepcopy(case[0]), Tester.deepcopy(case[1])))
            t_ans = time.perf_counter() - t_ans
            
            # run main
            t_target = time.perf_counter()
            target_res = target_func((Tester.deepcopy(case[0]), Tester.deepcopy(case[1])))
            t_target = time.perf_counter() - t_target
            
            print("is equal? : ", ans_res == target_res)
            if ((ans_res == target_res) != True):
                input("틀렸습니다!")
            print("ans ret: ", ans_res, "target ret: ", target_res)
            print("ans time (ns): ",t_ans * NSMULTIPLY, "target time (ns): ", t_target * NSMULTIPLY)
            ans_acc_t += t_ans
            tar_acc_t += t_target
        print("avr ans take: ", ans_acc_t / len(self.cases) * NSMULTIPLY)
        print("avr target take: ", tar_acc_t  / len(self.cases) * NSMULTIPLY)

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
    
    # submit cases
    rows, cols = map(int, input().split(' '))
    input_string = ""
    for i in range(rows):
        input_string += input()
        input_string += "\n"
    input_string = input_string[:-1]
    
    
    res = main_brute(Tester.purify_string_matrix(input_string))
    print(res)
    
    ## manual cases
    # tester.add_case(Tester.purify_string_matrix(    "...XXXXXX..XX.XXX\n"+
    #                                                 "....XXXXXXXXX.XXX\n"+
    #                                                 "...XXXXXXXXXXXX..\n"+
    #                                                 "..XXXXX.LXXXXXX..\n"+
    #                                                 ".XXXXXX..XXXXXX..\n"+
    #                                                 "XXXXXXX...XXXX...\n"+
    #                                                 "..XXXXX...XXX....\n"+
    #                                                 "....XXXXX.XXXL..."))
    
    # tester.run_cases(main_brute)
    
    
    # ## random cases, worst case complexity graph calculation
    # def random_swan(rows, cols):
    #     while True:
    #         # make the pond
    #         case_str = ""
    #         for i in range(rows):
    #             for j in range(cols):
    #                 is_water = random.randint(0,1) # 1 then is water
    #                 if is_water == 1:
    #                     case_str += "."
    #                 else:
    #                     case_str += "X"
    #             case_str += "\n"
    #         case_str = case_str[:-1]
    #         # place the swan
    #         case_str = list(case_str)
    #         counter = 2
    #         if case_str.count(".") < 2:
    #             continue
    #         while counter > 0:
    #             rand_water = random.randint(0,len(case_str) - 1)
    #             if case_str[rand_water] == ".":
    #                 case_str[rand_water] = "L"
    #                 counter -= 1
    #         return "".join(case_str)
    
    # n = 30
    # for i in range(10000):
    #     tester.add_case(Tester.purify_string_matrix(random_swan(n, n)))
    
    # tester.compare_cases(main_brute, main_brute)
    
    # # report for main_brute
    # # n    |  t (ns, average)
    # # 3    | 7000
    # # 10   | 90000
    # # 20   | 400000
    # # 30   | 1000000
    # # roughly, Omega(main_brute) = Omega(n)
    
    