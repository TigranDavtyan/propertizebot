#This is a generated file
from data import DatabaseManager
db = DatabaseManager()

ARM = 0
RUS = 1
ENG = 2
GE  = 3

def language_change(cid : int, all : bool = False) -> str:
    '''🇦🇲🇷🇺🇺🇸🇬🇪 Change language'''
    phrases = ['''🇦🇲🇷🇺🇺🇸🇬🇪 Փոխել լեզուն''', '''🇦🇲🇷🇺🇺🇸🇬🇪 Изменить язык''', '''🇦🇲🇷🇺🇺🇸🇬🇪 Change language''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def language_choose(cid : int, all : bool = False) -> str:
    '''Select language 🇺🇸'''
    phrases = ['''Ընտրեք լեզուն 🇦🇲''', '''Выберите язык 🇷🇺''', '''Select language 🇺🇸''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def languages(cid : int, all : bool = False) -> str:
    '''English🇺🇸'''
    phrases = ['''Հայերեն🇦🇲''', '''Русский🇷🇺''', '''English🇺🇸''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def language_set(cid : int, all : bool = False) -> str:
    '''English is selected 🇺🇸'''
    phrases = ['''Ընտրվեց հայերեն լեզուն 🇦🇲''', '''Выбран русский язык 🇷🇺''', '''English is selected 🇺🇸''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def agree(cid : int, all : bool = False) -> str:
    '''✅ I agree!'''
    phrases = ['''✅ Համաձայն եմ!''', '''✅ Я согласен!''', '''✅ I agree!''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def disagree(cid : int, all : bool = False) -> str:
    '''❌ I disagree'''
    phrases = ['''❌ Համաձայն չեմ''', '''❌ Я не согласен''', '''❌ I disagree''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def cancel(cid : int, all : bool = False) -> str:
    '''🚫 Cancel'''
    phrases = ['''🚫 Չեղարկել''', '''🚫 Отменить''', '''🚫 Cancel''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def canceled(cid : int, all : bool = False) -> str:
    '''🚫 Canceled'''
    phrases = ['''🚫 Չեղարկված է''', '''🚫 Отменено''', '''🚫 Canceled''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def all_right(cid : int, all : bool = False) -> str:
    '''✅ That's right'''
    phrases = ['''✅ Ճիշտ է''', '''✅ Все верно''', '''✅ That's right''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def back(cid : int, all : bool = False) -> str:
    '''👈 Back'''
    phrases = ['''👈 Վերադառնալ''', '''👈 Назад''', '''👈 Back''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def skip(cid : int, all : bool = False) -> str:
    '''👉 Skip'''
    phrases = ['''👉 Բաց թողնել''', '''👉 Пропустить''', '''👉 Skip''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def confirm(cid : int, all : bool = False) -> str:
    '''👍 Confirm'''
    phrases = ['''👍 Հաստատել''', '''👍 Подтвердить''', '''👍 Confirm''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def confirmed(cid : int, all : bool = False) -> str:
    '''👍 Confirmed'''
    phrases = ['''👍 Հաստատված է''', '''👍 Подтверждено''', '''👍 Confirmed''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def yes(cid : int, all : bool = False) -> str:
    '''✅ Yes'''
    phrases = ['''✅ Այո՛''', '''✅ Да''', '''✅ Yes''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def no(cid : int, all : bool = False) -> str:
    '''❌ No'''
    phrases = ['''❌ Ոչ''', '''❌ Нет''', '''❌ No''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def ok(cid : int, all : bool = False) -> str:
    '''ok'''
    phrases = ['''օկ''', '''ок''', '''ok''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def add(cid : int, all : bool = False) -> str:
    '''➕'''
    phrases = ['''➕''', '''➕''', '''➕''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def details(cid : int, all : bool = False) -> str:
    '''🧾'''
    phrases = ['''🧾''', '''🧾''', '''🧾''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def delete(cid : int, all : bool = False) -> str:
    '''❌'''
    phrases = ['''❌''', '''❌''', '''❌''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def wrong_action(cid : int, all : bool = False) -> str:
    '''❌Wrong action❌
 Read the message again☝️, get /help from admin or go to /start and try again.'''
    phrases = ['''❌Սխալ գործողություն❌
 Կրկին կարդացեք հաղորդագրությունը☝️, ստացեք /help ադմինիստրատորից կամ /start արեք և նորից փորձեք:''', '''❌Неверное действие❌
 Прочитайте сообщение еще раз☝️, получите /help от администратора или вернитесь и повторите попытку.''', '''❌Wrong action❌
 Read the message again☝️, get /help from admin or go to /start and try again.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def duration(cid : int, all : bool = False) -> str:
    '''Duration'''
    phrases = ['''Տևողություն''', '''Продолжительность''', '''Duration''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def fee(cid : int, all : bool = False) -> str:
    '''Fee'''
    phrases = ['''Վճար''', '''Плата''', '''Fee''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def dram(cid : int, all : bool = False) -> str:
    '''amd'''
    phrases = ['''դրամ''', '''драм''', '''amd''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def minute(cid : int, all : bool = False) -> str:
    '''minutes'''
    phrases = ['''րոպե''', '''минут''', '''minutes''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def today(cid : int, all : bool = False) -> str:
    '''Today'''
    phrases = ['''Այսօր''', '''Сегодня''', '''Today''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def tomorrow(cid : int, all : bool = False) -> str:
    '''Tomorrow'''
    phrases = ['''Վաղը''', '''Завтра''', '''Tomorrow''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def afterTomorrow(cid : int, all : bool = False) -> str:
    '''The day after tomorrow'''
    phrases = ['''Վաղը չէ մյուս օրը''', '''Послезавтра''', '''The day after tomorrow''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def date(cid : int, all : bool = False) -> str:
    '''Date'''
    phrases = ['''Ամսաթիվ''', '''Дата''', '''Date''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def start2(cid : int, all : bool = False) -> str:
    '''Start'''
    phrases = ['''Սկիզբ''', '''Начало''', '''Start''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def end(cid : int, all : bool = False) -> str:
    '''End'''
    phrases = ['''Վերջ''', '''Конец''', '''End''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def day(cid : int, all : bool = False) -> str:
    '''Day'''
    phrases = ['''Օր''', '''День''', '''Day''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def january(cid : int, all : bool = False) -> str:
    '''January'''
    phrases = ['''Հունվարի''', '''Январь''', '''January''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def february(cid : int, all : bool = False) -> str:
    '''February'''
    phrases = ['''Փետրվարի''', '''Февраль''', '''February''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def march(cid : int, all : bool = False) -> str:
    '''March'''
    phrases = ['''Մարտի''', '''Март''', '''March''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def april(cid : int, all : bool = False) -> str:
    '''April'''
    phrases = ['''Ապրիլի''', '''Апрель''', '''April''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def may(cid : int, all : bool = False) -> str:
    '''May'''
    phrases = ['''Մայիսի''', '''Май''', '''May''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def june(cid : int, all : bool = False) -> str:
    '''June'''
    phrases = ['''Հունիսի''', '''Нюнь''', '''June''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def july(cid : int, all : bool = False) -> str:
    '''July'''
    phrases = ['''Հուլիսի''', '''Июль''', '''July''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def august(cid : int, all : bool = False) -> str:
    '''August'''
    phrases = ['''Օգոստոսի''', '''Август''', '''August''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def september(cid : int, all : bool = False) -> str:
    '''September'''
    phrases = ['''Սեպտեմբերի''', '''Сентябрь''', '''September''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def october(cid : int, all : bool = False) -> str:
    '''October'''
    phrases = ['''Հոկտեմբերի''', '''Октябрь''', '''October''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def november(cid : int, all : bool = False) -> str:
    '''November'''
    phrases = ['''Նոյեմբերի''', '''Ноябрь''', '''November''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def december(cid : int, all : bool = False) -> str:
    '''December'''
    phrases = ['''Դեկտեմբերի''', '''Декабрь''', '''December''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def anonymous(cid : int, all : bool = False) -> str:
    '''unknown 🤷‍♀️'''
    phrases = ['''անհայտ 🤷‍♀️''', '''неизвестный 🤷‍♀️''', '''unknown 🤷‍♀️''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def start(cid : int, all : bool = False) -> str:
    '''Hello 🙂
I am your list.am automation bot. I can help you automate actions on the List.am website.
To get started, please sign up.'''
    phrases = ['''Ողջույն 🙂
Ես քո list.am-ի ավտոմատացման բոտն եմ։ Ես կարող եմ օգնել ձեզ ավտոմատացնել գործողությունները List.am կայքում:
Սկսելու համար խնդրում ենք գրանցվել:''', '''Привет 🙂
Я ваш бот автоматизации list.am. Я могу помочь вам автоматизировать действия на сайте List.am.
Чтобы начать, пожалуйста, зарегистрируйтесь.''', '''Hello 🙂
I am your list.am automation bot. I can help you automate actions on the List.am website.
To get started, please sign up.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def signup_info(cid : int, all : bool = False) -> str:
    '''To perform actions on list.am i need the login password of your list.am page.'''
    phrases = ['''List.am-ում գործողություններ կատարելու համար ինձ անհրաժեշտ է ձեր list.am էջի մուտքի գաղտնաբառը:''', '''Для выполнения действий на list.am мне нужен пароль для входа на вашу страницу list.am.''', '''To perform actions on list.am i need the login password of your list.am page.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def change_logpass(cid : int, all : bool = False) -> str:
    '''Change login info'''
    phrases = ['''Փոխել մուտքի տվյալները''', '''Изменить данные для входа''', '''Change login info''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def signup(cid : int, all : bool = False) -> str:
    '''Sign up'''
    phrases = ['''Գրանցվել''', '''Sign up''', '''Sign up''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def ask_for_login(cid : int, all : bool = False) -> str:
    '''Type the email or phone you use to login into List.am
For example "abracadabra@gmail.com" or "098765432"'''
    phrases = ['''Մուտքագրեք էլփոստը կամ հեռախոսը, որն օգտագործում եք List.am մուտք գործելու համար
Օրինակ՝ «abracadabra@gmail.com» կամ «098765432»''', '''Введите адрес электронной почты или телефон, который вы используете для входа в List.am
Например, «abracadabra@gmail.com» или «098765432».''', '''Type the email or phone you use to login into List.am
For example "abracadabra@gmail.com" or "098765432"''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def ask_for_password(cid : int, all : bool = False) -> str:
    '''Type the password you use to login into List.am
For example "abracadabra"'''
    phrases = ['''Մուտքագրեք գաղտնաբառը, որն օգտագործում եք List.am մուտք գործելու համար
Օրինակ՝ «abracadabra»''', '''Введите пароль, который вы используете для входа в List.am
Например, «абракадабра».''', '''Type the password you use to login into List.am
For example "abracadabra"''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def successfull_login(cid : int, all : bool = False) -> str:
    '''Successfull login'''
    phrases = ['''Successfull login''', '''Successfull login''', '''Successfull login''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def error_login(cid : int, all : bool = False) -> str:
    '''Login error, try again'''
    phrases = ['''Login error, try again''', '''Login error, try again''', '''Login error, try again''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def payment_successfull(cid : int,sub_end, all : bool = False) -> str:
    '''Your payment was successfull🎉 Subscription ends at [sub_end]. '''
    phrases = ['''Ձեր վճարումը հաջող է եղել🎉 Բաժանորդագրությունն ավարտվում է [sub_end]-ին:''', '''Ваш платеж прошел успешно🎉 Подписка заканчивается в [sub_end].''', '''Your payment was successfull🎉 Subscription ends at [sub_end]. ''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[sub_end]",str(sub_end))

def pay_button(cid : int, all : bool = False) -> str:
    '''💵 Pay'''
    phrases = ['''💵 Վճարել''', '''💵 Платить''', '''💵 Pay''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def payment_image_sent(cid : int, all : bool = False) -> str:
    '''Thank you! The admin will review the invoice and will prolong your subscription 🙂'''
    phrases = ['''Շնորհակալություն! Ադմինը կվերանայի հաշիվ-ապրանքագիրը և կերկարաձգի ձեր բաժանորդագրությունը 🙂''', '''Спасибо! Админ рассмотрит счет и продлит подписку 🙂''', '''Thank you! The admin will review the invoice and will prolong your subscription 🙂''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def payment_accepted(cid : int,price, all : bool = False) -> str:
    '''Your payment of [price] dram was successful.'''
    phrases = ['''Ձեր [price] դրամ վճարումը հաջող է եղել''', '''Ваш платеж в размере [price] драма успешно завершен''', '''Your payment of [price] dram was successful.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[price]",str(price))

def payment_declined(cid : int, all : bool = False) -> str:
    '''❗️❗️❗️Your payment was declined by the admin'''
    phrases = ['''❗️❗️❗️Ձեր վճարումը մերժվել է ադմինի կողմից''', '''❗️❗️❗️Ваш платеж отклонен администратором''', '''❗️❗️❗️Your payment was declined by the admin''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def subscription(cid : int, all : bool = False) -> str:
    '''⭐️ Subscription'''
    phrases = ['''⭐️ Բաժանորդագրություն''', '''⭐️ Подписка''', '''⭐️ Subscription''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def sub_info_deactivated(cid : int, all : bool = False) -> str:
    '''Your subscription has been disabled. If you want to subscribe, click "Pay".'''
    phrases = ['''Ձեր բաժանորդագրությունն անջատված է: Եթե ցանկանում եք բաժանորդագրվել, սեղմեք «Վճարել»''', '''Ваша подписка отключена. Если вы хотите подписаться, нажмите «Оплатить»''', '''Your subscription has been disabled. If you want to subscribe, click "Pay".''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def sub_info_free(cid : int,sub_end_days, all : bool = False) -> str:
    '''You have [sub_end_days] days of free trial. To prolong the subscription click "Pay"'''
    phrases = ['''Դուք ունեք [sub_end_days] օր անվճար փորձաշրջան: Բաժանորդագրությունը երկարացնելու համար սեղմեք «Վճարել»''', '''У вас есть [sub_end_days] дней бесплатной пробной версии. Для продления подписки нажмите «Оплатить»''', '''You have [sub_end_days] days of free trial. To prolong the subscription click "Pay"''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[sub_end_days]",str(sub_end_days))

def sub_info_premium(cid : int,sub_end_days, all : bool = False) -> str:
    '''Your subscription ends in [sub_end_days] days. To prolong the subscription click "Pay"'''
    phrases = ['''Ձեր բաժանորդագրությունն ավարտվում է [sub_end_days] օրից: Բաժանորդագրությունը երկարացնելու համար սեղմեք «Վճարել»''', '''Ваша подписка закончится через [sub_end_days] дн. Для продления подписки нажмите «Оплатить»''', '''Your subscription ends in [sub_end_days] days. To prolong the subscription click "Pay"''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[sub_end_days]",str(sub_end_days))

def subscription_not_enough(cid : int,user_sub,min_sub, all : bool = False) -> str:
    '''Your subscription ([user_sub]) is not sufficient for this action. Minimum subscription level for this action is "[min_sub]"․'''
    phrases = ['''Ձեր բաժանորդագրությանը ([user_sub]) բավարար չէ այս գործողության համար: Այս գործողության համար բաժանորդագրության նվազագույն մակարդակը "[min_sub]" է''', '''Уровень вашей подписки ([user_sub]) недостаточен для этого действия. Минимальный уровень подписки для этого действия: "[min_sub]"''', '''Your subscription ([user_sub]) is not sufficient for this action. Minimum subscription level for this action is "[min_sub]"․''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[user_sub]",str(user_sub)).replace("[min_sub]",str(min_sub))

def subscription_end(cid : int, all : bool = False) -> str:
    '''❗️ Warning ❗️
Your subscribtion ended.'''
    phrases = ['''❗️ Զգուշացում ❗️
Ձեր բաժանորդագրությունն ավարտվել է:''', '''❗️ Предупреждение ❗️
Ваша подписка закончилась.''', '''❗️ Warning ❗️
Your subscribtion ended.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def payment_info(cid : int, all : bool = False) -> str:
    '''To prolong the subscribtion send money to this bank card <code>5501040100593259</code>, and send the photo of the invoice as a reply to this message.
6 months ---- 29000 dram
12 months --- 49000 dram'''
    phrases = ['''Բաժանորդագրությունը երկարացնելու համար գումար ուղարկեք այս բանկային քարտին <code>5501040100593259</code>, և որպես պատասխան այս հաղորդագրության ուղարկեք հաշիվ-ապրանքագրի լուսանկարը:
6 ամիս ---- 29000 դրամ
12 ամիս --- 49000 դրամ''', '''Для продления подписки отправьте деньги на эту банковскую карту <code>5501040100593259</code>, а в ответ на это сообщение отправьте фото счета.
6 месяцев ---- 29000 драм
12 месяцев --- 49000 драм''', '''To prolong the subscribtion send money to this bank card <code>5501040100593259</code>, and send the photo of the invoice as a reply to this message.
6 months ---- 29000 dram
12 months --- 49000 dram''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def menu(cid : int, all : bool = False) -> str:
    '''📜 Menu'''
    phrases = ['''📜 Մենյու''', '''📜 Меню''', '''📜 Menu''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def wrong_format(cid : int, all : bool = False) -> str:
    '''❌ Wrong format, try again'''
    phrases = ['''❌ Սխալ ձևաչափ, նորից փորձեք''', '''❌ Неверный формат, попробуйте еще раз''', '''❌ Wrong format, try again''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def renew_now(cid : int, all : bool = False) -> str:
    '''♻️Renew now'''
    phrases = ['''♻️Թարմացնել հիմա''', '''♻️Обнови сейчас''', '''♻️Renew now''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def renewd_n_items(cid : int,nRenews, all : bool = False) -> str:
    '''♻️Updated [nRenews] listings♻️'''
    phrases = ['''♻️Թարմացվել է [nRenews] հայտարարություն♻️''', '''♻️Обновлено [nRenews] объявлении♻️''', '''♻️Updated [nRenews] listings♻️''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[nRenews]",str(nRenews))

def cant_renew_for_30_mins(cid : int, all : bool = False) -> str:
    '''❌ You cant renew now ❗️ You can renew once for every 30 minutes.'''
    phrases = ['''❌ Այժմ չեք կարող թարմացնել ❗️ Կարող եք թարմացնել 30 րոպեն մեկ անգամ։''', '''❌ Обновить сейчас нельзя ❗️ Обновлять можно один раз каждые 30 минут.''', '''❌ You cant renew now ❗️ You can renew once for every 30 minutes.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def send_code(cid : int, all : bool = False) -> str:
    '''❗️❗️❗️ A verification code has been sent to your phone or email. Please check your phone or email (which you use to log in to list.am) and then enter the code here to complete the verification process and log in.⬇️⬇️⬇️'''
    phrases = ['''❗️❗️❗️ Հաստատման կոդը ուղարկվել է ձեր հեռախոսին կամ էլ․ փոստին։ Խնդրում եմ ստուգել ձեր հեռախոսը կամ էլ․փոստը(որը օգտագործում եք list.am մուտք գործելու համար) այնուհետև մուտքագրեք կոդը այստեղ՝ ստուգման գործընթացը ավարտելու և մուտք գործելու համար:⬇️⬇️⬇️''', '''❗️❗️❗️ Код подтверждения был отправлен на ваш телефон или электронную почту. Пожалуйста, проверьте свой телефон или электронную почту (которую вы используете для входа на list.am), а затем введите здесь код, чтобы завершить процесс проверки и войти в систему.⬇️⬇️⬇️''', '''❗️❗️❗️ A verification code has been sent to your phone or email. Please check your phone or email (which you use to log in to list.am) and then enter the code here to complete the verification process and log in.⬇️⬇️⬇️''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def setup_renew_times(cid : int, all : bool = False) -> str:
    '''⚙️ Setup renew times'''
    phrases = ['''⚙️ Կարգավորեք թարմացման ժամերը''', '''⚙️ Настройка времени обновления''', '''⚙️ Setup renew times''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def times_info(cid : int, all : bool = False) -> str:
    '''These are the times the bot will automatically renew your listing.'''
    phrases = ['''Սրանք այն ժամանակներն են, երբ բոտը ավտոմատ կթարմացնի ձեր հայտարարությունները:''', '''В эти времена бот будет автоматически обновлять ваши объявления.''', '''These are the times the bot will automatically renew your listing.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def ask_new_time(cid : int, all : bool = False) -> str:
    '''Enter the time you want to renew your listings, for example <code>15:00</code>'''
    phrases = ['''Մուտքագրեք այն ժամը, երբ ցանկանում եք թարմացնել ձեր հայտարարությունները, օրինակ <code>15:00</code>''', '''Введите время, когда вы хотите обновить свои объявления, например <code>15:00</code>.''', '''Enter the time you want to renew your listings, for example <code>15:00</code>''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def ask_new_limit(cid : int, all : bool = False) -> str:
    '''Enter the maximum number of listings you want to renew, for example <code>50</code>'''
    phrases = ['''Մուտքագրեք հայտարարությունների առավելագույն քանակը, որոնք ցանկանում եք թարմացնել, օրինակ <code>50</code>''', '''Введите максимальное количество объявлений, которые вы хотите продлить, например <code>50</code>.''', '''Enter the maximum number of listings you want to renew, for example <code>50</code>''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def time_added_successfully(cid : int, all : bool = False) -> str:
    '''✅ Renew time added successfully ✅'''
    phrases = ['''✅ Թարմացնելու ժամը հաջողությամբ ավելացվեց ✅''', '''✅ Время объявления успешно добавлено ✅''', '''✅ Renew time added successfully ✅''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def change_time(cid : int, all : bool = False) -> str:
    '''Enter a new time for renew, for example <code>15:00</code>'''
    phrases = ['''Մուտքագրեք թարմացման նոր ժամ, օրինակ <code>15:00</code>''', '''Введите новое время объявления, например <code>15:00</code>.''', '''Enter a new time for renew, for example <code>15:00</code>''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def time_changed_successfully(cid : int, all : bool = False) -> str:
    '''✅Time changed successfully ✅'''
    phrases = ['''✅Ժամը հաջողությամբ փոխվեց ✅''', '''✅Время успешно изменено ✅''', '''✅Time changed successfully ✅''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def change_limit(cid : int, all : bool = False) -> str:
    '''Enter a new limit, for example <code>50</code>'''
    phrases = ['''Մուտքագրեք նոր սահմանաչափ, օրինակ <code>50</code>''', '''Введите новый лимит, например <code>50</code>.''', '''Enter a new limit, for example <code>50</code>''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def limit_changed_successfully(cid : int, all : bool = False) -> str:
    '''✅ Limit changed successfully ✅'''
    phrases = ['''✅ Սահմանաչափը հաջողությամբ փոխվեց ✅''', '''✅ Лимит успешно изменен ✅''', '''✅ Limit changed successfully ✅''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]