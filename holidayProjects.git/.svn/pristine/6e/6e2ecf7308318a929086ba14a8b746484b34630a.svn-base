// Swapping.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<string>
template <typename T>
void swapfunc(T &a, T &b)
{
	std::cout << "Value of first input" << a << std::endl;
	std::cout << "Value of second input" << b << std::endl;
	a = a + b;
	std::cout << "Value of addition of inputs" << a << std::endl;
	b = a - b;
	std::cout << "Value of difference of input" << b << std::endl;
	a = a - b;
	std::cout << "Value of second difference of input" << a << std::endl;
}

int main()
{
	int a=10, b=20;
	std::cout << "The values of a and b before swapping are: a =" <<a <<" and b=" << b<< std::endl;
	swapfunc(a, b);
	std::cout << "The values of a and b after swapping are: a =" << a << " and b=" << b << std::endl;

	double a1 = 11.12, b2 = 23.45;

	std::cout << "The values of a and b before swapping are: a =" << a1 << " and b=" << b2 << std::endl;
	swapfunc(a1, b2);
	std::cout << "The values of a and b after swapping are: a =" << a1 << " and b=" << b2 << std::endl;

	char x = 'a', y = 'd';
	std::cout << "The values of x and y before swapping are: x =" << x << " and y=" << y << std::endl;
	swapfunc(x, y);
	std::cout << "The values of x and y after swapping are: x =" << x << " and y=" << y << std::endl;

	//std::string t1 = "abc", t2 = "xyz";
	//std::cout << "The values of t1 and t2 before swapping are: t1 =" << t1 << " and t2=" << t2 << std::endl;
	//swapfunc(t1, t2);
	//std::cout << "The values of t1 and t2 after swapping are: t1 =" << t1 << " and t2=" << t2 << std::endl;

    return 0;
}

