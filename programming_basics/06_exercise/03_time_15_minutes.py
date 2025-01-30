# 03_time_15_minutes

# Да се напише програма, която чете час и минути от 24-часово денонощие, въведени от потребителя и изчислява колко ще е часът след 15 минути.
# Резултатът да се отпечата във формат часове:минути. Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59.
# Часовете се изписват с една или две цифри. Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.

hours = int(input())
mins_str = str(input())

mins = int(mins_str)

time_wanted = mins + 15

if time_wanted > 59:
    hours += 1
    mins = time_wanted - 60
else:
    mins = time_wanted
    
if hours > 23:
    hours = 0

if mins < 10:
    print(f"{hours}:0{mins}")
else:
    print(f"{hours}:{mins}")