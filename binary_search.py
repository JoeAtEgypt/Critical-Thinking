from inputs import *


def max_powder(n, k, needs, haves, max_cookies):
    def is_ok(cookies_count):
        temp_k = k
        for i in range(n):
            current_needs = needs[i] * cookies_count
            if current_needs > haves[i]:
                difference = abs(current_needs - haves[i])
                if temp_k >= difference:
                    temp_k -= difference
                else:
                    return False
        return True

    l, h = 0, max_cookies

    while l < h:
        mid = (h + l + 1) // 2
        if is_ok(cookies_count=mid):
            l = mid
        else:
            h = mid - 1
    return l


if __name__ == "__main__":
    n, k = input_integers(2)
    needs, haves = input_array(n), input_array(n)
    max_cookies = 2 * 10**9

    print(max_powder(n, k, needs, haves, max_cookies))
