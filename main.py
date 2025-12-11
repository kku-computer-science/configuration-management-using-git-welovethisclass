from quick_sort import quick_sort
from bubble_sort import bubble_sort

def main():

    raw = input("ป้อนตัวเลขที่ต้องการเรียงลำดับ (คั่นด้วยช่องว่าง): ")
    arr =list(map(int, raw.split()))

    choice = input("เลือกวิธีการเรียงลำดับ (QuickSort/ Bubble): ").lower()

    if choice == "quicksort":
        quick_sort(arr, 0, len(arr) - 1)
        print("ผลลัพธ์การเรียงลำดับด้วย QuickSort:", arr)
    elif choice == "bubble":
        result = bubble_sort(arr)
        print("ผลลัพธ์การเรียงลำดับด้วย Bubble Sort:", result)
    else:
        print("วิธีการเรียงลำดับที่เลือกไม่ถูกต้อง")

if __name__ == "__main__":
    main()
