#ifndef _JOB_H
#define _JOB_H
#include "header.h"


class job{
	string date,name,client,job_id,comment;
	string checker_name,engineer_name,approved_name,checker_date;
	string ref,part,rev,approved_date;
	public:
		string get(fstream &file);
		void print();
		int insert(int &);

};

#endif
