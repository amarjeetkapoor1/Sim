# Sim

Structure information model is software used to form database model for 
the the given structure by extracting info from .std file made by 
staad.pro


## Requirement 
	
	g++
	libmysqlcppconn-dev
	make 
	
##Installation 
	

	cd Path/to/This/	
	make all user= Your_sql_username password= Your_sql_password

# Running
	./main.sh Name_of_std_file Name_of_destionation_file
	
#For Documentation-:
	
	cd Path/to/This/
	doxygen Doxyfile
or

	make Doxygen
