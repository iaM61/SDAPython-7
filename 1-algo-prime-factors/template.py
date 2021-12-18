from typing import List

primes = [2, 3, 5, 7, 11, 13, 17]

List = []
def get_prime_factors(n: int) -> List[int]:
    for i in primes:
        if n % i == 0:
            List.append(i)
    return []


# <editor-fold defaultstate="collapsed" desc="Tests">
def test_prime_factors():
    assert sorted(get_prime_factors(1)) == []
    assert sorted(get_prime_factors(4)) == [2, 2]
    assert sorted(get_prime_factors(17)) == [17]
    assert sorted(get_prime_factors(27)) == [3, 3, 3]
# </editor-fold>
