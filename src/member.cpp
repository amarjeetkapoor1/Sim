/*!
 *	\file member.cpp 
 *
 *	\brief  It contain definitions for member functions of class Member, MemPro,
 *	MemberLoad
 *      
 *  Compiler  g++
 *
 *  \author amarjeet singh kapoor
 *      
 */

#include"header/member.h"

void MemPro::print(){
	cout<<country<<",";
	cout<<type<<","<<YD<<",";
	cout<<ZD;
	for(int j=0;j<member_id.size();j++)
		cout<<","<<member_id[j];
}

Member::Member(){
	beta="0";
	material="None";
	memberload=NULL;
}

void Member::print(){
	cout<<id<<","<<beta<<","<<material<<",";
	if(memberload!=NULL)
		memberload->print();
    for(int j=0;j<joint_id.size();j++)
    {
        cout<<joint_id[j]<<",";
    }
}

MemberLoad::MemberLoad(){
	specCode=" ";
	spec=0;
}


void MemberLoad::print(){
	cout<<code<<","<<spec<<","<<specCode<<",";
	for(int i=0;i<f.size();i++)
		cout<<f[i]<<",";
}
