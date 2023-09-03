import re
import regex
from phrases import phrases as P
import datetime
import hashlib
import base64

time_interval_pattern = re.compile(r"^(?:(?:([01][0-9]|2[0-3]|[1-9]):)([0-5]?[0-9])) ?- ?(?:(?:([01][0-9]|2[0-3]|[1-9]):)([0-5]?[0-9]))$")
time_pattern = re.compile(r"^(?:(?:([01][0-9]|2[0-3]|[1-9]):)([0-5]?[0-9]))")

language_suffixes = ['phrase_arm','phrase_rus','phrase_eng']

weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

months = ['january',
'february',
'march',
'april',
'may',
'june',
'july',
'august',
'september',
'october',
'november',
'december']

def now():
    return datetime.datetime.now().replace(microsecond=0)

def dateForUser(date: datetime.date, cid: int):
    '''January 1'''
    return eval(f'P.{months[date.month-1]}')(cid) + ' ' + str(date.day)

def dateForUser2(date: datetime.date, cid: int):
    '''January 1 (Wednesday)'''
    return eval(f'P.{months[date.month-1]}')(cid) + f' {date.day} (' + eval(f'P.{weekdays[date.weekday()]}')(cid)+')'

def dateForUser3(date: datetime.date, cid: int):
    '''Today / January 1 (Wednesday)'''
    n = now()
    return P.today(cid) if date == n.date() else P.tomorrow(cid) if date == n.date() + datetime.timedelta(days=1) \
        else dateForUser2(date, cid)

def dateForUser4(date: datetime.date, cid: int):
    '''Today / January 1'''
    n = now()
    return P.today(cid) if date == n.date() else P.tomorrow(cid) if date == n.date() + datetime.timedelta(days=1) \
        else dateForUser(date, cid)


def parseTimeInterval(text:str):
    '''start_hour    start minutes    end hour       end minutes'''

    match = time_interval_pattern.match(text)
    if match:#  start_hour    start minutes    end hour       end minutes
        return int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))
    else:
        return None

def parseNameLastName(text: str):
    if len(text) > 30: return None

    n_l = regex.findall(r"[\p{L}]+", text)
    if n_l is None or len(n_l) != 2: return None
    return n_l

phonePattern = re.compile(r"^0(99|98|97|96|95|94|93|91|79|77|66|55|47|44|43|41|33)\d{6}$")
def isPhoneNumber(text: str) -> bool:
    return phonePattern.search(text)

emailPattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
def isEmail(text: str) -> bool:
    return emailPattern.search(text)

def isInstagramUsername(text: str) -> bool:
    return re.search(r"^[a-zA-Z][a-zA-Z0-9._]{0,29}$", text)

def parseMonthDay(text:str):
    try:
        match = re.search(r"^(\d{2}) ?- ?(\d{2})$", text)
        month = int(match.group(1))
        day = int(match.group(2))
        return month,day
    except:
        return None

def parsePhoneNumber(text: str) -> str:
    if type(text) != type(''): return ''
    return text.replace('+','').replace('374','0')

def log(a,b=None,c= None,d=None):
    print('------------------\nA= ',a,'\n------------------')
    if b:
        print('------------------\nB= ',b,'\n------------------')
    if c:
        print('------------------\nC= ',b,'\n------------------')
    if d:
        print('------------------\nD= ',b,'\n------------------')

def str2dt(text: str) -> datetime.datetime:
    if type(text) == datetime.datetime:
        return text
    try:
        return datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S")
    except:
        return datetime.datetime.strptime(text, "%Y-%m-%d")

def ref_code_hash(cid: int) -> str:
    cid = str(cid).encode('utf-8')
    cid = hashlib.md5(cid).digest()
    return base64.urlsafe_b64encode(cid).decode('utf-8')

def validateTime(timeStr: str) -> bool:
    m = time_pattern.search(timeStr)
    return m != None