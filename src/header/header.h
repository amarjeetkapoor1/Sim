/*!
 *	\file header.h 
 *
 *  \brief It contain directives to include all necessary headers and bases 
 *	function split used to parse.    
 *
 *      
 *	compiler g++
 *
 *  \author amarjeet singh kapoor
 *      
 */
#ifndef _HEADER_H_
#define _HEADER_H_

#include<iostream>
#include<fstream>
#include<cstring>
#include <vector>
#include <sstream>
#include<cctype>
#include<string>


#include <mysql_connection.h>

#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/resultset.h>
#include <cppconn/statement.h>
#include <cppconn/prepared_statement.h>

#define USER "root"
#define PASSWORD "hashtagme"

using namespace std;

class base{
	public:
	sql::Driver *driver;
	sql::Statement *stmt;
	sql::Connection *connection;
	sql::PreparedStatement  *prep_stmt;
	sql::ResultSet *result;
	
};

/*!
	\brief This function is used to split string bases on given delimiter 
	and for given no. of times. By default cut is 0 which means it will
	split for all possible delimiter.
	\param str string to be split
	\param del delimiter to be used
	\param cut no. of splits to be performed
	\return vector<string>
*/

vector<string> split(string, string ,int cut=0);

/*!
	\brief This function is used to return vector of int
	base on given rule from given string
	\n
	list = *{ i 1 i 2 i 3 ... | i 1 TO i 2 (BY i 3 ) | X or Y or Z }
	\param temp string to be split
	\return vector<int>

*/
vector<int> toList(string temp);
/*!
	\brief This function is used to return vector of int
	base on given rule from given vectorof i*
	\n
	list = *{ i 1 i 2 i 3 ... | i 1 TO i 2 (BY i 3 ) | X or Y or Z }
	\param temp string to be split
	\return vector<int>

*/

vector<int> toListVector(vector<string> vect_temp1);

/*!
	\brief This function is used to split string bases on given delimiter based on follwing split rule
{ X | Y | Z | GX | GY | GZ | PX | PY | PZ }
	\param string string to be split
	\param string string of delimiters
	\param string delimiter that worked
	\return vector<string>
*/
vector<string> splitOr(string, string ,string&,int cut=0);

/*!
	\brief This function is used to split string bases on given delimiter based on follwing split rule
*{ X | Y | Z | GX | GY | GZ | PX | PY | PZ }
	\param string string to be split
	\param string string of delimiters
	\param vector<string> delimiter that worked
	\return vector<string>
*/
vector<string> splitOrStar(string main, string cut,vector<string> &ans );

#endif
