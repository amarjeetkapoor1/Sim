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

void Structure::insert(){
	try{
		string message;
		stmt->execute("start transaction");
		int z;
		job.insert(z);	
		for(int i=0;i<job_joints.size();i++){
			message="Job not Present";
			prep_stmt = con->prepareStatement("INSERT INTO Joint(job_id,id,x,y,z,support) VALUES (?,?,?,?,?,?)");
			prep_stmt->setInt(1,z);
			message="duplicate entry of Joint id ="+job_joints[i].id;
			prep_stmt->setInt(2,job_joints[i].id);
			
			prep_stmt->setDouble(3,job_joints[i].x);
			message="No value of x in Joint id ="+job_joints[i].id;
			prep_stmt->setDouble(4,job_joints[i].y);
			message="No value of y in Joint id ="+job_joints[i].id;
			prep_stmt->setDouble(5,job_joints[i].z);
			prep_stmt->setString(6,job_joints[i].support);
			prep_stmt->execute();
		}
		insertMember(z);
		insertMaterial(z);
		insertMemberPro(z);
		
		message="ok";
		stmt->execute("commit");
	}
	catch (sql::SQLException &e) {
		stmt->execute("Rollback");
		cerr<<message;
		cerr<<" \n so transaction terminated \n";
	}
}


void Structure::insertMaterial(int z){
	for(int i=0;i<job_material.size();i++){
		prep_stmt = con->prepareStatement("INSERT INTO Job_material(job_id,name,E,poisson,density,damp,alpha,G,strength,type) VALUES (?,?,?,?,?,?,?,?,?,?)");
		prep_stmt->setInt(1,z);
		message="No name of material";
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

void Structure::insertMember(int z){
		for(int i=0;i<job_members.size();i++){
			prep_stmt = con->prepareStatement("INSERT INTO Member(job_id,member_id) VALUES (?,?)");
			prep_stmt->setInt(1,z);
			stringstream sstm;
			sstm<<"Duplicate Member id = "<<job_members[i].id;
			message = sstm.str();
			prep_stmt->setInt(2,job_members[i].id);
			prep_stmt->execute();
			for(int k=0;k<job_members[i].joint_id.size();k++){
		  prep_stmt = con->prepareStatement("INSERT INTO Member_incidence(job_id,member_id,joint_id) VALUES (?,?,?)");
				prep_stmt->setInt(1,z);
				prep_stmt->setInt(2,job_members[i].id);
				stringstream sstm1;
				sstm1<<" wrong JOINT id "<<job_members[i].joint_id[k]<<" in member ="<<job_members[i].id;
				message = sstm1.str();
				prep_stmt->setInt(3,job_members[i].joint_id[k]);
				prep_stmt->execute();
		}
	  }
}

void Structure::insertMemberPro(int z){

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

Structure::~Structure(){
	delete stmt;
	delete con;
}
	
void Structure::print(){
	
	//printing job info
	job.print();
    cout<<"width,"<<width<<endl;
    cout<<"unit,"<<unit<<endl;
    //cout<<"group:\t"<<group<<endl;
    
    //printing joint coordinates
    cout<<"JOINT COORDINATES:\n";
    cout<<"joint id , x cooordinates, y coordinates, z coordinates  support\n";
    for(int i=0;i<job_joints.size();i++)
    {
        cout<<job_joints[i].id<<","<<job_joints[i].x<<",";
        cout<<job_joints[i].y<<","<<job_joints[i].z<<","<<job_joints[i].support<< endl;
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
    cout<<"country,TYPE, YD, ZD, Member,  Member, Member, ...... \n";
    for(int i=0;i<member_pr.size();i++){
    cout<<member_pr[i].country<<",";
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

    
Structure::Structure(fstream &file)   
{
    string str="", temp;
    
    driver =get_driver_instance();
	con = driver->connect("localhost",USER,PASSWORD);
	stmt = con->createStatement();
	stmt->execute("USE Sim");
    
    str=job.get(file);
    
    
	temp=str;
	
	for(int i=0 ; i<temp.length();i++)
    {
    	if(temp[i]=='*'){
    		while(temp[i]!='\n')
    			i++;
    	}
        if(temp[i]=='\n' || temp[i]=='\r'){
        	temp[i]=' ';
        
        }
    }
   
   
    getUnits(str);
    
  
    //get joint coordinates
    getJoint(temp);
    
    
    getMember(temp);
    
    
    //getting group information 
    //temp=split(temp, "START GROUP DEFINITION")[1];
    //group=split(temp, "END GROUP DEFINITION")[0];
    
    //getting material info
    
   	getMaterial(str);
    

    //gettin member properties
    getMemberPro(temp);
    
        
    
    //getting concerete design
    getDesign(temp);
    getDesignBeam(temp);
    getSupports(temp);
    

}

void Structure::getUnits(string temp){
	
	vector <string> w;
	w=split(split(temp, "UNIT")[0], "INPUT WIDTH");
   	
   	if(w.size()==1){
    	cerr<<"NO Input width \n";
    	return ;
	}
	width=w[1];
    //get units
    w=split(temp, "UNIT");
    if(w.size()==1){
    	cerr<<"NO Units \n";
    	return ;
	}
    unit=split(w[1], "\n")[0];
}


	
void Structure::getMaterial(string temp){
    vector<string> vect_temp;
    vector<string> vect_temp1;
    vect_temp=split(temp, "DEFINE MATERIAL START");
    if(vect_temp.size()==1){
    	cerr<<"NO Material \n";
    	return ;
	}
	
	
    temp=split(vect_temp[1], "END DEFINE MATERIAL")[0];
	vect_temp=split(temp, "\n");
	
	
	for(int j=0;j<vect_temp.size();){
		Material mater ;
		int z=j;
		for(int i=z;i<9+z && j<vect_temp.size();i++)
		{	
			vect_temp1=split(vect_temp[i], " ", 1);
   			string h=vect_temp1[0];
			if(i==z){
				mater.name=vect_temp1[0]+" "+vect_temp1[1];
				j++;   
 				continue;
			}
			if(h=="E")
			{
				istringstream(vect_temp1[1])>>mater.E;
				j++;   
 				continue;
			}
			if(h=="POISSON")
			{
				istringstream(vect_temp1[1])>>mater.poisson;
				j++;   
 				continue;
			}
			if(h=="DENSITY")
			{
				istringstream(vect_temp1[1])>>mater.density;
				j++;   
 				continue;
			}
			if(h=="ALPHA")
			{
				istringstream(vect_temp1[1])>>mater.alpha;
				j++;   
 				continue;
			}
			if(h=="DAMP")
			{
				istringstream(vect_temp1[1])>>mater.damp;
				j++;   
				 continue;
			}
			if(h=="TYPE")
			{	
				mater.type=vect_temp1[1];
				j++;   
 				continue;
			}
			if(h=="STRENGTH")
			{
				mater.strength=vect_temp1[1];
				j++;   
 				continue;
			}
			if(h=="G")
			{
				istringstream(vect_temp1[1])>>mater.G;
				j++;   
 				continue;
			}
			
			break;
			
		}
		job_material.push_back(mater);
   }
}
	
void Structure::getJoint(string temp){

    vector<string> vect_temp;
    vector<string> vect_temp1;
	vect_temp=split(temp, "JOINT COORDINATES");
	if(vect_temp.size()==1){
    	cerr<<"NO Joint Coordinates \n";
    	return ;
	}
	
    temp=split(vect_temp[1], "MEMBER INCIDENCES")[0];
    vect_temp=split(temp, "; ");
    
    
    for(int i=0;i<vect_temp.size();i++)
    {
        vect_temp1=split(vect_temp[i], " ");
        Joint j;
        istringstream(vect_temp1[0])>>j.id;
        istringstream(vect_temp1[1])>>j.x;
        istringstream(vect_temp1[2])>>j.y;
        istringstream(vect_temp1[3])>>j.z;
        job_joints.push_back(j);
        vect_temp1.clear();
    }
    
}

void Structure::getMember(string temp){
    
    vector<string> vect_temp;
    vector<string> vect_temp1;
    //get MEMBER INCIDENCES
    vect_temp=split(temp, "MEMBER INCIDENCES");
    if(vect_temp.size()==1){
    	cerr<<"NO Member Incidences \n";
    	return ;
	}
	
	
    temp=split(vect_temp[1], "START GROUP DEFINITION")[0];
    vect_temp=split(temp, ";");
    for(int i=0;i<vect_temp.size()-1;i++)
    {	
        vect_temp1=split(vect_temp[i], " ");
        Member m;
        istringstream(vect_temp1[0])>>m.id;
        for(int j=1;j<vect_temp1.size();j++)
        {
            int l;
            istringstream(vect_temp1[j])>>l;
            m.joint_id.push_back(l);
        }
        job_members.push_back(m);
        vect_temp1.clear();
        
    }
    vect_temp.clear();
}
	
void Structure::getMemberPro(string temp){

    vector<string> vect_temp1;
    vector<string> vect_temp;
    vect_temp1=split(temp, "MEMBER PROPERTY");
     if(vect_temp1.size()==1){
    	cerr<<"NO Member Property \n";
    	return ;
	}
	
	
	for(int ii=1; ii<vect_temp1.size();ii++){
		temp=split(vect_temp1[ii], "CONSTANTS")[0];
		
		vect_temp=split(temp," ");
		
		MemPro *me;
		me=new MemPro;
		if(!isdigit(vect_temp[0][0])){
			string x=vect_temp[0];
			me->country=x;
		}
		for(int i=1; i<vect_temp.size();i++){
			
			float l=0,l1=0;
			if(isdigit(vect_temp[i][0])){
				istringstream(vect_temp[i])>>l;
				(*me).member_id.push_back(l);
				continue;
			}
				if(vect_temp[i]=="TO"){
					istringstream(vect_temp[i-1])>>l;
					istringstream(vect_temp[i+1])>>l1;
					for( int j=l+1;j<l1;j++){
						
						(*me).member_id.push_back(j);
					}
				}
				
				if(vect_temp[i]=="PRIS"){
					istringstream(vect_temp[i+2])>>l;
					istringstream(vect_temp[i+4])>>l1;
					(*me).type=vect_temp[i];
					(*me).YD=l;
					(*me).ZD=l1;
					member_pr.push_back(*me);
					delete me;
					MemPro *me;
					me=new MemPro;
					me->country=x;
					i=i+4;
					
				}
			
		}
	}
    

}


void Structure::getDesign(string temp){

    vector<string> vect_temp;
    vector<string> vect_temp1;
	
	//getting concrete info 
    vect_temp=split(temp,"START CONCRETE DESIGN");
     if(vect_temp.size()==1){
    	cerr<<"NO Concrete design \n";
    	return ;
	}
    temp=split(vect_temp[1],"DESIGN BEAM")[0];
    vect_temp=split(temp," ");
    
    con_des.code=vect_temp[1];
    CodeType *cd;
    cd=new CodeType;
	for(int i=2; i<vect_temp.size();i++){
		float l=0,l1=0;
		if(isdigit(vect_temp[i][0])){
			istringstream(vect_temp[i])>>l;
			cd->member_id.push_back(l);
			continue;
		}
		
		
		if(vect_temp[i]=="TO"){
			istringstream(vect_temp[i-1])>>l;
			istringstream(vect_temp[i+1])>>l1;
			for( int j=l+1;j<l1;j++){
					cd->member_id.push_back(j);
				}
		}
		else{
			if(isalpha(vect_temp[i][0])){
				if(i>5){
				  	con_des.cty.push_back(*cd);
				 	 	
				}
				delete cd;
				CodeType *cd;
				cd=new CodeType;
				cd->code=vect_temp[i];
				cd->section=vect_temp[i+1];
				i=i+2;
				if(vect_temp[i]=="ALL"){
    			
    			for(int ii=0;ii<job_members.size();ii++)
    				(*cd).member_id.push_back(job_members[ii].id);
    				continue;
    		}
				
			}
		}
	}
   con_des.cty.push_back(*cd);  
}
	  
void Structure::getDesignBeam(string temp){
   	//getting design beam 
   	vector<string> vect_temp;
    vector<string> vect_temp1;
    
	vect_temp=split(temp,"DESIGN BEAM");
	 if(vect_temp.size()==1){
    	cerr<<"NO Design Beam \n";
    	return ;
	}
	temp=split(vect_temp[1],"DESIGN COLUMN")[0];
    vect_temp=split(temp," ");
     for(int i=0; i<vect_temp.size();i++){
    	float l=0,l1=0;
    	if(isdigit(vect_temp[i][0])){
    		istringstream(vect_temp[i])>>l;
    		beam.push_back(l);
    		continue;
    	}
    	if(vect_temp[i]=="TO"){
    		istringstream(vect_temp[i-1])>>l;
    		istringstream(vect_temp[i+1])>>l1;
    		for( int j=l+1;j<l1;j++){
    				beam.push_back(j);
    			}
    		}
    	
    }
    
}

void Structure::getDesignColumn(string temp){
   	//getting design beam 
   	vector<string> vect_temp;
    vector<string> vect_temp1;
	//getting design column
    vect_temp=split(temp,"DESIGN COLUMN");
     if(vect_temp.size()==1){
    	cerr<<"NO Member Incidences \n";
    	return ;
	}
    vect_temp=split(vect_temp[1]," ");
    for(int i=0; i<vect_temp.size();i++){
		float l=0,l1=0;
		if(isdigit(vect_temp[i][0])){
			istringstream(vect_temp[i])>>l;
			column.push_back(l);
			continue;
		}
		if(vect_temp[i]=="TO"){
			istringstream(vect_temp[i-1])>>l;
			istringstream(vect_temp[i+1])>>l1;
			for( int j=l+1;j<l1;j++){
				column.push_back(j);
			}
		}
	}
}

void Structure::getSupports(string temp)
{
    temp=split(temp, "SUPPORTS")[1];
    if(split(temp1, type).size()==1)     //check
    {
    	cerr<<" No Supports defined";
        return;
    }
    getSupportsTypes(temp,"FIXED");
    getSupportsTypes(temp,"HINGED");
    getSupportsTypes(temp,"ROLLED");
    getSupportsTypes(temp,"PINNED");
	//add others as well
}

void Structure::getSupportsTypes(string temp1,string type)
{
    vector<string> vect_temp, vect_temp1; 
    if(split(temp1, type).size()==1)     //check
    {
        return;
    }
    temp1=split(temp1, type)[0];
    //cout<<temp1;
    vect_temp=split(temp1, "TO");
    temp1="";
    for(int i=0;i<vect_temp.size();i++)
    {
        vect_temp1.clear();
        vect_temp1=split(vect_temp[i], " ");
        if(temp1!="")
        {
           int ii, iii;
           istringstream(temp1)>>ii;
           istringstream(vect_temp1[0])>>iii;
           for(int j=ii+1;j<iii;j++)
           {
               //cout<<j<<endl;
               for(int k=0;k<job_joints.size();k++)
                {
                    if(job_joints[k].id==j)
                    {
                        job_joints[k].support=type;
                        break;
                    }
                }
           }
        }
        for(int j=0;j<vect_temp1.size();j++)
        {
            if(isdigit(vect_temp1[j][0]))
            {
                temp1=vect_temp1[j];
                for(int k=0;k<job_joints.size();k++)
                {
                    int kk;
                    istringstream(vect_temp1[j])>>kk;
                    if(job_joints[k].id==kk)
                    {
                        job_joints[k].support=type;
                        break;
                    }
                }
            }
        }
    }
}

