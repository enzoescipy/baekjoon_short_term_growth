# 문제
# 이 문제는 아주 평범한 배낭에 관한 문제이다.

# 한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.

# 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

# 입력
# 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

# 입력으로 주어지는 모든 수는 정수이다.

# 출력
# 한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.
# 
# 
# 예제 입력 1 
# 4 7
# 6 13
# 4 8
# 3 6
# 5 12
# 예제 출력 1 
# 14
#
# 해답 : https://howudong.tistory.com/106
# 문제 : https://www.acmicpc.net/problem/12865
#

from audioop import add


class Tester:
    candidate = 'candidate'
    limit = 'limit'  
    index :int = 0
    
    answers:list[int] = []
    cases:list[int] = []
    count = 0
    
    @classmethod
    def init(cls):
        cls.cases = [
            {cls.candidate : [
                (6, 13),
                (4, 8),
                (3, 6),
                (5, 12),
                # 13 + 6 + 12 = 31
            ],
            cls.limit : 14
            },
            {cls.candidate : [
                (6, 0),
            ],
            cls.limit : 100
            },
            {cls.candidate : [
                (1,2),
                (3,4),
                (5,6),
                (7,8),
                (9,10),
                (11,12),
                (13,12),
                (16,28),
                (13,24),
                (24,42),
            ],
            cls.limit : 100
            },
        ]
        
        cls.answers = [31,0, 0]
        
        cls.count = 1
    
    @classmethod
    def next(cls) -> tuple[dict[str, any], any]:
        res = (cls.cases[cls.index],cls.answers[cls.index])
        cls.index += 1
        return res

# def weight_value_sum(candidate: list[tuple[int,int]], target_indices = list[int]) -> list[int, int]:
#     sum_v = 0
#     sum_w = 0
#     for index in target_indices:
#         w, v = candidate[index]
#         sum_v += v
#         sum_w += w
    
#     return (sum_w, sum_v)

# def identical(a:list[int], b:list[int]) -> bool:
#     if len(a) != len(b):
#         return False
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             return False

#     return True


def main_edu(candidate :list[tuple[int,int]], limit:int):
    # fix the initial point on dp table as (0,0)
    candidate.insert(0,(0,0))
    limit = limit + 1
    
    dp:list[tuple[int,int]] = [] # dp[a] = (k,i) : recognize until 0_th ~ k_th item and also has the bag max weight (i)
    dp_value_table:list[int] = [] # dp[a] = (k,i) then dp_value_table[a] = v, the solved knapsack problem's value sum
    dp_sack_table:list[list[int]] = [] # exact sack table for dp_value_table, for debuging reason
    def knapsack_set(toItem:int, knapsackMax:int, valueSum:int , currentSack:list[tuple]) -> None:
        nonlocal dp
        nonlocal dp_value_table
        index = -1
        try:
            index = dp.index((k, i))
            dp_value_table[index] = valueSum
        except:
            dp.append((toItem, knapsackMax))
            dp_value_table.append(valueSum)
            dp_sack_table.append(currentSack)
    
    def knapsack_get(k, i) -> tuple[int, list[tuple]]:
        try:
            index = dp.index((k, i))
            return (dp_value_table[index], dp_sack_table[index])
        except:
            return (0, [])
    
    def knapsack_view(k, j):
        dp_view = [[-1 for u in range(j)] for i in range(k)]
        for index in range(len(dp)):
            value = dp_value_table[index]
            i, j = dp[index]
            dp_view[i][j] = value

        for li in dp_view:
            print(li)
            
    def knapsack_view_deep(k, j, opt=0):
        dp_view = [[-1 for u in range(j)] for i in range(k)]
        for index in range(len(dp)):
            value = dp_sack_table[index]
            i, j = dp[index]
            dp_view[i][j] = list(map(lambda x: x[opt],value)) # collect only weight

        for li in dp_view:
            print(li)
    candidate_len = len(candidate)
    for k in range(candidate_len):
        for i in range(limit):
            target_w, target_v = candidate[k]
            if k == 0 or i == 0:
                knapsack_set(k, i, 0, [])
            else:
                # case of knapsack item not changed as before k
                c_li = []
                continue_case, c_li = knapsack_get(k-1, i)
                
                # case of add item to knapsack 
                # (knapsack capable of i 's problem) => (k's value) + (knapsack capable of (i - k's weight) until k-1 th item)
                additive_case = -1
                a_li = []
                if i-target_w > 0:
                    additive_case, a_li = knapsack_get(k-1, i-target_w)
                    additive_case += target_v
                    a_li = a_li + [(target_w, target_v)]

                # compare cases to assign
                res = continue_case
                res_li = c_li
                
                if (additive_case > continue_case):
                    res = additive_case
                    res_li = a_li
                
                knapsack_set(k, i, res, res_li)
    print("weight")
    knapsack_view_deep(candidate_len, limit)
    print("value")
    knapsack_view_deep(candidate_len, limit, opt=1)
    print(candidate_len - 1, limit)
    return knapsack_get(candidate_len - 1, limit - 1)

if __name__ == "__main__":
    
    print("====TEST START====")
    
    Tester.init()
    for i in range(Tester.count):
        put, take = Tester.next()
        
        res = main_edu(candidate=put[Tester.candidate], limit=put[Tester.limit])
        
        print("result : ", res, "answer : ", take)
        
    # first_input = list(map(int, input().split(' ')))
    # candidate = []
    # for i in range(first_input[0]):
    #     candidate.append(tuple(map(int, input().split(' '))))
    # res = main(candidate=candidate, limit=first_input[1])

    # print(res)