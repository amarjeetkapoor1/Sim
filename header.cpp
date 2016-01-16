#include "header/header.h"

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
