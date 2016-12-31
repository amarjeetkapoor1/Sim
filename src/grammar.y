%{
#include <cstdio>
#include <iostream>
#include <vector>
#include "header/structure.h"
#include "header/joint.h"

using namespace std;

// stuff from flex that bison needs to know about:
extern "C" int yylex();
extern "C" int yyparse();
extern "C" FILE *yyin;
 
void yyerror(const char *s);



%}

%union {
    double dval;
    int ival;
    class Joint *joint;
    class vectJoint *joints;
    class Structure *mainStructure;
}


%token <dval> FLOAT
%token JOINT

%type <joint> points
%type <joints> number
%type <joints> joint_coordinates
%type <mainStructure> structure

%%

structure: 
	| joint_coordinates structure { $$->job_joints=*$1; };
 	/* member rule */

joint_coordinates: 
    |JOINT '\n' number { $$=$3; }
    ;
number:
    |points ';' end number { $$->list.push_back(*$1); }
    ;

points:
    |FLOAT FLOAT FLOAT FLOAT 
	{cout<<$1<<" "<<$2<<" "<<$3<<" "<<$4<<endl;
		Joint *joint = (Joint *) malloc(sizeof(Joint));  
		joint->id=$1;
    		joint->x=$2; 
		joint->y=$3; 
		joint->z=$4;
		$$=joint; 
	}
    ;
end:
    |"\n" end
    ;

%%

int main(int, char**) {
    // open a file handle to a particular file:
    FILE *myfile = fopen("a.std", "r");
    // make sure it is valid:    int id;
    double x, y, z;
    if (!myfile) {
        cout << "I can't open a.snazzle.file!" << endl;
        return -1;
    }
    // set flex to read from it instead of defaulting to STDIN:
    yyin = myfile;
  
    // parse through the input until there is no more:
    do {
        yyparse();
    } while (!feof(yyin));
}

void yyerror(const char *s) {
    cout << "EEK, parse error!  Message: " << s << endl;
    // might as well halt now:
    exit(-1);
}
