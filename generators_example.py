numbers = [1, 2, 3, 4, 5]

numbers_generator = ([number * 2 for number in numbers])
print(numbers_generator)
# print(next(numbers_generator))
# print(next(numbers_generator))
# print(next(numbers_generator))

def number_generator_long(number_list: list[int]):
    for number in number_list:
        yield number * 2



my_generator = number_generator_long(numbers)
print(my_generator) 
# print(next(my_generator))  

# print([*my_generator])

print(*[1, 2, 3])
print(1, 2, 3)
