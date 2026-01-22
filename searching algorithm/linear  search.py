#Implementing linear search algorithm
def search(arr, x):
    l = len(arr)
    for i in range(len(arr)):
        if arr[i] == x:
            return i


if __name__ == "__main__":
   arr =[3,4,5,7,20,9]
   x = 20
   result = search(arr, x)
   if result == -1:
       print("value not found")
   else:
       print("value found at index:", result)



