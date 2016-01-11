#include<iostream>
#include<fstream>
#include<cstring>
#include <vector>
#include <sstream>
#include<cctype>
#include<stdlib.h>
/*#include"job.h"*/

using namespace std;

struct joint{
    int id;
    double x, y, z;
};

struct member{
    vector<int> joint_id;
    int id;
};

struct material{
    string name, E, alfa, type, strength, G;
    double poison, density, damp;
};

struct mem_pro{
	vector<int> joint_id;
	string type;
	float YD;
	float ZD;
};

struct code_type{
	string code;
	string section;
	vector<int> member_id;
};

struct concrete_design{
	string code;
	vector<code_type> cty;
};


class structure{

	//job job_d;
	string engineer, date, width, unit, group;
    vector<joint> job_joints;
    vector<member> job_members;
    material job_material;
	string units;
	string widht;
	joint jo;
	string x;
	vector<int> beam;
	vector<int> column;
	vector<mem_pro> member_pr;
	concrete_design con_des;
	//group gr;
	//matrial m;
	public:
		structure(fstream &file);
		void print();	

};

vector<string> split(string str, string del);
