/*!
 *	\file structure.cpp 
 *
 *	\brief  It contain definitions for member functions of class Structure
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
		stmt->execute("USE Sim");
		stmt->execute("start transaction");
		int z;
		job.insert(z,*connection);	
		for(int i=0;i<job_joints.size();i++){
			message=job_joints[i].insert(z,*connection);
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
		prep_stmt = connection->prepareStatement("INSERT INTO Job_material(job_id,name,E,poisson,density,damp,alpha,G,strength,type) VALUES (?,?,?,?,?,?,?,?,?,?)");
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
			prep_stmt = connection->prepareStatement("INSERT INTO Member(job_id,member_id) VALUES (?,?)");
			prep_stmt->setInt(1,z);
			stringstream sstm;
			sstm<<"Duplicate Member id = "<<job_members[i].id;
			message = sstm.str();
			prep_stmt->setInt(2,job_members[i].id);
			prep_stmt->execute();
			for(int k=0;k<job_members[i].joint_id.size();k++){
		  prep_stmt = connection->prepareStatement("INSERT INTO Member_incidence(job_id,member_id,joint_id) VALUES (?,?,?)");
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
		prep_stmt = connection->prepareStatement("INSERT INTO Member_property(job_id,idd,type,YD,ZD) VALUES (?,?,?,?,?)");
		prep_stmt->setInt(1,z);
		prep_stmt->setInt(2,i);
		prep_stmt->setString(3,member_pr[i].type);
		prep_stmt->setDouble(4,member_pr[i].YD);
		prep_stmt->setDouble(5,member_pr[i].ZD);
		prep_stmt->execute();
		for(int j=0; j<member_pr[i].member_id.size();j++){
			prep_stmt = connection->prepareStatement("UPDATE Member SET member_property = ? where job_id = ? and member_id= ?");
			prep_stmt->setDouble(1,i);
			prep_stmt->setDouble(2,z);
			prep_stmt->setInt(3,member_pr[i].member_id[j]);
			prep_stmt->execute();
		}
	}
}

Structure::~Structure(){
	delete stmt;
	delete connection;
}
	
void Load::print(){		
	cout<<id<<","<<type<<","<<reduce<<","<<title<<","<<endl;
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
        job_joints[i].print();
        cout<<endl;
    }
    
    //printing member incidences
    cout<<"MEMBER INCIDENCES:\n";
    cout<<"member id ,beta,joint id ,joint id , .... \n";
    for(int i=0;i<job_members.size();i++)
    {
        job_members[i].print();
        cout<<endl; 
        
    }
    
    //printing material defination
     for(int i=0;i<job_material.size();i++){
    	job_material[i].print();
    }
    
    //printing member property
    cout<<"MEMBER PROPERTY \n";
    cout<<"country,TYPE, YD, ZD, Member,  Member, Member, ...... \n";
    for(int i=0;i<member_pr.size();i++){
    	member_pr[i].print();
    	cout<<endl;
    }
    
    //printing concrete design info
    con_des.print();
    
    
    cout<<"LOAD"<<endl;
    for(int i=0;i<load.size();i++){
    	load[i].print();
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
	connection = driver->connect("localhost",USER,PASSWORD);
	stmt = connection->createStatement();
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
   
   //get units
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
    getBeta(str);
    getLoad(str);
    getJointLoad(str);
    getMemberLoad(str);
    

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


/*
SUPPORTS
{ joint-list | ni TO nj GENERATE } { PINNED | FIXED ( BUT
release-spec (spring-spec) ) | ENFORCED ( BUT release-spec)
}
release-sepc = { FX | FY | FZ | MX | MY | MZ }
spring-spec = *{KFX f1 | KFY f2 | KFZ f3 | KMX f4 | KMY f5
| KMZ f6 }
*/

void Structure::getSupports(string temp)
{
    temp=split(temp, "SUPPORTS")[1];
    
    getSupportsTypes(temp,"FIXED");
    getSupportsTypes(temp,"HINGED");
    getSupportsTypes(temp,"ROLLED");
    getSupportsTypes(temp,"PINNED");
	//add others as well
}

void Structure::getSupportsTypes(string temp,string type)
{
	vector<string> temp2, temp3;
	
	
    if(split(temp, type).size()==1)
    {
        return;
    }
    temp=split(temp, type)[0];
    vector<int> lst=toList(temp);
    for(int i=0;i<lst.size();i++)
    {
        for(int j=0;j<job_joints.size();j++)
        {
            if(job_joints[j].id==lst[i])
            {
                job_joints[j].support=type;
                break;
            }
        }
    }
}



//temp is the big string, IT MUST NOT HAVE ITS \n REPLACED BY SPACES, USE THE \n VERSION OF THE BIG
/*
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

*/	

void Structure::getBeta(string temp){
    
    //temp contains the big string with \n's and not the spaces
    string temp1;
    vector<string> temp2;
    vector<string> temp3;
    temp2=split(temp, "BETA");
    
    temp1=split(temp2.back(), "\n")[0];
    temp2.pop_back();
    temp2.push_back(temp1+"\n");
    if(temp2.size()==1)
        return;
    temp3=split(temp2[1], "ALL");
    if(temp3.size()!=1)
    {
        for(int i=0;i<job_members.size();i++)
        {
            job_members[i].beta=temp3[0];
        }
        //return;
    }
    temp3.clear();
    for(int i=1; i<temp2.size();i++)
    {
        temp1=split(temp2[i], "MEMB")[1];
        vector<int> lst=toList(temp1);  //this function's definition is in the support.txt file
        for(int k=0;k<lst.size();k++)
        {
            //cout<<lst[k]<<endl;
            for(int j=0;j<job_members.size();j++)
            {
                if(job_members[j].id==lst[k])
                {
                    job_members[j].beta=split(temp2[i], "MEMB")[0];
                    break;
                }
            }
        }
    }
}

void Structure::getLoad(string temp){
	string temp1;
    vector<string> vect_temp,vect_temp1;
    vect_temp=split(temp, "\nLOAD ");
    if(vect_temp.size()==1)
        return; 
    for(int i=1 ;i<vect_temp.size();i++){
		Load *ld;
		ld=new Load;
		
		temp=split(vect_temp[i], "\n",1)[0];
		vect_temp1=split(temp, "TITLE");
		if(vect_temp1.size()>1){
			
			ld->title=vect_temp1[1];
		}
		temp=vect_temp1[0];
		vect_temp1.clear();
		vect_temp1=split(temp, "LOADTYPE");
		if(vect_temp1.size()>1){
			temp=vect_temp1[0];
			vect_temp1=split(vect_temp1[1]," ");
			ld->type=vect_temp1[0];			
			if(vect_temp1.size()>1 && vect_temp1[1]=="REDUCIBLE")
				ld->reduce=true;
			else
				ld->reduce=false;
		}
		
		vect_temp1.clear();
		istringstream(vect_temp1[0])>>ld->id;
		load.push_back(*ld);
		 delete ld;
	}
}


	
/*JOINT LOAD
joint-list *{ FX f 7 | FY f 8 | FZ f 9 | MX f 10 | MY f 11 | MZ f 12
}

*/
	
void Structure::getJointLoad(string temp){
	string temp1;
    vector<string> vect_temp,vect_temp1;
    vect_temp=split(temp, "\nJOINT LOAD");
    if(vect_temp.size()==1)
        return;
       
    vect_temp=split(vect_temp[1],"\n");
    JointLoad *jl;
    for(int i=0;i<vect_temp.size();i++){
    	jl= new JointLoad;
    	vect_temp1=split(vect_temp[i]," ");
    	if(isdigit(vect_temp1[i][0])){
	    	for(int j=vect_temp1.size()-2;j>-1;j=j-2){
	    		
	    		if(isdigit(vect_temp1[j][0]) )
	    			continue;
				else{
					
					if(vect_temp1[j]=="FX"){
						istringstream(vect_temp1[j+1])>>jl->FX;
                        vect_temp1.pop_back();
                        vect_temp1.pop_back();
						continue;
					}
					if(vect_temp1[j]=="FY"){
						istringstream(vect_temp1[j+1])>>jl->FY;
                        vect_temp1.pop_back();
                        vect_temp1.pop_back();
						continue;
					}
					if(vect_temp1[j]=="FZ"){
						istringstream(vect_temp1[j+1])>>jl->FZ;
                        vect_temp1.pop_back();
                        vect_temp1.pop_back();
						continue;
					}
					if(vect_temp1[j]=="MX"){
						istringstream(vect_temp1[j+1])>>jl->MX;
                        vect_temp1.pop_back();
                        vect_temp1.pop_back();
						continue;
					}
					if(vect_temp1[j]=="MY"){
						istringstream(vect_temp1[j+1])>>jl->MY;
                        vect_temp1.pop_back();
                        vect_temp1.pop_back();
						continue;
					}
					if(vect_temp1[j]=="MZ"){
						istringstream(vect_temp1[j+1])>>jl->MZ;
                        vect_temp1.pop_back();
						vect_temp1.pop_back();
						continue;
					}
				}
             }
            
            
	    	vector <int>vect_temp2=toListVector(vect_temp1);
	    	for(int k=0;k<vect_temp2.size();k++){
	    		for(int j=0;j<job_joints.size();j++){
		            if(job_joints[j].id==vect_temp2[k]){
		                job_joints[j].jointload=*jl;
		                
		            }
            	}
	    	}
	    	
          }
          else{
          	break;
          	}
	    	jl=new JointLoad;
	 }
	    delete jl;
}

/*
MEMBER LOAD
member-list { { UNI | UMOM } dir-spec f 1 f 2 f 3 f 4 | { CON |
CMOM } dir-spec f 5 f 6 f 4 | LIN dir-spec f 7 f 8 f 9 | TRAP dir-
spec f 10 f 11 f 12 f 13 }

*/
void Structure::getMemberLoad(string temp){
	string temp1,cut="UNI,UMOM,CON,CMOM,LIN,TRAP",ans;
    vector<string>vect_temp,vect_temp1;
    vect_temp=split(temp, "\nMEMBER LOAD");
    if(vect_temp.size()==1)
        return;
    vect_temp=split(vect_temp[1], "\n");
    
    for(int i=0;i<vect_temp.size();i++){
    	MemberLoad *ml;
    	ml=new MemberLoad;
    	if(isdigit(vect_temp[i][0])){
			vect_temp1=splitOr(vect_temp[i],cut,ml->code);
			vector <int>vect_temp2=toList(vect_temp1[0]);
			vect_temp1=split(vect_temp1[1]," ");
			ml->specCode=vect_temp1[0];
			istringstream(vect_temp1[1])>>ml->spec;
		   	for(int j=2;j<vect_temp1.size();j++){
		   		float a;
		   		istringstream(vect_temp1[1])>>a;
		   		ml->f.push_back(a);
			}
		   	for(int k=0;k<vect_temp2.size();k++){
					for(int j=0;j<job_members.size();j++){
				        if(job_members[j].id==vect_temp2[k]){
				            job_members[j].memberload=ml;
				            memberload.push_back(*ml);
				        }
		        	}
				}
			ml=new MemberLoad;
		}
		else{
			
			delete ml;
			break;
		}
	}		

}


    
