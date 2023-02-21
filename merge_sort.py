from list_impl import List, Elem

def merge(left_list, right_list):
    result = List()
    left_elem = left_list.head
    right_elem = right_list.head

    while left_elem is not None and right_elem is not None:
        if left_elem.val <= right_elem.val:
            result.append(left_elem.val)
            left_elem = left_elem.next
        else:
            result.append(right_elem.val)
            right_elem = right_elem.next

    while left_elem is not None:
        result.append(left_elem.val)
        left_elem = left_elem.next

    while right_elem is not None:
        result.append(right_elem.val)
        right_elem = right_elem.next

    return result

def merge_sort(lst):
    if lst.length() <= 1:
        return lst

    mid = lst.length() // 2
    left_half = List()
    right_half = List()
    curr_elem = lst.head

    for i in range(mid):
        left_half.append(curr_elem.val)
        curr_elem = curr_elem.next

    while curr_elem is not None:
        right_half.append(curr_elem.val)
        curr_elem = curr_elem.next

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)



new_list = List()
new_list.append(4)
new_list.append(2)
new_list.append(5)
new_list.append(1)
new_list.append(3)

print("Unsorted list: ")
print(new_list)

sorted_new_list = merge_sort(new_list)

print("Sorted list: ")
print(sorted_new_list)
