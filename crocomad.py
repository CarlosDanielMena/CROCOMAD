#-*- coding: utf-8 -*- 
########################################################################
#crocomad.py

#Subjet   : Cross-Correlation Matching Distance (crocomad)
#Author   : Carlos Daniel Hernández Mena
#Date     : October 1st, 2021
#Location : Garðastræti 6, 101 Reykjavík, Iceland.

#Usage:

#	$ python3 crocomad.py

########################################################################
#This function performs a cross-correlation between
#two strings. The longest is the reference and it is fixed. 

#   comes
#kone    
# kone   
#  kone  
#   kone 
#    kone
#     kone
#       kone

#Then, the maximun number of character-matches is counted.
#In this example:

#   comes   * This is the reference becuase it is the longest word.
#   kone

#This is the aligment with the maximum number of character-matches,
#which are: "o" and "e". Thus, 2 of the 5 characters of the reference match.

#The las step is the normalization:

# crocomad = 1 - ( maximum-number-of-character-matches / reference-lenght )

# crocomad = 1 - ( 2 / 5 )

# crocomad = 1 - ( 0.4 )

# crocomad = 0.6

#This function goes from 0 to 1.
#A value of 0 means that the input strings are the same
#A value of 1 means no character-matches found.

########################################################################
#Function Definition

def crocomad(string_in1,string_in2):
	#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
	#Function :  Cross-Correlation Matching Distance (crocomad)
	#Author   :  Carlos Daniel Hernández Mena
	#Date     :  October 1st, 2021
	#Location :  Garðastræti 6, 101 Reykjavík, Iceland.
	#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
	#Setting up input values	
	#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
	#The longest string will be the reference and the other will
	#be the hypothesis
	if len(string_in1) >= len(string_in2):
		REF=string_in1
		HYP=string_in2
	else:
		REF=string_in2
		HYP=string_in1
	#ENDIF	
	#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
	#Internal Functions
	#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
	#The function step_fwd() shifts the input list one place to
	#the right.
	def step_fwd(lista_in):
		len_lista_in=len(lista_in)
		lista_out=["x"]
		for i in range(0,len_lista_in-1):
			lista_out.append(lista_in[i])
		#ENDFOR
		return lista_out
	#ENDDEF
	#--------------------------------------------------------------#
	#The function extract_indexes() provides two list containing 
	#indexes corresponding to the current cross-correlation step.
	def extract_indexes(list_ref_in,list_hyp_in):
		list_ref_out=[]
		list_hyp_out=[]
		for i in range(0,len(list_ref_in)):
			if list_ref_in[i]!="x" and list_hyp_in[i]!="x":
				list_ref_out.append(list_ref_in[i])
				list_hyp_out.append(list_hyp_in[i])
			#ENDIF
		#ENDFOR
		return [list_ref_out,list_hyp_out]
	#ENDDEF
	#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
	#The algorithm begins here.
	#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
	#Calculating some relevant lenghts.
	ref_len=len(REF)
	hyp_len=len(HYP)
	vector_len=ref_len+2*hyp_len-2	
	#--------------------------------------------------------------#
	#Initialize the reference
	lista_ref=[]
	for i in range(0,hyp_len-1):
		lista_ref.append("x")
	#ENDFOR
	for i in range(0,ref_len):
		lista_ref.append(i)
	#ENDFOR
	for i in range(0,hyp_len-1):
		lista_ref.append("x")
	#ENDFOR
	#--------------------------------------------------------------#
	#Initialize the hypotesis
	lista_hyp=[]
	for j in range(0,vector_len):
		if j < hyp_len:
			lista_hyp.append(j)
		else:
			lista_hyp.append("x")
		#ENDDEF
	#ENDFOR
	#--------------------------------------------------------------#
	#Performing the cross-correlation.	
	#--------------------------------------------------------------#
	#This external for performs the whole cross-correlation
	#between the reference and the hypothesis.
	max_num_matches_found=0
	for k in range(0, (len(REF)+len(HYP)-1)):
		#Extracting the indexes corresponding to the current
		#cross-correlation step.
		indexes_ref, indexes_hyp = extract_indexes(lista_ref,lista_hyp)
		#These strings will contain just the portion of the
		#corresponding input string which specified by the
		#indexes extracted above.
		string_ref=[]
		string_hyp=[]
		#Extracting just the portion of the string indicated
		#by the indexes calculated above and counting the
		#number of character-matches.
		num_matches=0
		for m in range(0,len(indexes_ref)):
			index_ref=indexes_ref[m]
			#string_ref.append(REF[index_ref])
			index_hyp=indexes_hyp[m]
			#string_hyp.append(HYP[index_hyp])
			if REF[index_ref]==HYP[index_hyp]:
				num_matches=num_matches+1
			#ENDIF
		#ENDDEF
		#If the number of matches is greater than the one
		#found before, store it.
		if num_matches>max_num_matches_found:
			max_num_matches_found=num_matches
		#ENDIF		
		#Performing the next cross-correlation step.
		lista_hyp=step_fwd(lista_hyp)
	#ENDFOR	
	#Normalizing with respect to the reference length
	#(which is the longest of the two input strings)
	crocomad=1.0-(max_num_matches_found/ref_len)
	#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
	return crocomad
#ENDDEF

########################################################################
#Function Call
distance=crocomad("comes","kone")
print(distance)
########################################################################

