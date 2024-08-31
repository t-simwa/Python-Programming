
#  Write a function `collect_data` that accepts any number of data points and returns a list of those points.

def collect_data(*data_points):
    return list(data_points)

print(collect_data(10, 20, 30, 40))          # Output: [10, 20, 30, 40]
print(collect_data("a", "b", "c", "d"))      # Output: ['a', 'b', 'c', 'd']