# Selection Sort fucntion
def selection_sort(arrary):
    def find_smallest_value(arr):
        smallest_value = arr[0]
        smallest_index = 0
        for el in range(1, len(arr)):
            if arr[el] < smallest_value:
                smallest_value = arr[el]
                smallest_index = el
        return smallest_index

    sorted_list = []
    for i in range(len(arrary)):
        smallest = find_smallest_value(arrary)
        sorted_list.append(arrary.pop(smallest))
    return sorted_list







