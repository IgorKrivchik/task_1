# При помощи ф-ции filter() из кортежа слов отфильтровать,
# только те,которые читаются одинаково в обе стороны

tuple_list = ("абба","анна","перо","фильтр","алла", "мася",)
my_list = list (tuple_list)
result = list(filter(lambda x: (x == "".join(reversed(x))), my_list)) 
print (result)
