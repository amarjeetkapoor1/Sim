//for all 

 temp2=split(temp3[1],"\n",1);
    temp2=split(temp2[0]," ");
    if(temp2[0]=="BUT"){
    	for(int i=0;i<temp2.size();i++){
			if(temp2[i]=" "){
				continue;
			}
			
		}
	}
	
	
void Structure::getJointLoad(string temp){
	string temp1;
    vector<string> vect_temp,vect_temp1;
    vect_temp=split(temp, "\nMEMBER LOAD ");
    if(vect_temp.size()==1)
        return; 
