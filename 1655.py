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

from curses import nonl
import math
import random
from typing import override

from regex import R

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


def main_brute_force(case):
    current = []
    res = []
    for num in case:
        current.append(num)
        current.sort()
        median = math.floor(len(current) / 2)
        if len(current) % 2 == 0:
            median -= 1
        res.append(current[median])
    return res

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

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def heap_get_parent_index(self, index):
        return (index - 1) // 2
    def heap_get_left_child_index(self, index):
        return 2 * index + 1
    def heap_get_right_child_index(self, index):
        return 2 * index + 2

    def sift_up(self, index):
        me = index
        while me > 0:
            parent = self.heap_get_parent_index(me)
            if self.heap[me] <= self.heap[parent]:
                return
            grab_parent = self.heap[parent]
            self.heap[parent] = self.heap[me]
            self.heap[me] = grab_parent
            
            me = parent
    def sift_down(self, index):
        me = index
        while me < len(self.heap):
            left_child = self.heap_get_left_child_index(me)
            right_child = self.heap_get_right_child_index(me)
            
            if left_child >= len(self.heap) and right_child >= len(self.heap):
                return
            elif left_child >= len(self.heap):
                if self.heap[right_child] >= self.heap[me]:
                    right_child_value = self.heap[right_child]
                    self.heap[right_child] = self.heap[me]
                    self.heap[me] = right_child_value
                    me = right_child
                    continue
                return
            elif right_child >= len(self.heap):
                if self.heap[left_child] >= self.heap[me]:
                    left_child_value = self.heap[left_child]
                    self.heap[left_child] = self.heap[me]
                    self.heap[me] = left_child_value
                    me = left_child
                    continue
                return
            
            left_child_value = self.heap[left_child]
            right_child_value = self.heap[right_child]
            
            if left_child_value >= self.heap[me] and left_child_value >= right_child_value:
                self.heap[left_child] = self.heap[me]
                self.heap[me] = left_child_value
                me = left_child
            elif right_child_value >= self.heap[me] and right_child_value >= left_child_value:
                self.heap[right_child] = self.heap[me]
                self.heap[me] = right_child_value
                me = right_child
            else:
                return
    
    def push(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)
    def extrude_root(self):
        res = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop(-1)
        self.sift_down(0)
        return res

class MinHeap(MaxHeap):
    def sift_down(self, index):
        me = index
        while me < len(self.heap):
            left_child = self.heap_get_left_child_index(me)
            right_child = self.heap_get_right_child_index(me)
            
            if left_child >= len(self.heap) and right_child >= len(self.heap):
                return
            elif left_child >= len(self.heap):
                if self.heap[right_child] <= self.heap[me]:
                    right_child_value = self.heap[right_child]
                    self.heap[right_child] = self.heap[me]
                    self.heap[me] = right_child_value
                    me = right_child
                    continue
                return
            elif right_child >= len(self.heap):
                if self.heap[left_child] <= self.heap[me]:
                    left_child_value = self.heap[left_child]
                    self.heap[left_child] = self.heap[me]
                    self.heap[me] = left_child_value
                    me = left_child
                    continue
                return
            
            left_child_value = self.heap[left_child]
            right_child_value = self.heap[right_child]
            
            if left_child_value <= self.heap[me] and left_child_value <= right_child_value:
                self.heap[left_child] = self.heap[me]
                self.heap[me] = left_child_value
                me = left_child
            elif right_child_value <= self.heap[me] and right_child_value <= left_child_value:
                self.heap[right_child] = self.heap[me]
                self.heap[me] = right_child_value
                me = right_child
            else:
                return
    
    def sift_up(self, index):
        me = index
        while me > 0:
            parent = self.heap_get_parent_index(me)
            if self.heap[me] >= self.heap[parent]:
                return
            grab_parent = self.heap[parent]
            self.heap[parent] = self.heap[me]
            self.heap[me] = grab_parent
            
            me = parent

def main(case):
    max_heap = MaxHeap()
    min_heap = MinHeap()
    temporary_storage = []
    
    def push_called(call):
        nonlocal max_heap
        nonlocal min_heap
        nonlocal temporary_storage
        # null catching
        if len(max_heap.heap) == 0 or len(min_heap.heap) == 0:
            temporary_storage.append(call)
            if len(temporary_storage) == 2:
                i1 = temporary_storage[0]
                i2 = temporary_storage[1]
                if i1 < i2:
                    max_heap.push(i1)
                    min_heap.push(i2)
                else:
                    max_heap.push(i2)
                    min_heap.push(i1)
            return
        
        # pushing stage
        if call <= max_heap.heap[0] and call <= min_heap.heap[0]:
            max_heap.push(call)
        elif call >= max_heap.heap[0] and call >= min_heap.heap[0]:
            min_heap.push(call)
        else:
            # balancing
            delta = len(max_heap.heap) - len(min_heap.heap)
            if delta >= 0:
                min_heap.push(call)
            elif delta < 0:
                max_heap.push(call)
                
        # balancing stage
        delta = len(max_heap.heap) - len(min_heap.heap)
        if delta > 1:
            for i in range(delta - 1):
                popped = max_heap.extrude_root()
                min_heap.push(popped)
        elif delta < -1:
            for i in range(-delta - 1):
                popped = min_heap.extrude_root()
                max_heap.push(popped)

    res = []
    for call in case:
        push_called(call)
        if (len(max_heap.heap) == 0 and len(min_heap.heap) == 0):
            res.append(temporary_storage[0])
            continue
        
        if len(max_heap.heap) == len(min_heap.heap):
            res.append(max_heap.heap[0])
        else:
            if len(max_heap.heap) <= len(min_heap.heap):
                res.append(min_heap.heap[0])
            else:
                res.append(max_heap.heap[0])
    
    return res
        

# tester = Tester()


## arbitrary testing section

# tester.add_case([-59, 68, -9, 58, 59, 41, -81, -92, -75, -10])
# tester.compare_all(main, main_brute_force)

# # random testing section
# for i in range(100):
#     tes = []
#     for i in range(10):
#         tes.append(random.randint(-100,100))
#     tester.add_case(tes)

# tester.compare_all(main, main_binary_injection)

# real running code
input_num = int(input())
input_list = []
for i in range(input_num):
    input_list.append(int(input()))

answer_list = main(input_list)
for ans in answer_list:
    print(ans)