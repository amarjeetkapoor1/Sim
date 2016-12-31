/* just like Unix wc */
/* declare tokens */
%x Job
%x Joints



%{
#include<iostream>
//#include"parse.tab.h"
using namespace std;

enum yytokentype {
JOB = 258,
STRING=259,
INT=260,
FLOAT=271

};
%}



%%
["*"]+(.)*"\n" {}
"START JOB INFORMATION" { return JOB;}
"JOB NAME" { return JOB;}
"JOB CLIENT" { return JOB;}
"JOB NO" { return JOB;}
"JOB REV" { return JOB;}
"JOB PART" { return JOB;}
"JOB REF" { return JOB;}
"JOB COMMENT" { return JOB; }
[A-z]+[0-9]* { return STRING;}
[-+]?([0-9]*) {return INT;}
[-+]?([0-9]*)"*"[-+]?([0-9]*) {return multiple;}
[-+]?([0-9]*\.?[0-9]+|[0-9]+\.)([e]?[-+]?([0-9]*))? {return FLOAT;}
"END JOB INFORMATION" { return JOB;}
%%
int main(int argc, char **argv){
int tok;
	if(argc<2){
		return 1;
	}
	yyin = fopen(argv[1], "r");
	while(tok = yylex()) {
    printf("%d", tok);
    }
   

}
