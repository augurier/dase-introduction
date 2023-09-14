a = float(input("请输入数字："))
left = 0
right = a
mid = 0
while(left < right):
    mid = (left + right) / 2
    mid3 = mid * mid * mid
    if mid3 < a:
        left = mid
    elif mid3 > a:
        right = mid
    if mid3 - a < 0.0000001 and mid3 - a > -0.0000001:
        break
print(mid)