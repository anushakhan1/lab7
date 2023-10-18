user_data = set()
num_data_points = int(input("how many data points would you like to enter"))
for i in range(num_data_points)
data = input(f"enter data point(i+1):")
user_data.add(data)
print("data entered by the user")
def new_func(data):
    print(data)

def new_func1(data, new_func):
    new_func(data)

for data in user_data:
    new_func1(data, new_func)
