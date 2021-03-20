#built to run on Python 3.6.9 with only standard libraries
#runs on every .java file in a directory and outputs a UML class diagram
#for example:
'''
BMI
____________________________________________
-	name:	String
-	age:	int
-	weight:	double
-	height:	double
+	KILOGRAMS_PER_POUND:	double
+	METERS_PER_INCH:	double
+	INCH_PER_FOOT:	int
____________________________________________
+	BMI(name:String,age:int,weight:double,height:double)
+	BMI(name:String,weight:double,height:double)
+	BMI(name:String,age:int,weight:double,feet:double,inches:double)
+	getBMI():	double
+	getStatus():	String
+	getName():	String
+	getAge():	int
+	getWeight():	double
+	getHeight():	double

'''
#to use, copy this file into the directory with all the .java's you want UML's of
#then run python uml.py


import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]

for f in files:
    if ".java" in f:
        with open(f, 'r') as i:
            temp = f + "_UML.txt"
            with open(temp, "w") as o:
                first = True
                o.write(f[:-5] +"\n")
                o.write("____________________________________________\n")

                data = i.readlines()
                for line in data:
                    out = ""
                    if "public class" in line:
                        continue
                    if "private" in line or "public" in line:
                        pieces = line.strip().split(" ")
                        if "private" in pieces[0]:
                            out = out + "-\t"
                        elif "public" in pieces[0]:
                            out = out = "+\t"
                        
                        #constructor or method
                        if "(" in line and ")" in line and "{" in line:
                            if first:
                                o.write("____________________________________________\n")
                                first = False
                            #constructor
                            if f[:-5] in pieces[1][:-2]:
                                out = out + f[:-5] + "("
                                params = line.split("(")[1].split(")")[0].split(",")
                                for p in params:
                                    p = p.strip()
                                    try:
                                        out = out + p.split(" ")[1] + ":" + p.split(" ")[0] + ", "
                                    except:
                                        continue
                                if "(" not in out[len(out)-1]:
                                    out = out[:-1]
                                out = out + ")"
                                
                            else:
                                line = line.replace(" static", "")
                                pieces = line.strip().split(" ")
                                out = out + pieces[2].split("(")[0] + "("
                                params = line.split("(")[1].split(")")[0].split(",")
                                for p in params:
                                    p = p.strip()
                                    try:
                                        out = out + p.split(" ")[1] + ":" + p.split(" ")[0] + ", "
                                    except:
                                        continue
                                if "(" not in out[len(out)-1]:
                                    out = out[:-1]
                                out = out + "):\t" + pieces[1]
                                
                                
                        #datavalue
                        else:
                            line = line.replace(" static", "")
                            line = line.replace(" final", "")
                            pieces = line.strip().split(" ")
                            out = out + pieces[2] + ":\t" + pieces[1]
                        
                        out = out.replace(";", "")
                        o.write(out + "\n")