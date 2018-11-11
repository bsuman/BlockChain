#pragma once
#include<iostream>
#include<vector>
class StackDArray
{	
	int top = -1;
public: 
	int *dataArr;
	bool isEmpty()
	{
		if (top == -1)
			return true ;
		else return false;
	}

	void push(int data) {
		dataArr[++top] = data;
	}

	void pop()
	{
		if (isEmpty() == false)
		{
			std::cout << "The pop element is:"<< dataArr[top] << std::endl;
			top--;
		}
		else
			std::cout << "The stack is empty, nothing to pop" << std::endl;
	}

	void popAll()
	{
		if (isEmpty())
		{
			std::cout <<"The stack is empty, nothing to pop" << std::endl;
		}
		else
		{
			std::cout << "The stack elements are" << std::endl;
			while (!isEmpty())
			{
				std::cout << dataArr[top] <<std::endl;
				top--;
			}
		}
		
	}
};

class StackVec {

private:
	std::vector<int> data;
public:
	bool isEmpty()
	{
		if (data.size() <= 0)
			return true;
		else 
			return false;
	}

	void push(int dt) {
		data.push_back(dt);
	}

	void pop()
	{
		if (isEmpty())
			std::cout << "Stack is empty" << std::endl;
		else
		{
			std::cout << "Popped Element is " << data[data.size() - 1]<< std::endl;
			data.pop_back();
		}
			
	}

	void popAll()
	{
		if (isEmpty())
			std::cout << "Stack is empty" << std::endl;
		else
		{
			while (!isEmpty())
			{
				std::cout << "Popped Element is " << data[data.size() - 1] <<std::endl;
				data.pop_back();
			}
		}
	}

};



