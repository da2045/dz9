# def calculate_product(numbers):
#     product = 1
#     for num in numbers:
#         product *= num
#     return product




# my_list = [2, 3, 5, 7]
# result = calculate_product(my_list)
# print(f"Добуток елементів списку {my_list} дорівнює {result}.")

# def find_minimum(numbers):
#     if not numbers:
#         return None  
#     return min(numbers)

# # Приклад використання функції
# my_list = [5, 2, 8, 1, 10]
# result = find_minimum(my_list)
# print(f"Мінімальне число у списку {my_list} дорівнює {result}.")





# def is_prime(n):
   
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def count_primes(numbers):
   
#     count = 0
#     for num in numbers:
#         if is_prime(num):
#             count += 1
#     return count

# my_list = [2, 3, 5, 7, 10, 11, 13]
# result = count_primes(my_list)
# print(f"Кількість простих чисел у списку {my_list} дорівнює {result}.")




# def remove_number_from_list(numbers, target):
#     count_removed = numbers.count(target)
#     numbers = [num for num in numbers if num != target]
#     return count_removed

# my_list = [2, 3, 5, 7, 5, 10, 5, 11]
# number_to_remove = 5
# removed_count = remove_number_from_list(my_list, number_to_remove)
# print(f"З числа {number_to_remove} було видалено {removed_count} разів.")
# print(f"Оновлений список: {my_list}")





# def merge_lists(list1, list2):
#     return list1 + list2

# my_list1 = [1, 2, 3]
# my_list2 = [4, 5, 6]
# merged_list = merge_lists(my_list1, my_list2)
# print(f"Об'єднаний список: {merged_list}")




# def calculate_powers(numbers, exponent):

#     return [num ** exponent for num in numbers]

# my_list = [2, 3, 5, 7]
# exponent_value = 2
# result_list = calculate_powers(my_list, exponent_value)
# print(f"Список піднесений до ступеня {exponent_value}: {result_list}")
