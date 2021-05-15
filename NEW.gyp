
def get_y(m, b, x):
  y = m*x + b
  return y

get_y(1, 0, 7) == 7
get_y(5, 10, 3) == 25

def calculate_error(m, b, point):
  x_point, y_point = point
  y = m*x_point + b
  distance = abs(y - y_point)
  return distance

#Testing:
print(calculate_error(1, 0, (3, 3)))
print(calculate_error(1, 0, (3, 4)))
print(calculate_error(1, -1, (3, 3)))
print(calculate_error(-1, 1, (3, 3)))

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

def calculate_all_error(m, b, points):
    total_error = 0
    for point in datapoints:
        point_error = calculate_error(m, b, point)
        total_error += point_error
    return total_error

#Testing:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))
print(calculate_all_error(1, 1, datapoints))
print(calculate_all_error(1, -1, datapoints))
print(calculate_all_error(-1, 1, datapoints))


possible_ms = [m * 0.1 for m in range(-100, 101)]
possible_bs = [b * 0.1 for b in range(-200, 201)]

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("inf")
best_m = 0
best_b = 0

for m in possible_ms:
    for b in possible_bs:
   	 error = calculate_all_error(m, b, datapoints)
   	 if error < smallest_error:
   		 best_m = m
   		 best_b = b
   		 smallest_error = error
       	 
print(best_m, best_b, smallest_error)

#the line that fits the data best has an m of 0.3 and a b of 1.7:
get_y(0.3, 1.7, 6)



