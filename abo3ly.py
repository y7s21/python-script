def yildiz():
    stars = 10
    for star in range(1, stars + 1):
        print((stars - star) * ' ' + star * '*')


yildiz()