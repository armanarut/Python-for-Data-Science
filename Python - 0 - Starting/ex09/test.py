from ft_package import power, average, SayHello, \
    count_in_list, sum, print_toml_data


SayHello("world")
x = power(3, 2)
print("power(3,2) : ", x)
x = average(3, 2)
print("average(3,2) : ", x)
x = sum(3, 2)
print("sum(3,2) : ", x)

print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
print(count_in_list(["toto", "tata", "toto"], "tata"))  # output: 1

print_toml_data()
