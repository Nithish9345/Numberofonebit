class NumberOfOne:
    def check(self, a):
        count = 0
        while a != 0 and a != 1:
            if a % 2 == 1:
                count += 1
            a //= 2

        if a == 1:
            count += 1

        return count

a = int(input())
object = NumberOfOne()
print(object.check(a))