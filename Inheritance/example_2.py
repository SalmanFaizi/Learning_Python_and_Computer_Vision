class A:
    def m1(self):
        return 20

class B(A):
    def m1(self):
        val=super().m1() + 30
        return 30



class C(B):
    def m1(self):
        val=self.m1() + 20 # this is an infinite recursion
        return val

obj1=C()
print(obj1.m1())

# 20+30+20=70