/*!
 *	\file structure.cpp 
 *
 *	\brief  It contain definitions for member functions of class structure
 *
 *      
 *  Compiler  g++
 *
 *  \author amarjeet singh kapoor
 *      
 */

#include "header/structure.h"

using namespace std;
using namespace sql;

void structure::insert(){
	int z;
	job1.insert(z);	
	for(int i=0;i<job_joints.size();i++){
		prep_stmt = con->prepareStatement("INSERT INTO Joint(job_id,id,x,y,z) VALUES (?,?,?,?,?)");
		prep_stmt->setInt(1,z);
		prep_stmt->setInt(2,job_joints[i].id);
		prep_stmt->setDouble(3,job_joints[i].x);
		prep_stmt->setDouble(4,job_joints[i].y);
		prep_stmt->setDouble(5,job_joints[i].z);
		prep_stmt->execute();
	}
	insert_member(z);
	insert_material(z);
	insert_member_pro(z);
	
}


void structure::insert_material(int z){
	for(int i=0;i<job_material.size();i++){
		prep_stmt = con->prepareStatement("INSERT INTO Job_material(job_id,name,E,poisson,density,damp,alpha,G,strength,type) VALUES (?,?,?,?,?,?,?,?,?,?)");
		prep_stmt->setInt(1,z);
		prep_stmt->setString(2,job_material[i].name);
		prep_stmt->setDouble(3,job_material[i].E);
		prep_stmt->setDouble(4,job_material[i].poisson);
		prep_stmt->setDouble(5,job_material[i].alpha);
		prep_stmt->setDouble(6,job_material[i].density);
		prep_stmt->setDouble(7,job_material[i].damp);
		prep_stmt->setDouble(8,job_material[i].G);
		prep_stmt->setString(9,job_material[i].strength);
		prep_stmt->setString(10,job_material[i].type);
		prep_stmt->execute();
	}
	
	
}

void structure::insert_member(int z){
	 
	for(int i=0;i<job_members.size();i++){
		prep_stmt = con->prepareStatement("INSERT INTO Member(job_id,member_id) VALUES (?,?)");
		prep_stmt->setInt(1,z);
		prep_stmt->setInt(2,job_members[i].id);
		prep_stmt->execute();
		for(int k=0;k<job_members[i].joint_id.size();k++){
      prep_stmt = con->prepareStatement("INSERT INTO Member_incidence(job_id,member_id,joint_id) VALUES (?,?,?)");
			prep_stmt->setInt(1,z);
			prep_stmt->setInt(2,job_members[i].id);
			prep_stmt->setInt(3,job_members[i].joint_id[k]);
			prep_stmt->execute();
    }
  }

}

void structure::insert_member_pro(int z){
	
	for(int i=0;i<member_pr.size();i++){
		prep_stmt = con->prepareStatement("INSERT INTO Member_property(job_id,id,type,YD,ZD) VALUES (?,?,?,?,?)");
		prep_stmt->setInt(1,z);
		prep_stmt->setInt(2,i);
		prep_stmt->setString(3,member_pr[i].type);
		prep_stmt->setDouble(4,member_pr[i].YD);
		prep_stmt->setDouble(5,member_pr[i].ZD);
		prep_stmt->execute();
		for(int j=0; j<member_pr[i].member_id.size();j++){
			prep_stmt = con->prepareStatement("UPDATE Member SET member_property = ? where job_id = ? and member_id= ?");
			prep_stmt->setDouble(1,i);
			prep_stmt->setDouble(2,z);
			prep_stmt->setInt(3,member_pr[i].member_id[j]);
			prep_stmt->execute();
		}
	}
	
}

structure::~structure(){
	delete stmt;
	delete con;
}
	
void structure::print(){
	
	//printing job info
	job1.print();
    cout<<"width,"<<width<<endl;
    cout<<"unit,"<<unit<<endl;
    //cout<<"group:\t"<<group<<endl;
    
    //printing joint coordinates
    cout<<"JOINT COORDINATES:\n";
    cout<<"joint id , x cooordinates, y coordinates, z coordinates \n";
    for(int i=0;i<job_joints.size();i++)
    {
        cout<<job_joints[i].id<<","<<job_joints[i].x<<",";
        cout<<job_joints[i].y<<","<<job_joints[i].z<<endl;
    }
    
    //printing member incidences
    cout<<"MEMBER INCIDENCES:\n";
    cout<<"member id , joint id ,joint id , .... \n";
    for(int i=0;i<job_members.size();i++)
    {
        cout<<job_members[i].id<<",";
        for(int j=0;j<job_members[i].joint_id.size();j++)
        {
            cout<<job_members[i].joint_id[j]<<",";
        }
        cout<<endl;
    }
    
    //printing material defination
     for(int i=0;i<job_material.size();i++){
    cout<<"material definition:\n";
    cout<<"name,"<<job_material[i].name<<endl;
    cout<<"E,"<<job_material[i].E<<endl;
    cout<<"poisson,"<<job_material[i].poisson<<endl;
    cout<<"density,"<<job_material[i].density<<endl;
    cout<<"alpha,"<<job_material[i].alpha<<endl;
    cout<<"damp,"<<job_material[i].damp<<endl;
    cout<<"type,"<<job_material[i].type<<endl;
    cout<<"strength,"<<job_material[i].strength<<endl;
    cout<<"G,"<<job_material[i].G<<endl;
    }
    //printing member property
    cout<<"MEMBER PROPERTY \n";
    cout<<"TYPE, YD, ZD, Member,  Member, Member, ...... \n";
    for(int i=0;i<member_pr.size();i++){
    	cout<<member_pr[i].type<<","<<member_pr[i].YD<<",";
    	cout<<member_pr[i].ZD;
    	for(int j=0;j<member_pr[i].member_id.size();j++)
    		cout<<","<<member_pr[i].member_id[j];
    	cout<<endl;
    }
    
    //printing concrete design info
    cout<<"CONCRETE DESIGN INFORMATION"<<endl;
    cout<<"CODE ,"<<con_des.code<<endl;
    for(int i=0;i<con_des.cty.size();i++){
    	cout<<con_des.cty[i].code<<","<<con_des.cty[i].section<<",";
    	cout<<endl;
    	for(int j=0;j<con_des.cty[i].member_id.size();j++)
    		cout<<con_des.cty[i].member_id[j]<<",";
    	cout<<endl;
    }
    
    //printing Design Beam
    cout<<"Design Beam"<<endl;
    for(int i=0;i<beam.size();i++){
    	cout<<beam[i]<<",";
    }
    
    //printing design column
    cout<<endl<<"DESIGN COLUMN"<<endl;
    for(int i=0;i<column.size();i++){
    	cout<<column[i]<<",";
    }
}

    
structure::structure(fstream &file)   
{
    string str="", temp;
    
    driver =get_driver_instance();
	con = driver->connect("localhost",USER,PASSWORD);
	stmt = con->createStatement();
	stmt->execute("USE Sim");
    
    str=job1.get(file);
	temp=str;
    for(int i=0 ; i<temp.length();i++)
    {
        if(temp[i]=='\n' || temp[i]=='\r'){
        	temp[i]=' ';
        
        }
    }
   
    temp=split(temp, "END JOB INFORMATION")[1];
	width=split(split(temp, "UNIT")[0], "INPUT WIDTH")[1];
   
    //get units
    temp=split(temp, "UNIT")[1];
    unit=split(temp, "JOINT COORDINATES")[0];
    
    //get joint coordinates
    get_joint(temp);
    
    //getting group information 
    temp=split(temp, "START GROUP DEFINITION")[1];
    group=split(temp, "END GROUP DEFINITION")[0];
    
    //getting material info
    temp=split(temp, "END GROUP DEFINITION")[1];
   	get_material(str);
    
    //gettin member properties
    get_member_pro(temp);
    
    return;
    //getting concerete design
    get_design(temp);
    

}


	
void structure::get_material(string temp){
    vector<string> vect_temp2;
    vector<string> vect_temp3;
    temp=split(temp, "DEFINE MATERIAL START")[1];
    temp=split(temp, "END DEFINE MATERIAL")[0];
	vect_temp2=split(temp, "\n");
	for(int j=0;j<vect_temp2.size();){
		material mater ;
		int z=j;
		for(int i=z;i<9+z && j<vect_temp2.size();i++)
		{	
			vect_temp3=split(vect_temp2[i], " ", 1);
   			string h=vect_temp3[0];
			if(i==z){
				mater.name=vect_temp3[0]+" "+vect_temp3[1];
				j++;   
 				continue;
			}
			if(h=="E")
			{
				istringstream(vect_temp3[1])>>mater.E;
				j++;   
 				continue;
			}
			if(h=="POISSON")
			{
				istringstream(vect_temp3[1])>>mater.poisson;
				j++;   
 				continue;
			}
			if(h=="DENSITY")
			{
				istringstream(vect_temp3[1])>>mater.density;
				j++;   
 				continue;
			}
			if(h=="ALPHA")
			{
				istringstream(vect_temp3[1])>>mater.alpha;
				j++;   
 				continue;
			}
			if(h=="DAMP")
			{
				istringstream(vect_temp3[1])>>mater.damp;
				j++;   
				 continue;
			}
			if(h=="TYPE")
			{	
				mater.type=vect_temp3[1];
				j++;   
 				continue;
			}
			if(h=="STRENGTH")
			{
				mater.strength=vect_temp3[1];
				j++;   
 				continue;
			}
			if(h=="G")
			{
				istringstream(vect_temp3[1])>>mater.G;
				j++;   
 				continue;
			}
			
			break;
			
		}
		job_material.push_back(mater);
   }
}
	
void structure::get_joint(string temp){
	string temp1;
    vector<string> vect_temp2;
    vector<string> vect_temp3;
	temp=split(temp, "JOINT COORDINATES")[1];
    temp1=split(temp, "MEMBER INCIDENCES")[0];
    vect_temp2=split(temp1, "; ");
    for(int i=0;i<vect_temp2.size();i++)
    {
        vect_temp3=split(vect_temp2[i], " ");
        joint j;
        istringstream(vect_temp3[0])>>j.id;
        istringstream(vect_temp3[1])>>j.x;
        istringstream(vect_temp3[2])>>j.y;
        istringstream(vect_temp3[3])>>j.z;
        job_joints.push_back(j);
        vect_temp3.clear();
    }
    
    
    
    vect_temp2.clear();
    
    //get MEMBER INCIDENCES
    temp=split(temp, "MEMBER INCIDENCES")[1];
    temp1=split(temp, "START GROUP DEFINITION")[0];
    vect_temp2=split(temp1, ";");
    for(int i=0;i<vect_temp2.size()-1;i++)
    {	
        vect_temp3=split(vect_temp2[i], " ");
        member m;
        istringstream(vect_temp3[0])>>m.id;
        for(int j=1;j<vect_temp3.size();j++)
        {
            int l;
            istringstream(vect_temp3[j])>>l;
            m.joint_id.push_back(l);
        }
        job_members.push_back(m);
        vect_temp3.clear();
        
    }
    vect_temp2.clear();
}
	
void structure::get_member_pro(string temp){

    vector<string> vect_temp2;

	temp=split(temp, "END DEFINE MATERIAL")[1];
    temp=split(temp, "MEMBER PROPERTY INDIAN")[1];
    temp=split(temp, "CONSTANTS")[0];
    vect_temp2=split(temp," ");
    mem_pro *me;
    me=new mem_pro;
    for(int i=0; i<vect_temp2.size();i++){
    	
    	float l=0,l1=0;
    	if(isdigit(vect_temp2[i][0])){
    		istringstream(vect_temp2[i])>>l;
    		(*me).member_id.push_back(l);
    		continue;
    	}
    		if(vect_temp2[i]=="TO"){
    			istringstream(vect_temp2[i-1])>>l;
    			istringstream(vect_temp2[i+1])>>l1;
    			for( int j=l+1;j<l1;j++){
    				
    				(*me).member_id.push_back(j);
    			}
    		}
    		if(vect_temp2[i]=="PRIS"){
    			istringstream(vect_temp2[i+2])>>l;
    			istringstream(vect_temp2[i+4])>>l1;
    			(*me).type=vect_temp2[i];
    			(*me).YD=l;
    			(*me).ZD=l1;
    			member_pr.push_back(*me);
    			delete me;
    			mem_pro *me;
    			me=new mem_pro;
    			i=i+4;
    			
    		}
    	
    }
    vect_temp2.clear();

}


void structure::get_design(string temp){
	string temp1;
    vector<string> vect_temp2;
    vector<string> vect_temp3;
	
	//getting concrete info 
    temp1=split(temp,"START CONCRETE DESIGN")[1];
    temp1=split(temp1,"DESIGN BEAM")[0];
    
    vect_temp2=split(temp1," ");
    
    con_des.code=vect_temp2[1];
    code_type *cd;
    cd=new code_type;
	for(int i=2; i<vect_temp2.size();i++){
		float l=0,l1=0;
		if(isdigit(vect_temp2[i][0])){
			istringstream(vect_temp2[i])>>l;
			cd->member_id.push_back(l);
			continue;
		}
		if(vect_temp2[i]=="TO"){
			istringstream(vect_temp2[i-1])>>l;
			istringstream(vect_temp2[i+1])>>l1;
			for( int j=l+1;j<l1;j++){
					cd->member_id.push_back(j);
				}
		}
		else{
			if(isalpha(vect_temp2[i][0])){
				if(i>5){
				  	con_des.cty.push_back(*cd);
				  	
				}
				delete cd;
				code_type *cd;
				cd=new code_type;
				cd->code=vect_temp2[i];
				cd->section=vect_temp2[i+1];
				i=i+2;
			}
		}
	}
   con_des.cty.push_back(*cd);
   
   
    vect_temp2.clear();
	  
   	//getting design beam 
	temp1=split(temp,"DESIGN BEAM")[1];
	temp1=split(temp1,"DESIGN COLUMN")[0];
    vect_temp2=split(temp1," ");
     for(int i=0; i<vect_temp2.size();i++){
    	float l=0,l1=0;
    	if(isdigit(vect_temp2[i][0])){
    		istringstream(vect_temp2[i])>>l;
    		beam.push_back(l);
    		continue;
    	}
    	if(vect_temp2[i]=="TO"){
    		istringstream(vect_temp2[i-1])>>l;
    		istringstream(vect_temp2[i+1])>>l1;
    		for( int j=l+1;j<l1;j++){
    				beam.push_back(j);
    			}
    		}
    	
    }
    
     vect_temp2.clear();
	
	//getting design column
    temp1=split(temp,"DESIGN COLUMN")[1];
    vect_temp2=split(temp1," ");
    for(int i=0; i<vect_temp2.size();i++){
		float l=0,l1=0;
		if(isdigit(vect_temp2[i][0])){
			istringstream(vect_temp2[i])>>l;
			column.push_back(l);
			continue;
		}
		if(vect_temp2[i]=="TO"){
			istringstream(vect_temp2[i-1])>>l;
			istringstream(vect_temp2[i+1])>>l1;
			for( int j=l+1;j<l1;j++){
				column.push_back(j);
			}
		}
	}
}
