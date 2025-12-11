from quick_sort import quick_sort
from bubble_sort import bubble_sort

def main():

    raw = input("ป้อนตัวเลขที่ต้องการเรียงลำดับ (คั่นด้วยช่องว่าง): ")
    arr =list(map(int, raw.split()))

    i = input("เลือกวิธีการเรียงลำดับ QuickSort (1)/ Bubble(2): ")
    choice = int(i)

    if choice == 1:
        quick_sort(arr, 0, len(arr) - 1)
        print("ผลลัพธ์การเรียงลำดับด้วย QuickSort:", arr)
<<<<<<< HEAD
    elif choice == 2:
=======
    elif choice == "bubble":
>>>>>>> refs/remotes/origin/main
        bubble_sort(arr)
        print("ผลลัพธ์การเรียงลำดับด้วย Bubble Sort:", arr)
    else:
        print("วิธีการเรียงลำดับที่เลือกไม่ถูกต้อง")

if __name__ == "__main__":
    main()
