arr = [3, 9, 2, 1, 4, 5]

class Node:
    def __init__(self, value):
        self.__value = value
        self.ptr = None

class MaxHeap:

    def __init__(self, array):
        self.__arr = self.heapify(array)
        # self.__arr = array
        

    def get_arr(self):
        return self.__arr

    
    def insert(self, value):
        self.__arr.append(value)
        self.__arr = self.heapify(self.__arr)
        return value
    
    def delete(self, value):
        try:
            i = self.__arr.index(value)
            size = len(self.__arr)
            first_nonleaf_index = size // 2 - 1
            if i > first_nonleaf_index:
                del self.__arr[i]
            else:    
                self.__arr[i], self.__arr[size-1] = self.__arr[size-1], self.__arr[i]
                self.__arr.pop()
        except ValueError:
            raise ValueError(f"{value} is not in the heap")
        

    def heapify(self, arr):
        size = len(arr)
        copy_arr = arr.copy()

        first_nonleaf_index = size//2 - 1
        for i in range(first_nonleaf_index, -1, -1):
            max_index = i
            left_child_index = 2 * i + 1
            right_child_index = 2 * i + 2

            if copy_arr[left_child_index] > copy_arr[max_index]:
                max_index = left_child_index
            if right_child_index < size and copy_arr[right_child_index] > copy_arr[max_index]:
                max_index = right_child_index
            
            copy_arr[i], copy_arr[max_index] = copy_arr[max_index], copy_arr[i]
        return copy_arr

max_heap = MaxHeap(arr)
print(max_heap.get_arr())

max_heap.insert(7)
print(max_heap.get_arr())

# max_heap.delete(3)
# print(max_heap.get_arr())

