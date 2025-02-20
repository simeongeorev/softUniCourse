import math

centuries = int(input())

years_in_cent = 100
days_in_year = 365.24
hours_in_day = 24
minutes_in_hour = 60

days_in_century = days_in_year * years_in_cent
hours_in_century = days_in_century * hours_in_day
minutes_in_century = hours_in_century * minutes_in_hour

print(f"{centuries} centuries ="
      f" {centuries * years_in_cent} years ="
      f" {centuries * days_in_century:.0f} days ="
      f" {centuries * hours_in_century:.0f} hours ="
      f" {centuries * minutes_in_century:.0f} minutes")

# I give up!!!!


