from __future__ import print_function

import DCLib
import requests

# global values
listDefault = [
				"?\t\t- commands help",
				"show\t\t- show configurations",
				"create\t\t- creates new instances",
				"modify\t\t- modify already created instances",
				"del\t\t- delete the created instances",
				]

listShow = [
			"show ipv4 <interface name>",
			"show callProfiles",
			"show callProfile <id>",
			"\nshow callLegProfiles",
			"show callLegProfile <id>",
			"show callLegProfile <id> usage\t- works only when there is a callLeg available",
			"\nshow spaces",
			"show space <id>",
			"show space <id> accessMethods",
			"show space <id> accessMethod <id>",
			"show space <id> spaceUsers",
			"show space <id> spaceUser <id>",
			"show space <id> diagnostics",
			"show space <id> meetingEntryDetail",
			]

listCreate = [
			"create ipv4 <interface name> <ip address/mask> <gateway>",
			"create callProfile",
			"create callLegProfile",
			"create space",
			"create space <id> accessMethod",
			"create space <id> spaceUser"
			]

listDel = [
			"del callProfile <id>",
			"del callLegProfile <id>",
			"del space <id>",
			"del space <id> accessMethod <id>",
			"del space <id> spaceUser <id>",
		]

listModify = [
				"CallProfiles configures in-call experience for SIP (including Lync) calls",
				"\tmodify callProfile <id> participantLimit <number>",
				"\tmodify callProfile <id> messageBoardEnabled <true/false>",
				"\tmodify callProfile <id> locked <true/false>",
				"\tmodify callProfile <id> recordingMode <disabled/manual/automatic>",
				"\tmodify callProfile <id> streamingMode <disabled/manual/automatic>",
				"\tmodify callProfile <id> passcodeMode <required/timeout>",
				"\tmodify callProfile <id> passcodeTimeout <in seconds>",

				"\nCallLegProfile defines a set of in-call behaviors. coSpace, coSpaceUser, accessMethod,\n\
and tenant objects can optionally have a callLegProfile association if you want\n\
to tweak the following parameters",
				"\tmodify callLegProfile <id> needsActivation <true/false>",
				"\tmodify callLegProfile <id> defaultLayout <allEqual/ speakerOnly/ telepresence/ stacked/\n\
		allEqualQuarters/ allEqualNinths/ allEqualSixteenths/ allEqualTwentyFifths/\n\
		onePlusFive/ onePlusSeven/ onePlusNine/ automatic/ onePlusN>",
				"\tmodify callLegProfile <id> changeLayoutAllowed <true/false>",
				"\tmodify callLegProfile <id> participantLabels <true/false>",
				"\tmodify callLegProfile <id> presentationDisplayMode <dualStream/ singleStream>",
				"\tmodify callLegProfile <id> presentationContributionAllowed <true/false>",
				"\tmodify callLegProfile <id> allowAllPresentationContributionAllowed <true/false>",
				"\tmodify callLegProfile <id> presentationViewingAllowed <true/false>",
				"\tmodify callLegProfile <id> endCallAllowed <true/false>",
				"\tmodify callLegProfile <id> disconnectOthersAllowed <true/false>",
				"\tmodify callLegProfile <id> muteOthersAllowed <true/false>",
				"\tmodify callLegProfile <id> changeJoinAudioMuteOverrideAllowed <true/false>",
				"\tmodify callLegProfile <id> videoMuteOthersAllowed <true/false>",
				"\tmodify callLegProfile <id> muteSelfAllowed <true/false>",
				"\tmodify callLegProfile <id> allowAllMuteSelfAllowed <true/false>",
				"\tmodify callLegProfile <id> videoMuteSelfAllowed <true/false>",
				"\tmodify callLegProfile <id> joinToneParticipantThreshold <number>",
				"\tmodify callLegProfile <id> leaveToneParticipantThreshold <number>",
				"\tmodify callLegProfile <id> videoMode <auto/ disabled>",
				"\tmodify callLegProfile <id> rxAudioMute <true/false>",
				"\tmodify callLegProfile <id> txAudioMute <true/false>",
				"\tmodify callLegProfile <id> rxVideoMute <true/false>",
				"\tmodify callLegProfile <id> txVideoMute <true/false>",
				"\tmodify callLegProfile <id> sipMediaEncryption <optional/ required/ prohibited>",
				"\tmodify callLegProfile <id> audioPacketSizeMs <number>",
				"\tmodify callLegProfile <id> deactivationMode <deactivate/ disconnect/ remainActivated>",
				"\tmodify callLegProfile <id> deactivationModeTime <number>",
				"\tmodify callLegProfile <id> telepresenceCallsAllowed <true/false>",
				"\tmodify callLegProfile <id> sipPresentationChannelEnabled <true/false>",
				"\tmodify callLegProfile <id> bfcpMode <serverOnly/ serverAndClient>",
				"\tmodify callLegProfile <id> callLockAllowed <true/false>",
				"\tmodify callLegProfile <id> recordingControlAllowed <true/false>",
				"\tmodify callLegProfile <id> streamingControlAllowed <true/false>",
				"\tmodify callLegProfile <id> name <string>",
				"\tmodify callLegProfile <id> maxCallDurationTime <seconds>",

				"\nSpaces are the virtual meeting rooms hosting ad-hoc, static and scheduled conferences",
				"\tmodify space <id> name <string>",
				"\tmodify space <id> uri <e.g. abhijit.dey@cisco.com>",
				"\tmodify space <id> secondaryUri <e.g. abhijit.dey2@cisco.com>",
				"\tmodify space <id> callId <number>",
				"\tmodify space <id> cdrTag <string>",
				"\tmodify space <id> passcode <string>",
				"\tmodify space <id> defaultLayout <automatic/ allEqual/ allEqualQuarters/ allEqualNinths/\n\
		allEqualSixteenths/ allEqualTwentyFifths/ speakerOnly/ telepresence/\n\
		stacked/ onePlusFive/ onePlusSeven/ onePlusNine/ onePlusN>",
				"\tmodify space <id> tenant <id>",
				"\tmodify space <id> callLegProfile <id>",
				"\tmodify space <id> callProfile <id>",
				"\tmodify space <id> callBrandingProfile <id>",
				"\tmodify space <id> requireCallId <true/ false>",
				"\tmodify space <id> secret <string>",
				"\tmodify space <id> regenerateSecret <true/ false>",
				"\tmodify space <id> nonMemberAccess <true/ false>",
				"\tmodify space <id> ownerJid <string>",
				"\tmodify space <id> streamUrl <e.g. http://allHands.cisco.com:8132>",
				"\tmodify space <id> ownerAdGuid <string>",
				"\tmodify space <id> messages <string>",

				"\nSpace accessMethod define URI / passcode / callID combinations that can be used to\n\
access a coSpace",
				"\tmodify space <id> accessMethod <id> uri <id>",
				"\tmodify space <id> accessMethod <id> callID <id>",
				"\tmodify space <id> accessMethod <id> passcode <string>",
				"\tmodify space <id> accessMethod <id> callLegProfile <id>",
				"\tmodify space <id> accessMethod <id> secret <string>",
				"\tmodify space <id> accessMethod <id> regenerateSecret <true/ false>",
				"\tmodify space <id> accessMethod <id> scope <public/ private>",

				"\nSpaceuser are the virtual meeting rooms hosting ad-hoc, static and scheduled conferences",
				"\tmodify spaceUser <id> userJid <id>\t\t- This userJid becomes part of this space user",
				"\tmodify spaceUser <id> callLegProfile <id>\t- Configs for the callLegProfile becomes part\n\
							  of this space user",
				"\tmodify spaceUser <id> canDestroy <true/ false>",
				"\tmodify spaceUser <id> canAddRemoveMember <true/ false>",
				"\tmodify spaceUser <id> canChangeName <true/ false>",
				"\tmodify spaceUser <id> canChangeUri <true/ false>",
				"\tmodify spaceUser <id> canChangeCallId <true/ false>",
				"\tmodify spaceUser <id> canChangePasscode <true/ false>",
				"\tmodify spaceUser <id> canPostMessage <true/ false>",
				"\tmodify spaceUser <id> canRemoveSelf <true/ false>",
				"\tmodify spaceUser <id> canDeleteAllMessages <true/ false>",
				]



# the code begins here

cmsIp = raw_input("CMS IP Address: ")
cmsPort = raw_input("CMS Port Number for https: ")
cmsLogin = raw_input("CMS Username: ")
cmsPassword = raw_input("CMS Password: ")

while 1:
	command = raw_input("cms>")
	if command == "quit" or command == "q" or command == "Q":
		print("\nThanks for using my code - Abhijit Dey,\nPlease give feedback at (abdey@cisco.com)\n")
		break

	elif command == "?":
		DCLib.showApiList(listDefault)

	elif command == "show ?":
		DCLib.showApiList(listShow)
	elif DCLib.firstWordOfCommand(command) == "show":
		commandList = DCLib.commandToList(command)
		if commandList[1]=="ipv4":
			DCLib.execShowMmp(command, cmsIp, cmsLogin, cmsPassword)
		elif commandList[1]!="ipv4":
			DCLib.execShowApi(command, cmsIp, cmsPort, cmsLogin, cmsPassword)

	elif command == "create ?":
		DCLib.showApiList(listCreate)
	elif DCLib.firstWordOfCommand(command) == "create":
		commandList = DCLib.commandToList(command)
		if commandList[1]=="ipv4":
			DCLib.execCreateMmp(command, cmsIp, cmsLogin, cmsPassword)
		elif commandList[1]!="ipv4":
			DCLib.execPostApi(command, cmsIp, cmsPort, cmsLogin, cmsPassword)

	elif command == "del ?":
		DCLib.showApiList(listDel)
	elif DCLib.firstWordOfCommand(command) == "del":
		commandList = DCLib.commandToList(command)
		if commandList[1]!="ipv4":
			DCLib.execDelApi(command, cmsIp, cmsPort, cmsLogin, cmsPassword)

	elif command == "modify ?":
		DCLib.showApiList(listModify)
	elif DCLib.firstWordOfCommand(command) == "modify":
		commandList = DCLib.commandToList(command)
		if commandList[1]!="ipv4":
			DCLib.execPutApi(command, cmsIp, cmsPort, cmsLogin, cmsPassword)



	
