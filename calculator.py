class Calculator:
    def add(self, x, y):
        """2つの数値を加算する"""
        return x + y

    def subtract(self, x, y):
        """2つの数値を減算する"""
        return x - y

    def multiply(self, x, y):
        """2つの数値を乗算する"""
        return x * y

    def divide(self, x, y):
        """2つの数値を除算する"""
        if y == 0:
            raise ValueError("0での除算はできません")
        return x / y
