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
