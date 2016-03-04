/*!
 *	\file ConcertDesign.h  
 *
 *  \brief  It contain declarations for ConcertDesgin to be defined
 *
 *      
 *	Compiler g++
 *
 *  \author amarjeet singh kapoor
 *      
 */

#ifndef _CONCERTDESIGN_H
#define _CONCERTDESIGN_H

#include"header.h"

class CodeType{
	public:
	string code;
	string section;
	vector<int> member_id;
	
	void print();
	
};

class ConcreteDesign{
	public:
	string code;
	vector<CodeType> cty;
	
	void print();
};

#endif
