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

#ifndef _STRUCTURE_H
#define _STRUCTURE_H

#include"header.h"
#include"job.h"



struct joint{
    int id;
    double x, y, z;
};

struct member{
    vector<int> joint_id;
    int id;
};

struct material{
    string name, type, strength;
    double E,poisson, alpha, density, damp , G=NULL;
};

struct mem_pro{
	vector<int> member_id;
	string type;
	double YD;
	double ZD;
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

	job job1;
	sql::Driver *driver;
	sql::Statement *stmt;
	sql::Connection *con;
	sql::PreparedStatement  *prep_stmt;
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
		void get_material(string);
		void get_member_pro(string);
		void get_design(string);
		void get_joint(string str);
		void insert();
		void insert_member(int );
		void insert_material(int);
		void insert_member_pro(int);
		~structure();
		
};

#endif


