/*!
 *	\file header.cpp
 *
 *  \brief It contain defination of function split(), toList(),splitOr().. used to parse.    
 *
 *      
 *	compiler g++
 *
 *  \author amarjeet singh kapoor
 *      
 */

#include "header/header.h"

using namespace std;

vector<string> split(string str, string del,int cut){
    vector<string> arr;
    while(str!=del && str!="")
    {
    	if(cut>0)
    	{
    		if(arr.size()==cut)
    		{
    			arr.push_back(str);
    			return arr;
    		}
    	}
        if(str.find(del)>str.length())
        {
            arr.push_back(str);
            break;
        }
        if(str.substr(0, str.find(del)).length())
            arr.push_back(str.substr(0, str.find(del)));
        if((str.find(del)+del.length())<str.length())
            str=str.substr(str.find(del)+del.length());
        else
            str="";
    }
    return arr;
}

vector<int> toList(string temp) //this function a list of integers parsing from a list which contains TO, can be used anywhere
{
	//temp is the string containg only the list of numbers separated by spaces and the occasional TO
    vector<string> temp2, temp3;
    vector<int> retVec;  //the vector that will returned at the end
	//logic
    temp2=split(temp, "TO");
    for(int i=0;i<temp2.size();i++)
    {
    	int in=0;
        temp3.clear();
        temp3=split(temp2[i], " ");
        if(retVec.size()!=0)
        {
        	in=1;
            int x, y,z=1;
            x=retVec[retVec.size()-1];
            istringstream(temp3[0])>>y;
            if(temp3[1]=="BY"){
            	in=3;
            	istringstream(temp3[2])>>z;
            }
          
            for(int i=x+z;i<=y;i=i+z)
            {
                retVec.push_back(i);
            }
        }
        for(int j=in;j<temp3.size();j++)
        {
			if(!isdigit(temp3[j][0]))
            {
                continue;
            }
            int x;
            istringstream(temp3[j])>>x;
            retVec.push_back(x);
        }
    }
    return retVec;
}


vector<string> splitOr(string main, string cut,string &ans ){
	vector<string> temp,temp1;
	temp=split(cut,",");
	for(int i=0; i<temp.size();i++){
		temp1=split(main,temp[i]);
			if(temp1.size()>1){
				ans=temp[i];
				break;
			}
		}
	return temp1;	
}

vector<string> splitOrStar(string main, string cut,vector<string> &ans ){
	vector<string> temp,temp1,retemp;
	temp=split(cut,",");
	for(int i=0; i<temp.size();i++){
		temp1=split(main,temp[i],1);
			if(temp1.size()>1){
				ans.push_back(temp[i]);
				retemp.push_back(temp1[1]);
			}
		}
	return retemp;	
}




vector<int> toListVector(vector<string> vect_temp1){
	string temp;
	for(int jj=0;jj<vect_temp1.size();jj++){
	    temp=temp+vect_temp1[jj]+" ";
	 }
	 return toList(temp);
}


