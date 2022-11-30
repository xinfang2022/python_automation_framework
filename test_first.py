import pytest




def inc(x):
    return x + 1


def test_baidu(test_url):
    print(test_url)


def test_inc():
    assert inc(3) == 4

# if __name__ == '__main__':
#     pytest.main()
breakpoint()