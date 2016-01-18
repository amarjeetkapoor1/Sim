#include "header/structure.h"


void job::print(){
    cout<<"date,"<<date<<endl;
    cout<<"JOB NAME,"<<name<<endl;
    cout<<"JOB CLIENT,"<<client<<endl;
    cout<<"JOB NO,"<<jobid<<endl;
    cout<<"JOB COMMENT,"<<comment<<endl;
    cout<<"CHECKER NAME,"<<checker_name<<endl;
    cout<<"ENGINEER NAME,"<<engineer_name<<endl;
    cout<<"APPROVED NAME,"<<approved_name<<endl;
    cout<<"CHECKER DATE,"<<checker_date<<endl;
    cout<<"JOB REF,"<<ref<<endl;
    cout<<"JOB PART,"<<part<<endl;
    cout<<"JOB REV,"<<rev<<endl;
    cout<<"APPROVED DATE,"<<approved_date<<endl;

}

void structure::insert(){
	string query;
	int j;
	int z;
	j=job1.insert(z);
	insert_member(j,z);	
	sql::Driver *driver;
	sql::Statement *stmt;
	sql::Connection *con;
	sql::PreparedStatement  *prep_stmt;
	//create a database connection using the Driver 
	driver =get_driver_instance();
	con = driver->connect("localhost","root","hashtagme");
	stmt = con->createStatement();
	stmt->execute("USE SIM");
	//istringstream(jobid)>>i;
	for(int i=0;i<job_joints.size();i++){
		prep_stmt = con->prepareStatement("INSERT INTO JOINT(jobid,id,x,y,z,serial) VALUES (?,?,?,?,?,?)");
		prep_stmt->setInt(1,j);
		prep_stmt->setInt(2,job_joints[i].id);
		prep_stmt->setInt(3,job_joints[i].x);
		prep_stmt->setInt(4,job_joints[i].y);
		prep_stmt->setInt(5,job_joints[i].z);
		prep_stmt->setInt(6,z);
		prep_stmt->execute();
	}
	
	
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
    cout<<"poison,"<<job_material[i].poison<<endl;
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
    	for(int j=0;j<member_pr[i].joint_id.size();j++)
    		cout<<","<<member_pr[i].joint_id[j];
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
    string str="", temp, temp1;
    vector<string> vect_temp2;
    vector<string> vect_temp3;
    char ch;
    
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
   	material3(str);
     return;
    
     
    //gettin member properties
    get_member_pro(temp);
    //getting concerete design
    get_design(temp);
    

}



int job::insert(int &r){
    sql::Driver *driver;
	sql::Statement *stmt;
	sql::Connection *con;
	sql::PreparedStatement  *prep_stmt;
	sql::ResultSet *result;
	//create a database connection using the Driver 
	driver =get_driver_instance();
	con = driver->connect("localhost","root","hashtagme");
	stmt = con->createStatement();

	stmt->execute("USE SIM");
	string query;
	int i;
	istringstream(jobid)>>i;
	prep_stmt = con->prepareStatement("INSERT INTO JOB(jobid, jobname, date, client, comment, checker_name, engineer_name, approved_name, checker_date, ref, part, rev, approved_date) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)");
	prep_stmt->setInt(1,i);
	prep_stmt->setString(2,name);
	prep_stmt->setString(3,date);
	prep_stmt->setString(4,client);
	prep_stmt->setString(5,comment);
	prep_stmt->setString(6,checker_name);
	prep_stmt->setString(7,engineer_name);
	prep_stmt->setString(8,approved_name);
	prep_stmt->setString(9,checker_date);
	prep_stmt->setString(10,ref);
	prep_stmt->setString(11,part);
	prep_stmt->setString(12,rev);
	prep_stmt->setString(13,approved_date);
	prep_stmt->execute();
	result=stmt->executeQuery("select max(serial) from JOB");
	result->next();
	r=result->getInt(1);
	delete stmt;
	delete con;
	return i;	
	
}

void structure::insert_member(int j,int z){
	sql::Driver *driver;
	sql::Statement *stmt;
	sql::Connection *con;
	sql::PreparedStatement  *prep_stmt;
	//create a database connection using the Driver 
	driver =get_driver_instance();
	con = driver->connect("localhost","root","hashtagme");
	stmt = con->createStatement();
	stmt->execute("USE SIM");
	//istringstream(jobid)>>i;
	for(int i=0;i<job_members.size();i++){
	prep_stmt = con->prepareStatement("INSERT INTO MEMBER(serial,member_id) VALUES (?,?)");
	prep_stmt->setInt(1,z);
	prep_stmt->setInt(2,job_members[i].id);
	prep_stmt->execute();
	for(int k=0;k<job_members[i].joint_id.size();k++){
        prep_stmt = con->prepareStatement("INSERT INTO JOINTMEMBER(serial,member_id,jointid) VALUES (?,?,?)");
		prep_stmt->setInt(1,z);
		prep_stmt->setInt(2,job_members[i].id);
		prep_stmt->setInt(3,job_members[i].joint_id[k]);
		prep_stmt->execute();
        }
        
	}
	delete stmt;
	delete con;
}



string job:: get( fstream &file){
	string str="", temp, temp1;
    vector<string> vect_temp2;
    vector<string> vect_temp3;
    char ch;
    
    //replacing newline wiht space
    while(file.get(ch))
    {
        if(ch=='\r')
        	continue;
        str+=ch;
    }
    
	//get enginner name 
    temp=split(str, "START JOB INFORMATION")[1];
    temp1=split(temp, "END JOB INFORMATION")[0];
   	vect_temp2=split(temp1, "\n");
   	for(int i=0;i<vect_temp2.size();i++)
   	{
   		vect_temp3=split(vect_temp2[i], " ", 2);
   		string h=vect_temp3[0]+vect_temp3[1];
		if( h=="ENGINEERDATE")
		{
			date=vect_temp3[2];
		}
		if( h=="JOBNAME")
		{
			name=vect_temp3[2];
		}
		if( h=="JOBCLIENT")
		{
			client=vect_temp3[2];
		}
		if( h=="JOBNO")
		{
			jobid=vect_temp3[2];

		}
		if( h=="JOBREV")
		{
			rev=vect_temp3[2];
		}
		if( h=="JOBPART")
		{
			part=vect_temp3[2];
			
		}
		if( h=="JOBREF")
		{
			ref=vect_temp3[2];
			
		}
		if( h=="JOBCOMMENT")
		{
			comment=vect_temp3[2];
			
		}
		if( h=="ENGINEERNAME")
		{
			engineer_name=vect_temp3[2];
			
		}
		if( h=="CHECKERNAME")
		{
			checker_name=vect_temp3[2];
			
		}
		if( h=="APPROVEDNAME")
		{
			approved_name=vect_temp3[2];
			
		}
		if( h=="CHECKERDATE")
		{
			checker_date=vect_temp3[2];
			
		}
		if( h=="APPROVEDDATE")
		{
			approved_date=vect_temp3[2];
			
		}
   		vect_temp3.clear();
   	}
   	vect_temp2.clear();
   	
   	return str;
}
	
void structure::material3(string str){
	string temp, temp1;
    vector<string> vect_temp2;
    vector<string> vect_temp3;
    char ch;
    temp=split(str, "DEFINE MATERIAL START")[1];
    temp1=split(temp, "END DEFINE MATERIAL")[0];
	vect_temp2=split(temp1, "\n");
	int j=0;
	for(int j=0;j<vect_temp2.size();){
		material mater ;
		int z=j;
		for(int i=z;i<9+z && j<vect_temp2.size();i++)
		{	
			vect_temp3=split(vect_temp2[i], " ", 1);
   			string h=vect_temp3[0];
			if(i==z){
				mater.name=vect_temp3[0]+" "+vect_temp3[1];;
				j++;   
 				continue;
			}
			if(h=="E")
			{
				mater.E=vect_temp3[1];;
				j++;   
 				continue;
			}
			if(h=="POISSON")
			{
				istringstream(vect_temp3[1])>>mater.poison;
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
				mater.alpha=vect_temp3[1];;
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
				mater.type=vect_temp3[1];;
				j++;   
 				continue;
			}
			if(h=="STRENGTH")
			{
				mater.strength=vect_temp3[1];;
				j++;   
 				continue;
			}
			if(h=="G")
			{
				mater.G=vect_temp3[1];;
				j++;   
 				continue;
			}
			
			break;
			
		}
		job_material.push_back(mater);
   }
}
	
void structure::get_joint(string str){
	string temp, temp1;
    vector<string> vect_temp2;
    vector<string> vect_temp3;
    char ch;
    temp=str;
	temp=split(temp, "JOINT COORDINATES")[1];
    temp1=split(temp, "MEMBER INCIDENCES")[0];
    vect_temp2=split(temp1, "; ");
    for(int i=0;i<vect_temp2.size()-1;i++)
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
	
void structure::get_member_pro(string str){

	string temp, temp1;
    vector<string> vect_temp2;
    vector<string> vect_temp3;
    char ch;
	
	temp=split(str, "END DEFINE MATERIAL")[1];
    temp1=split(temp, "MEMBER PROPERTY INDIAN")[1];
    temp1=split(temp1, "CONSTANTS")[0];
    vect_temp2=split(temp1," ");
    mem_pro *me;
    me=new mem_pro;
    for(int i=0; i<vect_temp2.size();i++){
    	
    	float l=0,l1=0;
    	if(isdigit(vect_temp2[i][0])){
    		istringstream(vect_temp2[i])>>l;
    		(*me).joint_id.push_back(l);
    		continue;
    	}
    		if(vect_temp2[i]=="TO"){
    			istringstream(vect_temp2[i-1])>>l;
    			istringstream(vect_temp2[i+1])>>l1;
    			for( int j=l+1;j<l1;j++){
    				
    				(*me).joint_id.push_back(j);
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
void structure::get_design(string str){
	string temp, temp1;
    vector<string> vect_temp2;
    vector<string> vect_temp3;
    char ch;
	
	//getting concrete info 
    temp1=split(str,"START CONCRETE DESIGN")[1];
    
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
	temp1=split(str,"DESIGN BEAM")[1];
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
    temp1=split(str,"DESIGN COLUMN")[1];
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
