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
	make user= Your_sql_username password= Your_sql_password
	mysql -u Your_sql_username -p Sim <Sim.sql 
	
# Running
	./main.sh Name_of_std_file Name_of_destionation_file
	
#For Documentation-:
	cd Path/to/This/
	doxygen Doxyfile
