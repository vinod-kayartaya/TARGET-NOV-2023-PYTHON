"""
Example for list `slice` operations and `comprehension`
"""


def main():
    nums = [19, 29, 93, 91, 92, 94, 91, 48, 59, 58]
    # index starts from 0 and len(nums)-1
    # accessing element at index 3
    print(f'element at index 3 is {nums[3]}')
    print(f'last element in the list {nums[-1]}')
    # accessing a part of the list
    print(f'elements from index 2 to index 6 are {nums[2:7]}')
    # all elements from index 0 to 6
    print(nums[0:7])
    print(nums[:7])
    # all elements from index 5 till the end
    print(nums[5:100000])  # assuming there are less than 100000 elements
    print(nums[5:])
    # all elements; same as `nums`
    print(nums[:])
    # elements at `even` indexes
    print(nums[0:100000:2])
    print(nums[0::2])
    print(nums[::2])
    # elements at `odd` indexes
    print(nums[1:100000:2])
    print(nums[1::2])
    print(nums[::-1])

    even_nums = [n for n in nums if n % 2 == 0]
    print(even_nums)
    odd_nums = [n for n in nums if n % 2]
    print(odd_nums)
    squares = [n*n for n in nums]
    print(squares)


if __name__ == '__main__':
    main()
