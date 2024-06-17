class CombinationCalculator:
    def __init__(self, max_n, mod=998244353):
        self.max_n = max_n
        self.mod = mod
        self.fact = [1] * (max_n + 1)
        self.ifact = [1] * (max_n + 1)
        self._precompute_factorials()

    def _precompute_factorials(self):
        for i in range(self.max_n):
            self.fact[i + 1] = self.fact[i] * (i + 1) % self.mod
        self.ifact[self.max_n] = pow(self.fact[self.max_n], -1, self.mod)
        for i in range(self.max_n, 0, -1):
            self.ifact[i - 1] = self.ifact[i] * i % self.mod

    def comb(self, n, k):
        if k > n or k < 0:
            return 0
        return self.fact[n] * self.ifact[k] % self.mod * self.ifact[n - k] % self.mod
