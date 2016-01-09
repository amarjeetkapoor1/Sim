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
		x=x+temps[0]+","+temps[1]+','+temps[2]+','+temps[3]+'\n';
		file>>temps[0];
		file>>temps[1];
		file>>temps[2];
		file>>temps[3];
	}while(temps[0]!="MEMBER");

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

