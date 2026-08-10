def generate_sequence(index , subset , phone_number , result , value):
    if index >= len(value):
        result.append(subset.copy())
        return 
    for val in phone_number[int(value[index])]:
        subset.append(val)
        generate_sequence(index+1 , subset , phone_number , result , value)
        subset.pop()

phone_numbber = {
    2 : "abc",
    3 : "def",
    4 : "ghi",
    5 : "jkl",
    6 : "mno",
    7 : "pqrs",
    8 : "tuv",
    9 : "wxyz"
}
index = 0
subset = []
result = []
value = "24"
generate_sequence(index , subset , phone_numbber , result , value)
print(result)