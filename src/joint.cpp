/*!
 *	\file joint.cpp 
 *
 *	\brief  It contain definitions for member functions of class Joint 
 *  and JointLoad
 *      
 *  Compiler  g++
 *
 *  \author amarjeet singh kapoor
 *      
 */
#include "header/joint.h"

Joint::Joint(){

	support="FREE";

}


void Joint::print(){
	cout<<id<<","<<x<<",";
    cout<<y<<","<<z<<","<<support<<",";
    jointload.print();
}   


void JointLoad::print(){
	cout<<FX<<","<<FY<<","<<FZ<<","<<MX<<","<<MY<<","<<MZ;
}



JointLoad::JointLoad(){
	FX=0;
	FY=0;
	FZ=0;
	MX=0;
	MY=0;
	MZ=0;
}

string Joint::insert(int &r,sql::Connection &con){
	//create a database connection using the Driver 
	string message;
	stmt = con.createStatement();
	message="Job not Present";
	prep_stmt = con.prepareStatement("INSERT INTO Joint(job_id,idd,x,y,z,support) VALUES (?,?,?,?,?,?)");
	prep_stmt->setInt(1,r);
	message="duplicate entry of Joint id ="+id;
	prep_stmt->setInt(2,id);
	
	prep_stmt->setDouble(3,x);
	message="No value of x in Joint id ="+id;
	prep_stmt->setDouble(4,y);
	message="No value of y in Joint id ="+id;
	prep_stmt->setDouble(5,z);
	prep_stmt->setString(6,support);
	prep_stmt->execute();
	return message;
}
	
