CFLAGS=-I/header -L/usr/lib -lmysqlcppconn

all: Main

Main: main.cpp structure.o material.o header.o joint.o member.o job.o ConcreteDesign.o
	g++  main.cpp structure.o ConcreteDesign.o header.o job.o joint.o member.o material.o -o Main $(CFLAGS)

structure.o:  
	g++ src/structure.cpp -c 

job.o: 
	g++ src/job.cpp -c 
	
joint.o:
	g++ src/joint.cpp -c 
	
member.o:
	g++ src/member.cpp -c 
	
material.o:
	g++ src/material.cpp -c 

ConcreteDesign.o:
	g++ src/ConcreteDesign.cpp -c
	
header.o:
	g++ src/header.cpp -D USER=$(user) -D PASSWORD=$(password) -c
	
clear:
	rm -r *.o 
	rm Main
