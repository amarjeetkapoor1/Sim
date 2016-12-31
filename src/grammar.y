%{
#include <cstdio>
#include <iostream>
#include <vector>
#include "header/structure.h"
#include "header/joint.h"
#include "header/job.h"
#include "header/member.h"

using namespace std;

// stuff from flex that bison needs to know about:
int yylex();
int yyparse();
extern FILE *yyin;
 
void yyerror(const char *s);

class Structure *mainstructure;



%}

%union {
    double dval;
    int ival;
    char *ch;
    class Joint *joint;
    class vectJoint *joints;
    class Job* job;
    class vectmem *vec;
    class Memberlist * member;
}


%token <dval> FLOAT
%token JOINT MEMBER
%token JOB_NAME JOB_CLIENT JOB_NO JOB_REV JOB_PART JOB_REF JOB_COMMENT
%token APPROVED_DATE CHECKER_DATE APPROVED_NAME CHECKER_NAME 
%token ENGINEER_NAME ENGINEER_DATE 
%token <ch> REST
%token UNIT

%type <joint> points
%type <joints> number
%type <joints> joint_coordinates
%type <job> job
%type <str> string
%type <vec> member;
%type <member> Member


%%

structure:
	| structure end
	| UNIT REST structure {mainstructure->unit=std::string($2);  }
	| job structure {mainstructure->job=*$1; } 
	| joint_coordinates structure {mainstructure->job_joints=*$1; }
 	| Member structure { mainstructure->job_members=*$1; }
	;

job: 
	| JOB_NAME string job{$$->name=$2; }
	| JOB_CLIENT string job{ $$->client = $2;}
	| JOB_NO string job{ $$->job_id = $2;}
	| JOB_REV string job{ $$->rev = $2;}
	| JOB_PART string job{ $$->part = $2;}
	| JOB_REF string job{ $$->ref = $2;}
	| JOB_COMMENT string job{ $$->comment = $2;}
	| APPROVED_DATE string job{$$->approved_date=$2; }
	| CHECKER_DATE string job{ $$->checker_date= $2;}
	| APPROVED_NAME string job{ $$->approved_name  = $2;}
	| CHECKER_NAME string job{ $$->CHECKERNAME = $2;}
	| ENGINEER_NAME string job{ $$->engineer_name = $2;}
	| ENGINEER_DATE string job{ $$->date = $2;}
	;

Member:
	| member ';' end Member { 
		Member m;
		while($1->list.size()!=1){
			int i =$1->list.back();
			m.joint_id.push_back(i);
			$1->list.pop_back();
		}
		m.id= $1->list.back();
		$$->list.push_back(m); 
		}
	;

member: 
	| FLOAT member { $$->list.push_back($1); } 

string:
	REST string { $$=$1+$2; }

 
joint_coordinates: 
    | JOINT '\n' number { $$=$3; }
    ;

number:
    |points ';' end number { $$->list.push_back(*$1); }
    ;

points:
    |FLOAT FLOAT FLOAT FLOAT 
	{cout<<$1<<" "<<$2<<" "<<$3<<" "<<$4<<endl;
		Joint *joint = new Joint();  
		joint->id=$1;
    		joint->x=$2; 
		joint->y=$3; 
		joint->z=$4;
		$$=joint; 
	}
    ;
end:
    |'\n' end
    ;

%%

int main(int, char**) {
    // open a file handle to a particular file:
    mainstructure=new Structure();
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
	mainstructure->print();
	

}

void yyerror(const char *s) {
    cout << "EEK, parse error!  Message: " << s << endl;
    // might as well halt now:
    exit(-1);
}
