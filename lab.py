# LAB_RECURSION_LAMBDA

## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

#### Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase . 
#### Example: given the phrase `I love python` , it should return : `4`

def count_vowels(s):
    if s == "":
        return 0
    elif s[0] in "aeiouAEIOU":
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])
    
## 2) Given a list of numbers : `[40,35, 10, 15, 20]`

#### create a new list containing each number from the previous list mutliplied by itself.
#### print the new list.
#### Note: use `map()` with a `lambda funciton`
def main():
    lines = [
    "hello",
    "programming",
    "sky",
    "computer",
    "queue",
    "algorithm",
    "strength",
    "aeiou",
    "bcdfg",
    "I love python"
]
    for line in lines:
        vowels_count = count_vowels(line)
        print(f"The number of vowels in the string \"{line}\" is: {vowels_count}")

    print()
    print()
    print("Task 2:")
    numbers = [1,2,3,4,5,6,7,8,9]
    new_numbers = map(lambda x: x*x, numbers)
    print(numbers)
    print(list(new_numbers))


if __name__ == "__main__":
    main()