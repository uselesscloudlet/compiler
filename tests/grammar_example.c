a = 1;
b = 1.1;
c = 'c';
d = "str";
{
    {
        e = a && a;
        e = b && b;
    }
    {
        e = a == a;
        e = b != b;
        e = c > c;
        e = d < d;
        e = a >= a;
        e = b <= b;
    }
    {
        a = a + b;
        b = a - b;
    }
    {
        a = a * b;
        b = a / b;
        a = a % a / 2;
    }
    {
        a = (int)b;
    }
    {
        e = ~a;
        e = !a;
    }
    {
        e = ++a;
        e = --b;
    }
}
a