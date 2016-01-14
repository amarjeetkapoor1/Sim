CFLAGS=-I/header -L/usr/lib -lmysqlcppconn

Main: main.cpp structure.cpp header/structure.h
	g++  main.cpp structure.cpp -o Main $(CFLAGS)
