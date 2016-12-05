#include <iostream>

using namespace std;

class Converter
{
	unsigned int numb;
public: 
	Converter(int);
	void convert(int);
};

Converter::Converter(int a)
{
	numb = a;
}

void Converter::convert(int numer)
{
	const int size = 7;
	char roman_nums[size] = { 'I','V','X','L', 'C', 'D', 'M' };
	int arabic_vals[size] = { 1, 5, 10, 50, 100, 500, 1000 };

    int num = numer;
 
    char romnum[BUFSIZ];
    char *rnptr = romnum;

    for(int i = size - 1; i >= 0; --i)
    {
        while(num >= arabic_vals[i])
        {
            if((num >= arabic_vals[i] * 4) && (i != size))
            {
                num -= arabic_vals[i] * 4;
                *rnptr++ = roman_nums[i];
                *rnptr++ = roman_nums[i + 1];
            }
            else
            {
                num -= arabic_vals[i];
                *rnptr++ = roman_nums[i];
            }
        }
    }

	*rnptr = '\0';
 
    cout << "Result: " << romnum << endl;

}

void main()
{
	unsigned int number;
	cout << "Hello, this is ArabicToRoman converter!" << endl;

	do{
	cout << "Type number from 1 to 3999, please" << endl;
	cin >> number;
	}while((number < 1) || (number > 3999));

	Converter result = Converter(number);
	
	result.convert(number);

	cin.get();
	cin.get();
}