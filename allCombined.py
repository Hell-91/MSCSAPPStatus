import mechanize 
import sys

def getResult(universityName,url,userName,password):
	logLevel=0 #by default no log
	if(len(sys.argv)>1):
		logLevel=int(sys.argv[1])

	b = mechanize.Browser()
	b.set_handle_robots(False)
	
	r1 = b.open(url)

	if(universityName=="Purdue"):
		b.select_form(name="frmApplicantConnectLogin")
		b["UserID"]=userName
		b["Password"]=password
	elif(universityName=="NEU"):
		b.select_form(name="Form1")
		b["txtUserName"]=userName
		b["txtPassword"]=password	
	elif(universityName=="ASU" or universityName=="TAMU"):
		b.select_form(nr=0)
		b["username"]=userName
		b["password"]=password
	elif(universityName=="SUNYSB"):
		b.select_form(nr=0)
		b["UserID"]=userName
		b["Password"]=password
	elif(universityName=="vtech"):
		b.select_form(name="loginForm")
		b["txtUserID"]=userName
		b["txtPassword"]=password
	elif(universityName=="TAMU"):
		result= s[s.find('class="highlight">')+18:s.find(" </span>\r\n")-3]
	elif(universityName=="UCSD"):
		b.select_form(nr=1)
		b["aemail"]=userName
		b["apass"]=password
	elif(universityName=="USC"):
		b.select_form(nr=0)
		b["UserID"]=userName
		b["Password"]=password

	if(logLevel>=1):
		print universityName,"login in progress..."
	r2 = b.submit()

	if(logLevel>=1):
		print "logged in successfully..."
	
	s=r2.read()

	if(logLevel==2):
		name1=''.join((universityName,'1.html'))
		name2=''.join((universityName,'2.html'))

		Html_file= open(name1,"w")
		Html_file.write(r1.read())
		Html_file.close()

		Html_file= open(name2,"w")
		Html_file.write(r2.read())
		Html_file.close()



	result="failed to get result."
	
	if(universityName=="Purdue"):
		result=s[s.find("<li><h4>")+1:s.find("</h4></li>")]
		result=result[7:]
	elif(universityName=="ASU"):
		result=s[s.find('app-status">')+12:s.find('app-status">')+21]
	elif(universityName=="SUNYSB"):
		result= s[s.find("Status")+1:s.find(" <img")]
		result=result[7:]
	elif(universityName=="vtech"):
		result= s[s.find('tableBottomBorder">')+1:s.find('<br><div class="info">')]
		result=result[-9:]
	elif(universityName=="USC"):
		result= s[s.find("Status")+1:s.find(" <img")]
		result=result[7:]
	elif(universityName=="NEU"):
		processNEUResult(result)
	elif(universityName=="TAMU"):
		result= s[s.find('class="highlight">')+18:s.find(" </span>\r\n")-3]
	elif(universityName=="UCSD"):
		result= s[s.find('<span class="value"><span class="Good">')+1:s.find("</span></span>")]
		result=result[38:]
		
	print universityName,"Status :",result
	print "----x----"

	
def processNEUResult(result) :
	if not "<span class=\"green\"> Application Submitted</span>" in result:
		print "Application Submitted: False"
	else:
		print "Applicaation Submitted: True"
		
	if not "<span class=\"green\"> App Materials Received</span>" in result:
		print "Application Materials Received: False"
	else:
		print "Application Materials Received: True"
	
	if not "<span class=\"green\"> My Decision Is Ready</span>" in result:
		print "Decision Ready: False"
	else:
		print "Decision Ready: True"
	

# Fill details of the universities of which you want to check status. Keep the rest as it is. 

purdueUserName=""
purduePass=""

asuUserName=""
asuPass=""

sunySBUserName=""
sunySBPass=""

vtechUserName=""
vtechPass=""

neuUserName=""
neuPass=""

tamuUserName=""
tamuPass=""

ucsdUserName=""
ucsdPass=""

uscUserName=""
uscPass=""

if(len(purdueUserName)>0):
	getResult("Purdue","https://app.applyyourself.com/AYApplicantLogin/fl_ApplicantConnectLogin.asp?id=purduegrad",purdueUserName,purduePass) 

if(len(asuUserName)>0):
	getResult("ASU","https://webapp4.asu.edu/myasu/",asuUserName,asuPass) 

if(len(sunySBUserName)>0):
	getResult("SUNYSB","https://app.applyyourself.com/ayapplicantlogin/fl_ApplicantLogin.asp?ID=sunysb-gs#tab2",sunySBUserName,sunySBPass)

if(len(vtechUserName)>0):
	getResult("vtech","https://gradapp.stl.vt.edu/pages/login.php",vtechUserName,vtechPass)

if(len(neuUserName)>0):
	getResult("NEU","https://neugrad.askadmissions.net/vip/Default.aspx",neuUserName,neuPass)

if(len(tamuUserName)>0):
	getResult("TAMU","https://cas.tamu.edu/cas/login?service=https://applicant.tamu.edu/Account/Login",tamuUserName,tamuPass)

if(len(ucsdUserName)>0):
	getResult("UCSD","https://gradapply.ucsd.edu/account/index.php?node=d56b699830e77ba53855679cb1d252da",ucsdUserName,ucsdPass)

if(len(uscUserName)>0):
        getResult("USC","https://app.applyyourself.com/AYApplicantLogin/fl_ApplicantLogin.asp?id=usc-grad",uscUserName,uscPass)
