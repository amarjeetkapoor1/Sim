/*!
 *	\file job.h 
 *
 *	\brief  It contain class to define job
 *
 *      
 *  Compiler  g++
 *
 *  \author amarjeet singh kapoor
 *      
 */


#ifndef _JOB_H
#define _JOB_H
#include "header.h"


class Job{

	string date,name,client,job_id,comment;
	string checker_name,engineer_name,approved_name,checker_date;
	string ref,part,rev,approved_date,type,title;
	public:
	  
	  /*!
			\brief This member function is used to initialize job property 
			\param file file to be parsed
    */
		string get(fstream &file);
		
		/*!
			\brief This member function is used to print job property 
    */
		void print();
		
		/*!
			\brief This member function is used to insert job 
			property
			\param z value of jobid
    	*/
		void insert(int &);

};

#endif
