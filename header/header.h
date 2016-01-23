#ifndef _HEADER_H_
#define _HEADER_H_

#include<iostream>
#include<fstream>
#include<cstring>
#include <vector>
#include <sstream>
#include<cctype>


#include <mysql_connection.h>

#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/resultset.h>
#include <cppconn/statement.h>
#include <cppconn/prepared_statement.h>


using namespace std;
using namespace sql;

vector<string> split(string, string ,int cut=0);


#endif
