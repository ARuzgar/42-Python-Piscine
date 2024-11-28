ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Modifying list
ft_list[1] = "World!"

# Modifying tuple (by converting to list, updating, then converting back to tuple)
mutateTuple = list(ft_tuple)
mutateTuple[1] = "Turkiye!"
ft_tuple = tuple(mutateTuple)

# Modifying set
ft_set.discard("tutu!")
ft_set.add("Istanbul!")

# Modifying dictionary
ft_dict["Hello"] = "42 Istanbul!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)