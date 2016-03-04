/*!
 *	\file ConcreteDesign.cpp 
 *
 *	\brief  It contain definitions for member functions of class ConcreteDesign and CodeType
 *
 *      
 *  Compiler  g++
 *
 *  \author amarjeet singh kapoor
 *      
 */

#include "header/ConcreteDesign.h"

void CodeType::print(){
	cout<<code<<","<<section<<",";
	cout<<endl;
	for(int j=0;j<member_id.size();j++)
		cout<<member_id[j]<<",";
}

void ConcreteDesign::print(){
	cout<<"CONCRETE DESIGN INFORMATION"<<endl;
	cout<<"CODE ,"<<code<<endl;
	for(int i=0;i<cty.size();i++){
		cty[i].print();
		cout<<endl;
	}
}

