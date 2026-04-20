#pthon follow indentation ; 

# string

# aboutme = """ I'm  Shamsher  
# education is bscs """;
# print(aboutme);
  
# why need , "" ,' ', """    """, 
# if need to store this type string 
#  about = " I'm shamsher ali "
# if want to go next line but string strore in variable 
about = """
   I'm shamsher ali ,
   my edu i sBSCS
   """ ;

# escape Sequence , charater 
#  used for formating in string like /n ,\t(tab) etc...

# about = "My name is Shamsher \n my  \t education is BSCS ";
# print("about = ",about);
# concatination ;
 
# v1 = " my Country"
# v2="Pakistan";
# final=v1+" "+v2;
# print(final);

#indexing 
# v1="Country";
#  C=0,o=1,u=2,n=3,t=4,r=5,y=6;
# print(v1[2])

#length :: 
# print("the length of V1 = ", len(v1));



# slicing 
# access parts of string
# st[start_inx : ending_idx], ending_index not inclued , exclude 
# v1="Pakistan";
# print(v1[0:3])
# print(v1[:4])
# print(v1[2:])
# print(v1[1:len(v1)])

# fr = "Apple";
# print(fr[-5:-2]);

# string  functions ::
 
v1 = "i am Python Developer Python"
# endswith()
# print(v1.endswith("we"))

# capitalize();
# print(v1.capitalize())

# replace("older_text","newText");

# rt = v1.replace("Python","C++");
# print("the rt is = ",rt);

# find("");
# print(v1.find("Python"))

# count()
about = " am Shamsher ali";
print(about.count("am"));


# Assignment :: 
# WAP to input name and print its length 
#WAP to find occurance of "s' in string andlos how many time ocur

 
#  if else 

nb =1;
# if(nb>0):
#     print("the number is greator ");
# else:
#     print("the number is less");

# #  if  elif else 
# if(nb>1):
#     print("greator than 1")
# elif(nb<1):
#     print (" Less than 1")
# else:
#     print("wrong input")

marks= int(input("enter the marks :"))

if(marks>90):
    print("the Grade is = A");
elif(marks>70):
    print("the Grade is = B");
elif(marks>60):
    print("the Grade is = C");
else:
    print("fail");

# nb/2==0 : even  / odd ;