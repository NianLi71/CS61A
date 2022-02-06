HW_SOURCE_FILE = __file__


def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    
    if pos == 0:
        return 0
    else:
        return (pos % 10 == 8) + num_eights(pos // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """

    # return recursion_v1(n)
    # return while_v1(n)
    
    def f(i, pp, delta):
        '''
        这里用递归的方式实现递推，从1递推到n

        pp: step i 得到的pingpong

        pingpong(1) = f(1,1,1)
        pingpong(2) = f(2,2,1)
        '''
        if i == n:
            return pp
        if turn(i):
            return f(i+1, pp + -1*delta, -1*delta)
        else:
            return f(i+1, pp + delta, delta)

    return f(1, 1, 1)

def turn(n):
        if n % 8 == 0 or num_eights(n):
            return True
        else:
            return False

def while_v1(n):
    pp = 1
    direction = 1
    i = 2
    while i <= n:
        pp += direction
        if turn(i):
            direction *= -1
        i += 1
    return pp

def recursion_v1(n):
    def t(n):
        '''
        t(n)实现效率比较低，每次对t(n)的调用，比如计算t(20)，t(19),都需要一直递归到t(8)，
        当然可以用一个cache存储t(n)的中间结果
        '''
        if n == 8:
            return -1
        
        if turn(n):
            return -1 * t(n-1)
        else:
            return t(n - 1)

    if n <= 8:
        return n

    return recursion_v1(n - 1) + t(n - 1)

# if __name__ == '__main__':
#     for i in range(1, 31):
#         print(f'{i}: {pingpong(i)}')

def missing_digits(n):
    """Given a number a that is in sorted, non-decreasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    
    def f(left_of_n, last_digit, missing_cnt):
        if left_of_n == 0:
            return missing_cnt
        
        current_digit = left_of_n % 10
        if current_digit != last_digit:
            missing_cnt += last_digit - current_digit - 1
        return f(left_of_n // 10, current_digit, missing_cnt)

    return f(n // 10, n % 10, 0)

# if __name__ == '__main__':
#     print(missing_digits(4))

def ascending_coin(coin):
    """Returns the next ascending coin in order.
    >>> ascending_coin(1)
    5
    >>> ascending_coin(5)
    10
    >>> ascending_coin(10)
    25
    >>> ascending_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def descending_coin(coin):
    """Returns the next descending coin in order.
    >>> descending_coin(25)
    10
    >>> descending_coin(10)
    5
    >>> descending_coin(5)
    1
    >>> descending_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    
    def f(change, coin):
        '''
        f(change, coin): 代表当前change, 用面额小于等于coin的硬币能找零钱的方式数量
        
        f(change, coin) = f(change - coin, coin) + f(change, descending_coin(coin))
            f(change - coin, coin): 使用当前coin面额硬币一个后找零的方式数量
            f(change, descending_coin(coin)): 不使用当前面额，而使用比当前面额小的硬币找零的方式数量

        例如
        f(15, 10) = f(15-10, 10) + f(10, 5)
            f(15-10, 10) = f(5, 10): 用掉一个10面额硬币后剩余面额5用小于等于10的面额找零方式数量
            f(10, 5): 不同面额10, 用面额<=5硬币找零方式数量

        f(15, 25) = f(15-25, 25) + f(15, 10) = f(15, 10)
            f(15, 10) = f(5, 10) + f(15, 5)
                f(5, 10) = f(5-10, 10) + f(5, 5) = f(5, 5)
                    f(5, 5) = f(5-5, 5) + f(5, 1) = 1 + f(5, 1)
                        f(5, 1) = 1
                    f(5, 5) = 1 + 1 = 2 # 5=5, 5=1+1+1+1+1
                f(5, 10) = f(5, 5) = 2

                f(15, 5) = f(10, 5) + f(15, 1)
                    f(10, 5) = f(5, 5) + f(10, 1) = 2 + 1  # 10=5+5, 10=1+1+1+1+1+1+1+1+1+1
                    f(15, 1) = 1
                f(15, 5) = 4
            f(15, 10) = 2 + 4 = 6
        f(15, 25) = 6
        '''

        if coin == 1:
            return 1
        if change == 0:
            return 1

        if change - coin < 0:
            return f(change, descending_coin(coin))
        else:
            return f(change - coin, coin) + f(change, descending_coin(coin))

    return f(change, coin=25)

if __name__ == '__main__':
    print(count_coins(200))

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"


from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
