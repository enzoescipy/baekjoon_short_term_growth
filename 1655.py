# 문제
# 백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다. 만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

# 예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 백준이가 외치는 정수의 개수 N이 주어진다. N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다. 그 다음 N줄에 걸쳐서 백준이가 외치는 정수가 차례대로 주어진다. 정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.

# 출력
# 한 줄에 하나씩 N줄에 걸쳐 백준이의 동생이 말해야 하는 수를 순서대로 출력한다.

# 예제 입력 1 
# 7
# 1
# 5
# 2
# 10
# -99
# 7
# 5
# 예제 출력 1 
# 1
# 1
# 2
# 2
# 2
# 2
# 5

import math

class Tester:
    def __init__(self) -> None:
        self.test_cases : list = []

    def add_case(self, case:list[int]) -> None:
        """
        arg:
            case -> list of integer, the numbers that Baekjoon shout out
        """
        self.test_cases.append(case)

    def test_all(self, main_func) -> None:
        for case in self.test_cases:
            print(main_func(case))



def main(case:list[int]):

    def see_where_to_inject(li:list[int], to_inject:int) -> int:
        # input(f"target : {target}")
        """
        calculate where to inject the to_inject integer to the sorted list, the target.
        Returns:
            -> int : the index of target. if target.insert(res, to_insert) then it is the proper place injection.
        """
        if (len(li) == 0):
            # print("zero")
            return 0

        # grab the middle index
        target_len = len(li)
        middle_index = math.floor(target_len / 2)
        middle_value = li[middle_index]
        if (to_inject < middle_value):
            # print("low")
            return see_where_to_inject(li[0 : middle_index],to_inject)
        elif(middle_value < to_inject):
            # print("hi")
            return middle_index + 1 + see_where_to_inject(li[middle_index+1 : ],to_inject)
        else:
            # print("eq")
            return middle_index


    def get_middle(li: list[int]) -> int | None:
        """
        get the median of the list
        Returns:
            -> int : the median of the list.
            -> None : li is empty
        """
        if (len(li) == 0):
            return -1

        target_len = len(li)
        middle_index = math.floor(target_len / 2)
        if target_len % 2 == 0:
            middle_index -= 1

        return li[middle_index]


    memory = [] # which is current sorted list
    shout_out_queue = [] # which is the answer
    for call in case: # call is the integer
        # print("memory : ", memory, "call: ", call)
        index = see_where_to_inject(memory, call)
        # print("index : ", index)
        memory.insert(index, call)

        res = get_middle(memory)
        shout_out_queue.append(res)
        # print(res, memory)
    return shout_out_queue





input_num = int(input())
input_list:list[int] = []
for i in range(input_num):
    input_list.append(int(input()))

answer_list = main(input_list)
for ans in answer_list:
    print(ans)