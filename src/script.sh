bison -dv grammar.y
flex scan.l
g++ grammar.tab.c lex.yy.c ../structure.o ../ConcreteDesign.o ../header.o ../job.o ../joint.o ../member.o ../material.o  -o main -lfl -I/header -L/usr/lib -lmysqlcppconn	
