%{
#include <cstdio>
#include <iostream>
using namespace std;
#define YY_DECL extern "C" int yylex()

#include "grammar.tab.h"  // to get the token types that we return

%}

%%
\n  { }
";"   { }
"JOINT COORDINATES" {return JOINT;}
	
[-+]?([0-9]*\.?[0-9]+|[0-9]+\.)([e]?[-+]?([0-9]*))? { yylval.dval = atof(yytext);  return FLOAT; }

.
%%
