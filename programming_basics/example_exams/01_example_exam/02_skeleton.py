control_minutes = int(input())
control_seconds = int(input())
ulei_length_meters = float(input())
seconds_to_cross_100_meters = int(input())

# на всеки 120 метра неговото време намаля с 2.5 секунди.

total_control_seconds = control_minutes * 60 + control_seconds # control time in seconds

delay_time_seconds = (ulei_length_meters / 120) * 2.5

seconds_to_cross_1_meter = seconds_to_cross_100_meters / 100
marin_time_to_cross_seconds = ulei_length_meters * seconds_to_cross_1_meter - delay_time_seconds

if marin_time_to_cross_seconds <= total_control_seconds:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {marin_time_to_cross_seconds:.3f}.")
else:
    print(f"No, Marin failed! He was {marin_time_to_cross_seconds - total_control_seconds:.3f} second slower.")

