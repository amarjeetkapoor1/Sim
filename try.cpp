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
	
/*JOINT LOAD
joint-list *{ FX f 7 | FY f 8 | FZ f 9 | MX f 10 | MY f 11 | MZ f 12
}

*/
	
void Structure::getJointLoad(string temp){
	string temp1;
    vector<string> vect_temp,vect_temp1;
    vect_temp=split(temp, "\nJOINT LOAD ");
    if(vect_temp.size()==1)
        return;
    vect_temp=split(vect_temp,"\n");
    for(int i=0;i<vect_temp.size();i++){
    	JoinLoad *jl;
    	jl= new JointLoad;
    	vect_temp1=split(vect_temp[i]," ");
    	if(isdigit(vect_temp1[0])){
	    	for(int j=vect_temp1.size()-2;j>=0;j=j-2){
	    		if(isdigit(vect_temp1[j])){
	    			break;
	    		else{
	    			if(vect_temp1[j]=="FX"){
	    				jl->FX=vect_temp1[j+1];
	    				vect_temp1.pop();
	    				vect_temp1.pop();
	    				continue;
	    			}
	    			if(vect_temp1[j]=="FY"){
	    				jl->FY=vect_temp1[j+1];
	    				vect_temp1.pop();
	    				vect_temp1.pop();
	    				continue;
	    			}
	    			if(vect_temp1[j]=="FZ"){
	    				jl->FZ=vect_temp1[j+1];
	    				vect_temp1.pop();
	    				vect_temp1.pop();
	    				continue;
	    			}
	    			if(vect_temp1[j]=="MX"){
	    				jl->MX=vect_temp1[j+1];
	    				vect_temp1.pop();
	    				vect_temp1.pop();
	    				continue;
	    			}
	    			if(vect_temp1[j]=="MY"){
	    				jl->MY=vect_temp1[j+1];
	    				vect_temp1.pop();
	    				vect_temp1.pop();
	    				continue;
	    			}
	    			if(vect_temp1[j]=="MZ"){
	    				jl->MZ=vect_temp1[j+1];
	    				vect_temp1.pop();
	    				vect_temp1.pop();
	    				continue;
	    			}
	    		}
	    	for(int j=0;j<vect_temp1.size();j++){
	    		temp1=temp1+vect_temp1[j];
	    	}
	    	vect_temp1=ToList(temp1);
	    	for(int k=0;j<vect_temp1.size();k++){
	    		for(int j=0;j<joint.size();j++){
                if(joint[j].id==vect_temp1[k]){
                    joint.joinLoad=*jl;
                    jl=new JointLoad;
                    break;
                }
            	}
	    	}
	    	delete jl;
	    }
	    
	}
    					
