#include "structure.h"

structure::structure(fstream &file){
	char ch;
	int a;
	string temp,temps[4];
	while(temp!="INPUT"){
		file>>temp;
	}
    file>>temp;
	file>>widht;
	file>>temp;
	file>>temp;
	do{
		units=units+temp+",";
		file>>temp;
	}
	while(temp!="JOINT");
	units=units+'\n';
	file>>temp;
	/*while(temp.find("JOINTCOORDINATES")){
		getline(file,temp);
	}*/
	do{
		x=x+jo.name+","+jo.x+','+jo.y+','+jo.z+'\n';
		file>>jo.name;
		file>>jo.x;
		file>>jo.y;
		file>>jo.z;
	}while(jo.name!="MEMBER");

}

void structure::print(){
	//job.print();
	cout<<"units,"<<units<<"\n";
	cout<<"widht,"<<widht<<"\n";
	cout<<x;
	/*joint.print();
	mI.print();
	gr.print();
	m.print();
	*/
}

