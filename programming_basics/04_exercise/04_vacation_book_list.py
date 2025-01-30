#     1. Брой страници в текущата книга – цяло число в интервала [1…1000]
#     2. Страници, които прочита за 1 час – цяло число в интервала [1…1000]
#     3. Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]

pages_total = int(input())
pages_per_hour = int(input())
days_to_finish_book = int(input())

required_hours_per_day = (pages_total / pages_per_hour) // days_to_finish_book

print(required_hours_per_day)
