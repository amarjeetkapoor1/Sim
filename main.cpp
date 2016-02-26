/*!
 * \file main.cpp 
 * \brief This file contain main program for 
 * extracting information from .std
 * file regarding full structure
 * 
 * \author
 * Amarjeet Singh Kapoor,
 * Govind Sharma
 */

#include<iostream>
#include<fstream>
#include"header/structure.h"

using namespace std;


int main(int argc ,char *argv[]){
	
	//opening file 
	fstream file;
	file.open(argv[1]);
	if(!file){
		cout<<"cannot open file";
		return 1;
	}
	// calling the structure 
	Structure s(file);
	
	// printing the structure information 
	file.close();
	s.print();
	s.insert();

	return 0;	
}
