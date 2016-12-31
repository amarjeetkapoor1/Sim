
Rep:INT "*" FLOAT{
	while($1){
		std::cout<<FLOAT;
	}
	}

List: List "-" "\n" List
List :	INT List
	| INT "TO" INT List
	| INT "TO" INT "BY" INT list

Units: 
	length-unit 
	|force-unit 
	| force-unit length-unit
	| length-unit force-unit 
	 

length-unit :
	INCHES 
	| FEET 
	| FT 
	| FO 
	| CM 
	| METER 
	| MMS
	| DME 
	| KM 
	
force-unit : 
		KIP 
		| POU
		| POUND 
		| KG 
		| MTO
		|MTON 
		| NEW
		| NEWTON 
		| KNS 
		| MNS
		| DNS 


JOINT:
	JOINT  COORDINATES System band-spec
	JOI  COO System band-spec

Corrdinate: x y z
	


System : 
	| CYLINDRICAL 
	| CYLINDRICAL  REVERSE 

band-spec: 
	| NOREDUCE BAND
	| NO BAND


(NOCHECK)
band-spec
i 1 , x 1 , y 1 , z 1 , ( i 2 , x 2 , y 2 , z 2 , i 3 )


