/* just like Unix wc */
%x Job
%{
#include<iostream>
%}
%%
^"*".*"\n"$ {}
"START JOB INFORMATION" {BEGIN Job; }
%%
int main(int argc, char **argv){
int tok;
yylex();
}
