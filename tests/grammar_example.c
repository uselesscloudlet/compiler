int a = 1;
float b = 1.1;
char c = 'c';
string d = "str";
{
    {
        a &&a;
        b &&b;
    }
    {
        a == a;
        b != b;
        c > c;
        d < d;
        a >= a;
        b <= b;
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
        ~a;
        !a;
    }
    {
        ++a;
        --b;
    }
}