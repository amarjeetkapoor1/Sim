#include<iostream>
#include<fstream>
#include<cstring>
#include<cctype>
/*#include"job.h"*/

using namespace std;

struct joint{
	string name;
	string x;
	string y;
	string z;
};

class structure{

	//job job_d;
	string units;
	string widht;
	joint jo;
	string x;
	//joint_co joint;
	//mem_ind mI;
	//group gr;
	//matrial m;
	public:
		structure(fstream &file);
		void print();	

};


