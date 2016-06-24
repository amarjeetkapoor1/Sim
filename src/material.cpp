/*!
 *	\file material.cpp 
 *
 *	\brief  It contain definitions for member functions of class Material
 *
 *      
 *  Compiler  g++
 *
 *  \author amarjeet singh kapoor
 *      
 */
 
#include "header/material.h"

Material::Material(){
	E=0;poisson=0;alpha=0;density=0;damp=0;
	G=9.8;
}

void Material::print(){
	cout<<"material definition:\n";
	cout<<"name,"<<name<<endl;
	cout<<"E,"<<E<<endl;
	cout<<"poisson,"<<poisson<<endl;
	cout<<"density,"<<density<<endl;
	cout<<"alpha,"<<alpha<<endl;
	cout<<"damp,"<<damp<<endl;
	cout<<"type,"<<type<<endl;
	cout<<"strength,"<<strength<<endl;
	cout<<"G,"<<G<<endl;
}
