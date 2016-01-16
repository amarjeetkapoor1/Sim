/**
 *
 *       \file       structer.h
 *
 *       \brief      
 *
 *      
 *       Compiler    g++
 *
 *       \author     amarjeet singh kapoor
 *      
 */


#include"header.h"


struct joint{
    int id;
    double x, y, z;
};

struct member{
    vector<int> joint_id;
    int id;
};

struct material{
    string name, E, alpha, type, strength, G;
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

class job{
	string engineer, date,name,client,jobid,comment;
	string checker_name,engineer_name,approved_name,checker_date;
	string ref,part,rev,approved_date;
	public:
		string get(fstream &file);
		void print();
		void insert();

};
	
class structure{

	job job1;
	string width, unit, group;
    vector<joint> job_joints;
    vector<member> job_members;
    vector<material> job_material;
	string units;
	string widht;
	joint jo;
	string x;
	vector<int> beam;
	vector<int> column;
	vector<mem_pro> member_pr;
	concrete_design con_des;
	public:
		structure(fstream &file);
		void print();	
		void material3(string);
		void get_member_pro(string);
		void get_design(string);
		void get_joint(string str);
		
};




