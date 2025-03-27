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
import random

class Tester:
    def __init__(self):
        self.test_cases = []

    def add_case(self, case):
        """
        arg:
            case -> list of integer, the numbers that Baekjoon shout out
        """
        self.test_cases.append(case)

    def test_all(self, main_func):
        for i in range(len(self.test_cases)):
            print(f"case {i+1} in {len(self.test_cases)}")
            print(f"case: {self.test_cases[i]}")
            print("ans : ",main_func(self.test_cases[i]))

    def compare_all(self, main_func, compare_func):
        for i in range(len(self.test_cases)):
            print(f"case {i+1} in {len(self.test_cases)}")
            print(f"case: {self.test_cases[i]}")
            main_res = main_func(self.test_cases[i])
            comp_res = compare_func(self.test_cases[i])
            print("ans : ",main_res)
            print("comp : ",comp_res)
            for i in range(len(main_res)):
                if comp_res[i] != main_res[i]:
                    input("잘못되었습니다!")


def main_binary_injection(case):
    def see_where_to_inject(li, to_inject):
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


    def get_middle(li):
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

def main(case):
    def heap_get_parent_index(i:int):
        return (i - 1) // 2
    def heap_get_left_child_index(i:int):
        return 2 * i + 1
    def heap_get_right_child_index(i:int):
        return 2 * i + 2
    
    def sift_up(heap:list[int], i:int, is_max_heap=True):
        me = i
        parent = heap_get_parent_index(me)
        while me > 0:
            if is_max_heap and heap[me] <= heap[parent]:
                return
            if is_max_heap != True and heap[me] >= heap[parent]:
                return
            grab_parent = heap[parent]
            heap[parent] = heap[me]
            heap[me] = grab_parent
            
            me = parent
            parent = heap_get_parent_index(me)
    
    def sift_down(heap:list[int], i:int, is_max_heap = True):
        me = i
        while me < len(heap):
            child_left = heap_get_left_child_index(me)
            child_right = heap_get_right_child_index(me)
            if len(heap) <= child_left or len(heap) <= child_right:
                if len(heap) > child_left:
                    if is_max_heap:
                        if heap[me] >= heap[child_left]:
                            return
                        else:
                            grab_left_child = heap[child_left]
                            heap[child_left] = heap[me]
                            heap[me] = grab_left_child
                            return
                    else:
                        if heap[me] <= heap[child_left]:
                            return
                        else:
                            grab_left_child = heap[child_left]
                            heap[child_left] = heap[me]
                            heap[me] = grab_left_child
                            return 
                return
            if is_max_heap and heap[me] >= heap[child_left] and heap[child_left] >= heap[child_right]:
                return
            if is_max_heap == False and heap[me] <= heap[child_left] and heap[child_left] <= heap[child_right]:
                return
            grab_left_child = heap[child_left]
            grab_right_child = heap[child_right]
            if is_max_heap:
                if grab_left_child >= grab_right_child:
                    heap[child_left] = heap[me]
                    heap[me] = grab_left_child
                    me = child_left
                else:
                    heap[child_right] = grab_left_child
                    heap[child_left] = grab_right_child
                    
                    heap[child_right] = heap[me]
                    heap[me] = grab_right_child
                    me = child_right
                    
            else:
                if grab_left_child <= grab_right_child:
                    heap[child_left] = heap[me]
                    heap[me] = grab_left_child
                    me = child_left
                else:
                    heap[child_right] = grab_left_child
                    heap[child_left] = grab_right_child
                    
                    heap[child_right] = heap[me]
                    heap[me] = grab_right_child
                    me = child_right
                    
    
    def push(heap: list[int], i:int, is_max_heap=True):
        heap.append(i)
        # print("heap: ",heap, "item: ",i)
        sift_up(heap, len(heap) - 1, is_max_heap=is_max_heap)

    def extrude_root(heap: list[int], is_max_heap=True):
        res = heap[0]
        heap[0] = heap[-1]
        heap.pop(-1)
        sift_down(heap, 0, is_max_heap=is_max_heap)
        return res
    
    # define heap. max heap is for lower values, min hip is for higher values
    max_heap = []
    min_heap = []
    temporary_storage = []
    
    def push_called(call:int):
        
        # null catching
        if len(max_heap) == 0 or len(min_heap) == 0:
            temporary_storage.append(call)
            if len(temporary_storage) == 2:
                i1 = temporary_storage[0]
                i2 = temporary_storage[1]
                if i1 < i2:
                    push(max_heap, i1)
                    push(min_heap, i2)
                else:
                    push(max_heap, i2)
                    push(min_heap, i1)
            return
        
        # pushing stage
        if call < max_heap[0] and call < min_heap[0]:
            push(max_heap, call)
        else: 
            push(min_heap, call, is_max_heap=False)
            
        # balancing stage
        delta = len(max_heap) - len(min_heap)
        if delta > 1:
            for i in range(delta - 1):
                popped = extrude_root(max_heap)
                push(min_heap, popped, is_max_heap=False)
        elif delta < -1:
            for i in range(-delta - 1):
                popped = extrude_root(min_heap, is_max_heap=False)
                push(max_heap, popped)

    res = []
    for call in case:
        push_called(call)
        print(max_heap, min_heap)
        if (len(max_heap) == 0 and len(min_heap) == 0):
            res.append(temporary_storage[0])
            continue
        
        if len(max_heap) == len(min_heap):
            res.append(max_heap[0])
        else:
            if len(max_heap) < len(min_heap):
                res.append(min_heap[0])
            else:
                res.append(max_heap[0])
    
    return res
        

tester = Tester()


## arbitrary testing section
tester.add_case([19, 42, 46, 81, 46, 78, 38, -59, -2, 8])
tester.add_case([-16, -28, -96, -91, -66, -23, -24, 95, 22, 54])
tester.add_case([-59, 68, -9, 58, 59, 41, -81, -92, -75, -10])
tester.compare_all(main, main_binary_injection)

## random testing section
# for i in range(100):
#     tes = []
#     for i in range(10):
#         tes.append(random.randint(-100,100))
#     tester.add_case(tes)

# tester.compare_all(main, main_binary_injection)

## real running code
# input_num = int(input())
# input_list = []
# for i in range(input_num):
#     input_list.append(int(input()))

# answer_list = main(input_list)
# for ans in answer_list:
#     print(ans)