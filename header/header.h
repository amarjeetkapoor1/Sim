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


#include <mysql_connection.h>

#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/resultset.h>
#include <cppconn/statement.h>
#include <cppconn/prepared_statement.h>

#define USER "root"
#define PASSWORD "hashtagme"

using namespace std;
/*!
	\brief This function is used to split string bases on given delimiter 
	and for given no. of times. By default cut is 0 which means it will
	split for all possible delimiter.
	\param str string to be split
	\param del delimiter to be used
	\param cut no. of splits to be performed
*/

vector<string> split(string, string ,int cut=0);


#endif
