import pytest

def fibonacci_index(n):


    x = 0;
    y = 1;
    s = 1;
    i = 1;

    while(s < n):
        s = x + y;

        i = i + 1;
        x = y;
        y = s;

    return i;


def fact(n):

    if(n == 0):
        return 1;
    if(n == 1):
        return 1;

    s = n - 1;
    ret = n;
    while(s != 0):
        ret = s * ret;
        s = s - 1;

    return ret;
