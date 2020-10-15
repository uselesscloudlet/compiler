int main()
{
    printf("Some Example");
    int a = 35482;
    float b = .9393;
    float c = 39.999;
    float d = 0.423E10;
    float e = 0.429E+10;
    float f = 0.289E-12;

    if (a > 50)
    {
        printf("True");
    }
    else
    {
        printf("Just False");
    }
    for (int i = 0; i < 10; ++i)
    {
        printf("just example\n");
    }
    int i = 0;
    while (1)
    {
        printf("%u", i);
        if (i == 10)
        {
            break;
        }
        i++;
    }
    a >= c;
    b <= c;
    b == b;
    a > c;
    b < c;
<<<<<<< HEAD
    int g = a + b;
    g++;
    g += b;
    g--;
    g -= a;
    // that is comment and we doing nothing
=======
    b++;
    c--;
    b += c;
>>>>>>> 4e966c7375897b22f6ad2fa278b9f6fef2062616
}