tail, body, head = input(), input(), input()

meerkat = [tail, body, head]

meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)