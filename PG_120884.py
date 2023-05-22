def solution(chicken):
    res = 0
    coupon = chicken

    while coupon >= 10:
        service = coupon // 10
        res += service
        coupon = service + coupon % 10

    return res
