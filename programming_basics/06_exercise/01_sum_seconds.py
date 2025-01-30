a_seconds = int(input())
b_seconds = int(input())
c_seconds = int(input())
  
sum = a_seconds + b_seconds + c_seconds

minutes = sum // 60
seconds_left = sum % 60

if seconds_left < 10:
    print(f"{minutes}:0{seconds_left}")
else:
    print(f"{minutes}:{seconds_left}")