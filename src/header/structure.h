/*!
 *	\file structure.h  
 *
 *  \brief  It contain declarations for Structure to be defined
 *
 *      
 *	Compiler g++
 *
 *  \author amarjeet singh kapoor
 *      
 */

#ifndef _STRUCTURE_H
#define _STRUCTURE_H

#include"header.h"
#include"job.h"
#include"joint.h"
#include"member.h"
#include"material.h"
#include"ConcreteDesign.h"


class Load{
	public:
	int id;
	string type,title;
	bool reduce;
	
	void print();
		
};	
    

class Structure: public base{

	
    vector<Material> job_material;
	string units;
	string widht;
	string x;
	vector<int> beam;
	vector<int> column;
	vector<MemPro> member_pr;
	ConcreteDesign con_des;
	string message;
	vector <Load> load;
	vector<MemberLoad> memberload;
	void getSupportsTypes(string temp1,string type);
	public:	
		string width, unit, group;
		vectJoint job_joints;
		Memberlist job_members;
			Job job;
		
		/*!
			\brief This is constructor that is used initialize all member
			variables.
    	*/
    	
    	
		Structure(fstream &);
		Structure();
		/*!
			\brief This member function is used to get units nad input widht
			 and is called in structure()
			\param temp string to be parsed
    	*/
		void getUnits(string);
		/*!
			\brief This member function is used to print all properties 
			of job and calls job::print() 
    	*/
		void print();	
		
		/*!
			\brief This member function is used to initialize material 
			property and is called in structure()
			\param temp string to be parsed
    	*/
		void getMaterial(string);
		
		/*!
			\brief This member function is used to initialize member property 
			and is called in structure() 
			\param temp string to be parsed
    	*/
		void getMemberPro(string);
		
		/*!
			\brief This member function is used to initialize design property 
			and is called in structure() 
			\param temp string to be parsed
    	*/
		void getDesign(string);
		
		/*!
			\brief This member function is used to initialize design column 
			and is called in structure() 
			\param temp string to be parsed
    	*/
		void getDesignColumn(string);
		
		/*!
			\brief This member function is used to initialize design beam 
			and is called in structure() 
			\param temp string to be parsed
    	*/
		void getDesignBeam(string);

		/*!
			\brief This member function is used to initialize joints 
			and is called in structure()
			\param temp string to be parsed
    	*/
		void getJoint(string str);
		
		/*!
			\brief This member function is used to initialize members 
			and is called in structure()
			
			JOINT  COORDINATES  (CYLINDRICAL  (REVERSE))
			(NOCHECK)band-spec
			i 1 , x 1 , y 1 , z 1 , ( i 2 , x 2 , y 2 , z 2 , i 3 )

			REPEAT   n, xi 1 , yi 1 , zi 1 , (xi 2 , yi 2 , zi 2 ,..., xi n , yi n , zi n )
			REPEAT  ALL   n, xi 1 , yi 1 , zi 1 , (xi 2 , yi 2 , zi 2 ,..., xi n , yi n ,
			zi n )
			\param temp string to be parsed
    	*/
		void getMember(string);
		/*!
			\brief This member function is to add BETA to joint
			
		SUPPORTS
		{ joint-list | ni TO nj GENERATE } { PINNED | FIXED ( BUT
		release-spec (spring-spec) ) | ENFORCED ( BUT release-spec)
		}
		release-sepc = { FX | FY | FZ | MX | MY | MZ }
		spring-spec = *{KFX f1 | KFY f2 | KFZ f3 | KMX f4 | KMY f5
		| KMZ f6 }


		Where:
		ni, nj = Start and end node numbers, respectively, for generating
		supports along a SURFACE element edge.
		f ... f = Spring constants corresponding to support spring directions
		1
		6
		X, Y, and Z and rotations about X, Y, and Z, repsectively.
		\param temp string to be parsed
		*/
		void getSupports(string);
		
		
		/*!
			\brief This member function is to add BETA to joint
			
		CONSTANTS
		MATERIAL name { MEMBER member/element-list | (ALL) }
		\n
		Where:
		name = material name as specified in the DEFINE MATERIAL
		command (See "Define Material" on page 386 ).
		or
		\n
		{ E f 1 | G f 2 | POISSON f 3 | DENSITY f 4 | BETA { f 5  | ANGLE
		| RANGLE } | ALPHA f 6 | CDAMP f 7 } { MEMBER memb/elem-list |
		BEAM | PLATE | SOLID | (ALL) }
		{ REF f8 , f9 , f10 | REFJT f 11 | REFVECTOR f 12 f 13 f 14 } MEMBER
		memb/elem-list
			and is called in structure()
			\param temp string to be parsed
    	*/
		void getBeta(string);
		
		
		/*!
			\brief This member function is to add load
			
			LOADING i 1 ( LOADTYPE a 1 ) ( REDUCIBLE ) ( TITLE any_load_
			title ) \n
			and is called in structure()
			\param temp string to be parsed
    	*/
		void getLoad(string);
		
		
		/*!
			\brief This member function is to add load to
			joint
			
			JOINT LOAD
			joint-list *{ FX f7 | FY f8 | FZ f9 | MX f10 | MY f11 | MZ f12

			and is called in structure()
			\param temp string to be parsed
    	*/	
		void getJointLoad(string temp);
		
		/*!
			\brief This member function is to add load to
			member
			MEMBER LOAD
			member-list { { UNI | UMOM } dir-spec f 1 f 2 f 3 f 4 | { CON |
			CMOM } dir-spec f 5 f 6 f 4 | LIN dir-spec f 7 f 8 f 9 | TRAP dir-
			spec f 10 f 11 f 12 f 13 }
			Where:
			dir-spec = { X | Y | Z | GX | GY | GZ | PX | PY | PZ }
			and is called in structure()
			\param temp string to be parsed
    	*/
		
		void getMemberLoad(string temp);
		
		/*!
			\brief This member function is used to insert data into DB.
    	*/
		void insert();
		
		/*!
			\brief This member function is used to insert members 
			\param z unique id of job generated by job::insert() 
			
    	*/
		void insertMember(int );
		
		/*!
			\brief This member function is used to insert material 
			property into Database.
      		\param z unique id of job generated by job::insert()
      		
    	*/
		void insertMaterial(int);
		
		/*!
			\brief This function is used to insert member property
				into Database.
      \param z unique id of job generated by job::insert()
      
     
    	*/
		void insertMemberPro(int);
		
		/*!
			\brief This destructure for structure that frees pointers.
    */
		~Structure();
		
};

#endif


