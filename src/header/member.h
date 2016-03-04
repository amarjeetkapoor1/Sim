/*!
 *	\file structure.h  
 *
 *  \brief  It contain declarations for structure to be defined
 *
 *      
 *	Compiler g++
 *
 *  \author amarjeet singh kapoor
 *      
 */

#ifndef _MEMBER_H
#define _MEMBER_H

#include"header.h"
#include"joint.h"

class MemberLoad{
	public:
	string code,specCode;
	float spec;
	vector<int>f;
	
	MemberLoad();	
	void print();
};

class Member{
    public:
    vector<int> joint_id;
    int id;
    string material;
    string beta;
    MemberLoad *memberload;
	
	Member();
	void print();
};

class MemPro{
	public:
	vector<int> member_id;
	string type;
	string country;
	double YD;
	double ZD;
	double ZB;
	
	void print();
};

#endif
