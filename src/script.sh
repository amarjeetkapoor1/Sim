flex scan.l
bison -d grammar.y
g++ grammar.tab.c lex.yy.c -lfl
