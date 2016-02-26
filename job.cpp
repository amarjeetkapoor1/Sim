/*!
 *	\file job.cpp
 *
 *	\brief  It contain definitions for member functions of class job
 *
 *      
 *  Compiler  g++
 *
 *  \author amarjeet singh kapoor
 *      
 */

#include"header/job.h"

using namespace std;
using namespace sql;

string job:: get( fstream &file)
{
	string str="", temp;
    vector<string> vect_temp2;
    vector<string> vect_temp3;
    char ch;
    
    //replacing newline wiht space
    while(file.get(ch))
    {
    	if(ch=='*'){
    		while(ch!='\n' ){
    			file.get(ch);
    			continue;
    		}
    		if(ch=='\n')
    			continue;
    	}
        if(ch=='\r')
        	continue;
        str+=ch;
    }
    
    
    
    
    
	//get enginner name 
    vect_temp2=split(str, "START JOB INFORMATION");
    if(vect_temp2.size()==1){
    	cerr<<"NO Start job Information \n";
    	return str;
	}    	
    temp=split(vect_temp2[1], "END JOB INFORMATION")[0];
    vect_temp2.clear();
   	vect_temp2=split(temp, "\n");
   	
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
			job_id=vect_temp3[2];

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

void job::print()
{
    cout<<"date,"<<date<<endl;
    cout<<"JOB NAME,"<<name<<endl;
    cout<<"JOB CLIENT,"<<client<<endl;
    cout<<"JOB NO,"<<job_id<<endl;
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



void job::insert(int &r)
{
    sql::Driver *driver;
	sql::Statement *stmt;
	sql::Connection *con;
	sql::PreparedStatement  *prep_stmt;
	sql::ResultSet *result;
	//create a database connection using the Driver 
	driver =get_driver_instance();
	con = driver->connect("localhost",USER,PASSWORD);
	stmt = con->createStatement();

	stmt->execute("USE Sim");
	prep_stmt = con->prepareStatement("INSERT INTO Job(id, name, date,client ,comment, checker_name, engineer_name, approved_name, checker_date, ref, part, rev, approved_date) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)");
	prep_stmt->setString(1,job_id);
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
	result=stmt->executeQuery("select max(job_id) from Job");
	result->next();
	r=result->getInt(1);
	delete stmt;
	delete con;
}
