# Create a list of integers (0-50) using list comprehension
%timeit nums_list_comp = [num for num in range(0,51)]

# Create a list of integers (0-50) using list comprehension
%timeit nums_list_comp = [num for num in range(51)]

# Create a list of integers (0-50) by unpacking range
%timeit nums_unpack = [*range(51)]

# Create a list of integers (0-50) using list comprehension
%timeit nums_list_comp = [num for num in range(0,51)]

# Create a list of integers (0-50) using list comprehension
%timeit nums_list_comp = [num for num in range(51)]

# Create a list of integers (0-50) by unpacking range
%timeit nums_unpack = [*range(51)]

# Create a list using the formal name
%timeit formal_list = list()

# Create a list using the literal syntax
%timeit literal_list = []

#compare the following techniques

%%timeit
hero_wts_lbs = []
for wt in wts:
    hero_wts_lbs.append(wt * 2.20462)

%%timeit
wts_np = np.array(wts)
hero_wts_lbs_np = wts_np * 2.20462
