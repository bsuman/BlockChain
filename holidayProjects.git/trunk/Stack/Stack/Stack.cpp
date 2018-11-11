// Stack.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include"Stack_Interface.h"
#define MaxSize 100

void f1()
{
	StackDArray t;
	t.dataArr = new int[MaxSize];
	t.push(10);
	t.push(20);
	t.push(30);
	t.pop();
	t.popAll();
}
void f2()
{
	StackVec temp;
	temp.push(10);
	temp.push(20);
	temp.push(30);
	temp.push(40);
	temp.pop();
	temp.popAll();
}
int main()
{
	
	std::cout << "=================================================" << std::endl;
	std::cout << "************STACK IMPLEMENTATION*****************" << std::endl;
	std::cout << "=================================================" << std::endl;

	int ch = - 1;
	std::cout << "Choose between static (Maximum number of elements 100) or dynamic stack implemetation " << std::endl;
	std::cout << "Please enter 1 for static and 2 for dynamic" << std::endl;
	while (1)
	{
		std::cin >> ch;
		if (std::cin.fail())
		{
			std::cin.clear();
			std::cin.sync();
			std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
			std::cout << "Please enter 1 or 2 as input " << std::endl;
			continue;
		}
		if (ch < 0 || ch >3)
		{
			std::cout << "Please enter 1 or 2 as input " << std::endl;
			continue;
		}
		else
			break;
	}
	switch (ch){
	case 1: f1();
			break;
	case 2: f2();
		break;
	}
    return 0;
}

