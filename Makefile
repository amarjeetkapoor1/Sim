CFLAGS=-I/header -L/usr/lib -lmysqlcppconn

all: Main

Main: main.cpp structure.o header.o 
	g++  main.cpp structure.o header.o -o Main $(CFLAGS)

structure.o: header.o 
	g++ structure.cpp -c 

header.o: header.cpp
	g++ header.cpp -c
	
clear:
	rm -r *.o 
	rm Main
