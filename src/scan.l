%{
#include <cstdio>
#include <iostream>
using namespace std;

std::string data;
#include "grammar.tab.h"  // to get the token types that we return

%}
%x Job rest

%%

"START JOB INFORMATION" {BEGIN(Job);}
<Job>{
"JOB NAME" { BEGIN(rest); return  JOB_NAME;}
"JOB CLIENT" { BEGIN(rest); return  JOB_CLIENT; }
"JOB NO" { BEGIN(rest); return  JOB_NO; }
"JOB REV" { BEGIN(rest); return  JOB_REV; }
"JOB PART" { BEGIN(rest); return  JOB_PART; }
"JOB REF" { BEGIN(rest); return  JOB_REF; }
"JOB COMMENT" { BEGIN(rest); return  JOB_COMMENT;  }
"APPROVED DATE" { BEGIN(rest); return  APPROVED_DATE;  }
"CHECKER DATE" { BEGIN(rest); return  CHECKER_DATE;  }
"APPROVED NAME" { BEGIN(rest); return  APPROVED_NAME;   }
"CHECKER NAME" { BEGIN(rest); return  CHECKER_NAME;  }
"ENGINEER NAME" { BEGIN(rest); return  ENGINEER_NAME;   }
"ENGINEER DATE" { BEGIN(rest); return ENGINEER_DATE;   }
"END JOB INFORMATION" { BEGIN(INITIAL); }
}

<rest>{

\n {  yylval.ch=strdup(data.c_str()); data.clear(); BEGIN(Job); return REST;  } 
^\n { cout<<yytext; data+=yytext; }
}

"UNIT" { BEGIN(rest); cout<<"asas"; BEGIN(INITIAL); return UNIT; }
"MEMBER INCIDENCES" {  return MEMBER;}
\n  { return yytext[0]; }
";"   { return yytext[0]; }
"JOINT COORDINATES" {  return JOINT;}
	
[-+]?([0-9]*\.?[0-9]+|[0-9]+\.)([e]?[-+]?([0-9]*))? { yylval.dval = atof(yytext);  return FLOAT; }

.
%%
