def test2(a, b, *args, **kwargs):
    print("-" * 10)
    print(a)
    print(b)
    print(args)
    print(kwargs)


def test1(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

    # test2(a, b, args, kwargs)
    test2(a, b, *args, **kwargs)

test1(1, 2, 3, 4, 5, 6, name="laowang", age=10)
