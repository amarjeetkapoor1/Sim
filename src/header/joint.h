/*!
 *	\file joint.h  
 *
 *  \brief  It contain declarations for Joint and JointLoad to be defined
 *
 *      
 *	Compiler g++
 *
 *  \author amarjeet singh kapoor
 *      
 */

#ifndef _JOINT_H
#define _JOINT_H

#include"header.h"


class JointLoad{
    public:
    int FX,FY,FZ, MX, MY, MZ;
   
    JointLoad();
    void print();
    string insert(int &r,sql::Connection &con);
};
  

class Joint: public base{

	public:
    int id;
    double x, y, z;
    //default value is free, and those 
    //who are fixed will be modified in the function.
    string support;
    JointLoad jointload;
    
    Joint();
    void print();
    string insert(int &r,sql::Connection &con);
    
    	
};


class vectJoint{
	public:
	vector<Joint> list;
};

#endif
