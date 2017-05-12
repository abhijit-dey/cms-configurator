
import requests, time

# some predined command outputs
actualCommand2 = "\
IPv4 configuration: \n"\
    "\taddress         10.106.170.214\n"\
    "\tdefault         true\n"\
    "\tdhcp            false\n"\
    "\tduplex          full\n"\
    "\tenabled         true\n"\
    "\tgateway         10.106.170.129\n"\
    "\tmacaddress      00:50:56:AE:1F:71\n"\
    "\tprefixlen       25\n"\
    "\tspeed           1000\n"\
"IPv4 observed values\n"\
"Addresses:\n"\
"10.106.170.214/25\n"\
"Routes:\n"\
    "\tsource          destination     gateway         global\n"\
    "\t0.0.0.0         10.106.170.214  0.0.0.0         false\n"\
    "\t0.0.0.0         10.106.170.128  0.0.0.0         false\n"\
    "\t0.0.0.0         10.106.170.128  0.0.0.0         false\n"\
    "\t0.0.0.0         10.106.170.255  0.0.0.0         false\n"\
    "\t0.0.0.0         0.0.0.0         10.106.170.129  true"


# function to display the list of available API commands
def xmlOutputImprove(xmlOutput):
	xmlList = []

	tempList = xmlOutput.split("<")

	for i in xrange(1,len(tempList)):
		a = tempList[i][0]
		if a != "?" and a != "/":
			b = tempList[i]
			b = b.replace(">","-")
			xmlList.append(b)

	return xmlList
	#for i in xrange(1,len(xmlList)):
	#	print(xmlList[i])

def showApiList(list1):
	listlen = len(list1)

	print("List of commands:\n\nUsage:\n")
	for a in range(0, listlen):
		print(list1[a])
	print("")

def commandToList(command):
	commandList = command.split(' ')
	return commandList

def firstWordOfCommand(command):
	command = command.split(' ')
	return command[0]

def getApiOnCms(url, cmsLogin, cmsPassword):
    try:
        response = requests.get(
            url=url,
            headers={
                "Authorization": "Basic YXBpOmFwaQ==",
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            },
            auth=(cmsLogin, cmsPassword),
            verify=False
        )
        output = xmlOutputImprove(response.content)
        print ("\nAPI is - \n"+url+"\n")
        for i in xrange(0,len(output)):
        	print(output[i])
    except requests.exceptions.RequestException:
        print("HTTPs Request failed")

def postApiOnCms(url, cmsLogin, cmsPassword):
    try:
        response = requests.post(
            url=url,
            headers={
                "Authorization": "Basic YXBpOmFwaQ==",
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            },
            auth=(cmsLogin, cmsPassword),
            verify=False
        )
        print("\nAPI is - \n"+url+"\n")
        print(response.status_code)
        print("Created")
    except requests.exceptions.RequestException:
        print("HTTPs Request failed")

def delApiOnCms(url, cmsLogin, cmsPassword):
    try:
        response = requests.delete(
            url=url,
            headers={
                "Authorization": "Basic YXBpOmFwaQ==",
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            },
            auth=(cmsLogin, cmsPassword),
            verify=False
        )
        print ("\nAPI is - \n"+url+"\n")
        print(response.status_code)
        print("Deleted")
    except requests.exceptions.RequestException:
        print("HTTPs Request failed")

def putApiOnCms(url, cmsLogin, cmsPassword, field):
    try:
        response = requests.put(
            url=url,
            headers={
                "Authorization": "Basic YXBpOmFwaQ==",
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            },
            auth=(cmsLogin, cmsPassword),
            verify=False,
            data=field
        )
        print("\nAPI is - \n"+url)
        print(field)
        code = response.status_code
        if code=="200":
        	print("Modified")
        else:
        	print("Command successfully sent")
    except requests.exceptions.RequestException:
        print("HTTPs Request failed")

def execShowMmp(command, cmsIp, cmsLogin, cmsPassword):
	commandList = command.split(' ')
#	cmsMmp = ssh into MMP interface and return handler as 
	if commandList[0]=="show" and commandList[1]=="ipv4":
		actualCommand = commandList[1] + " " + commandList[2]
#		cmsMmp.execute(actualCommand)
		print(actualCommand2)
#	cmsMmpShowResult = cmsMmp.execute(command)
#	return cmsMmpShowResult

def execCreateMmp(command, cmsIp, cmsLogin, cmsPassword):
	commandList = command.split(' ')
#	cmsMmp = ssh into MMP interface and return handler as 
	if commandList[0]=="create" and commandList[1]=="ipv4":
					#"create ipv4 <interface name> <ip address/mask> <gateway>",
		actualCommand = commandList[1] + " " + commandList[2] + " add " + commandList[3] + " " + commandList[4]
#		cmsMmp.execute(actualCommand)
		print(actualCommand)
#	cmsMmpShowResult = cmsMmp.execute(command)
#	return cmsMmpShowResult

def execShowApi(command, cmsIp, cmsPort, cmsLogin, cmsPassword):
	commandList = command.split(' ')
	commandListLen = len(commandList)
	if commandList[1] == "callProfiles":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/" + commandList[1]
		getApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[1] == "callProfile":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/" + "callProfiles" + "/" + commandList[2]
		getApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[1] == "callLegProfiles":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/" + commandList[1]
		getApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[1] == "callLegProfile" and commandListLen == 3:
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/" + "callLegProfiles" + "/" + commandList[2]
		getApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[1] == "callLegProfile" and commandList[3] == usage:
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/" + "callLegProfiles" + "/" + commandList[2]\
+ "/usage"
		getApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[1] == "spaces":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/" + "coSpaces"
		getApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[1] == "space" and commandListLen == 3:
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/" + "coSpaces" + "/" + commandList[2]
		getApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[3] == "accessMethods" and commandListLen == 4:
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/" + "coSpaces" + "/" + commandList[2]\
+ "/" + commandList[3]
		getApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[3] == "accessMethod" and commandListLen == 5:
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/" + "coSpaces" + "/" + commandList[2]\
+ "/" + "accessMethods" + "/" + commandList[4]
		getApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[3] == "spaceUsers":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/" + "coSpaces" + "/" + commandList[2]\
+ "/" + "coSpaceusers"
		getApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[3] == "spaceUser" and commandListLen == 5:
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/" + "coSpaces" + "/" + commandList[2]\
+ "/" + "coSpaceUsers"+ "/" + commandList[4]
		getApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[3] == "diagnostics":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/" + "coSpaces" + "/" + commandList[2]\
+ "/" + commandList[3]
		getApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[3] == "meetingEntryDetail":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/" + "coSpaces" + "/" + commandList[2]\
+ "/" + commandList[3]
		getApiOnCms(actualCommand, cmsLogin, cmsPassword)

def execPostApi(command, cmsIp, cmsPort, cmsLogin, cmsPassword):
	commandList = command.split(' ')
	commandListLen = len(commandList)
	if commandList[1] == "callProfile":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/callProfiles"
		postApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[1] == "callLegProfile":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/callLegProfiles"
		postApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[1] == "space" and commandListLen == 2:
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/coSpaces"
		postApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[3] == "accessMethod":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/coSpaces/" + commandList[2] + "/accessMethods"
		postApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[3] == "spaceUser":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/coSpaces/" + commandList[2] + "/coSpaceUsers"
		postApiOnCms(actualCommand, cmsLogin, cmsPassword)

def execDelApi(command, cmsIp, cmsPort, cmsLogin, cmsPassword):
	commandList = command.split(' ')
	commandListLen = len(commandList)
	if commandList[1] == "callProfile":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/callProfiles/" + commandList[2]
		delApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[1] == "callLegProfile":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/callLegProfiles/" + commandList[2]
		delApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[1] == "space" and commandListLen==3:
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/coSpaces/" + commandList[2]
		delApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[1] == "space" and commandList[3] == "accessMethod":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/coSpaces/" + commandList[2] + "/accessMethods/" + commandList[4]
		delApiOnCms(actualCommand, cmsLogin, cmsPassword)
	elif commandList[1] == "space" and commandList[3] == "spaceUser":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/coSpaces/" + commandList[2] + "/coSpaceUser/" + commandList[4]
		delApiOnCms(actualCommand, cmsLogin, cmsPassword)

def execPutApi(command, cmsIp, cmsPort, cmsLogin, cmsPassword):
	commandList = command.split(' ')
	commandListLen = len(commandList)
	if commandList[1] == "callProfile":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/callProfiles/" + commandList[2]
		field = {commandList[3]: commandList[4]}
		putApiOnCms(actualCommand, cmsLogin, cmsPassword, field)
	elif commandList[1] == "callLegProfile":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/callLegProfiles/" + commandList[2]
		field = {commandList[3]: commandList[4]}
		putApiOnCms(actualCommand, cmsLogin, cmsPassword, field)
	elif commandList[3] == "accessMethod":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/coSpaces/" + commandList[2] + "/accessMethods/" + commandList[4]
		field = {commandList[5]: commandList[6]}
		putApiOnCms(actualCommand, cmsLogin, cmsPassword, field)
	elif commandList[1] == "space":
		actualCommand = "https://" + cmsIp + ":" + cmsPort + "/api/v1/coSpaces/" + commandList[2]
		field = {commandList[3]: commandList[4]}
		putApiOnCms(actualCommand, cmsLogin, cmsPassword, field)







