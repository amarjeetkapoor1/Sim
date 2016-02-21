CFLAGS=-I/header -L/usr/lib -lmysqlcppconn

all: Main

Main: main.cpp structure.o header.o 
	g++  main.cpp structure.o header.o job.o -o Main $(CFLAGS)

structure.o: job.o 
	g++ structure.cpp -c 

job.o: header.o 
	g++ job.cpp -c 
header.o: header.cpp
	g++ header.cpp -D USER=$(user) -D PASSWORD=$(password) -c
	
clear:
	rm -r *.o 
	rm Main
