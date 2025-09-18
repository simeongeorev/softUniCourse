from collections import deque

materials = list(map(int, input().split()))  # last
magic_levels = deque(map(int, input().split()))  # first

table = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

presents_crafted = {}

while materials and magic_levels:
    current_material = materials[-1]
    current_magic = magic_levels[0]

    if current_material == 0:
        materials.pop()
        continue
    if current_magic == 0:
        magic_levels.popleft()
        continue

    multiplication = materials[-1] * magic_levels[0]

    if multiplication in table.keys(): # happy path
        present = table[multiplication]

        # adding to the dict of presents
        if present not in presents_crafted:
            presents_crafted[present] = 0
        presents_crafted[present] += 1

        materials.pop()
        magic_levels.popleft()

    elif multiplication < 0:
        sum_of_values = current_magic + current_material
        materials.pop()
        magic_levels.popleft()
        materials.append(sum_of_values)
        continue

    elif multiplication > 0 and multiplication not in table.keys():
        magic_levels.popleft()
        materials[-1] += 15

success_flag = False
if "Doll" in presents_crafted.keys() and "Wooden train" in presents_crafted.keys():
    success_flag = True
elif "Teddy bear" in presents_crafted.keys() and "Bicycle" in presents_crafted.keys():
    success_flag = True

if success_flag:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(el) for el in reversed(materials))}")
if magic_levels:
    print(f"Magic left: {', '.join(str(el) for el in magic_levels)}")

for toy, amount in sorted(presents_crafted.items()):
    print(f"{toy}: {amount}")

# Благодаря, че споделихте кода. Нека да разгледаме внимателно логиката и да намерим проблема, поради който един от граничните случаи не минава.
#
# Анализ на кода
#
# Проверка за нула: Когато текущият материал или магия е равно на нула, Вие правилно ги изваждате и продължавате с цикъла. Но едно нещо, което е важно, е да не пропускате проверките за нула между операции. Те трябва да бъдат на подходящи места.
#
#
#
# Работа с deque: Вие използвате deque за магическите нива и list за материалите. Това е вярно, защото искате да изтеглите елементи от началото на магическите нива. Убедете се, че логиката за работа с тях е коректно структуриранa.
#
#
#
# Проверка на произведението: Правилно проверявате произведението за наличие в таблицата и правите операции. Но не забравяйте да добавите логика за опити в случай, че произведението не е нито нула, нито отрицателно, но не е в таблицата.
#
#
#
# Флаг за успех: Логиката за успеха е добре структурирана, но уверете се, че правилно добавяте подаръците в речника presents_crafted.
#
#
# Потенциален проблем
# Един от често срещаните проблеми е, когато произведението е положително, но не е в таблицата и не се обработва правилно. Например, след операцията с добавяне на 15 към материала, уверете се, че проверките продължават.
#
# Предложение за подобрение
# Помислете как можете да добавите проверка, когато материалът или магията е нула, преди да умножите. По този начин можете да избегнете ненужни изчисления.
#
# Ето един частичен пример как да промените логиката за проверка на current_material и current_magic:
#
# if current_material == 0:
#     materials.pop()
#     continue
# if current_magic == 0:
#     magic_levels.popleft()
#     continue
# След това проверете за произведението:
#
# multiplication = current_material * current_magic  # коригирано от materials[-1] * magic_levels[0]
# Следваща стъпка
# Опитайте се да направите тези корекции и проверете дали проблемът с пропуснатия случай продължава. Ако все пак имате проблем, споделете конкретния случай (входни данни), който не работи, за да мога да Ви помогна по-добре!
