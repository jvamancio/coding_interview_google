def merge_sort(arr):
    if len(arr) > 1:
        
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        merge(arr, left_half, right_half)

def merge(arr, left_half, right_half):

    top_left = top_right = k = 0

    while top_left < len(left_half) and top_right < len(right_half):

        if left_half[top_left] < right_half[top_right]:
            arr[k] = left_half[top_left]
            top_left += 1

        else:
            arr[k] = right_half[top_right]
            top_right += 1

        k += 1
    
    while top_left < len(left_half):
        arr[k] = left_half[top_left]
        top_left += 1
        k += 1

    # Verifica se algum elemento foi deixado para trás na metade direita
    while top_right < len(right_half):
        arr[k] = right_half[top_right]
        top_right += 1
        k += 1

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Array original:")
    print(arr)
    merge_sort(arr)
    print("Array ordenado:")
    print(arr)
