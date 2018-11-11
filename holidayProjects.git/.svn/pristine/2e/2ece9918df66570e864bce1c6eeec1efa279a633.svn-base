#include "stdafx.h"
#include"List.h"
#include<iostream>

void llist::insertNode(int data)
{
	Node *temp = new Node();
	temp->data = data;
	temp->next = nullptr;
	if (head == nullptr)
		head = temp;
	else
	{
		Node *curr = head;
		while (curr->next!=nullptr)
			 curr = curr->next;
		curr->next = temp;
	}
}

void llist::deleteData(int data)
{
	if (head == nullptr)
		std::cout << "No data to delete" << std::endl;
	Node* curr = head;
	Node* prev = nullptr;
	while (curr->next !=nullptr)
	{
		if (curr->data == data)
		{
			if (prev == nullptr)
				head = curr->next;
			else
				prev->next = curr->next;

			delete curr;
			break;
		}
		else
		{
			prev = curr;
			curr = curr->next;
		}
	}

}

void llist::displayList()
{
	if (head == nullptr)
		std::cout << "List is empty" << std::endl;
	else
	{
		Node* curr = head;
		while (curr!= nullptr)
		{
			std::cout << curr->data << std::endl;
			curr = curr->next;
		}
	}
}

void llist::getData()
{
	if (head == nullptr)
		std::cout << "List is empty" << std::endl;
	else
	{
		Node* curr = head;
		std::vector<int> dataList;
		while (curr != nullptr)
		{
			dataList.push_back(curr->data);
			curr = curr->next;
		}
		for (int i= dataList.size()-1;i>=0;i--)
		{
			std::cout << dataList[i] << std::endl;
		}
	}
}