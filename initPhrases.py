import re

def insertPhrase(name:str, arm:str, rus:str, eng:str):
    global phrasespy

    matches = re.findall(r'(\[.*?\])', eng)
    arguments = ''
    replaces = ''
    for arg in matches:
        argn = arg[1:-1]
        arguments += argn + ','
        replaces += f'.replace("{arg}",str({argn}))'


    phrasespy.write(f"""\n\ndef {name}(cid : int,{arguments} all : bool = False) -> str:
    '''{eng}'''
    phrases = ['''{arm}''', '''{rus}''', '''{eng}''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]{replaces}""")


phrasespy = open("./phrases/phrases.py", "w", encoding="utf-8")
phrasespy.write('''#This is a generated file
from data import DatabaseManager
db = DatabaseManager()

ARM = 0
RUS = 1
ENG = 2
GE  = 3''')


#language
insertPhrase('language_change','🇦🇲🇷🇺🇺🇸🇬🇪 Փոխել լեզուն', '🇦🇲🇷🇺🇺🇸🇬🇪 Изменить язык', '🇦🇲🇷🇺🇺🇸🇬🇪 Change language')
insertPhrase('language_choose','Ընտրեք լեզուն 🇦🇲', 'Выберите язык 🇷🇺', 'Select language 🇺🇸')
insertPhrase('languages','Հայերեն🇦🇲', 'Русский🇷🇺', 'English🇺🇸')
insertPhrase('language_set','Ընտրվեց հայերեն լեզուն 🇦🇲','Выбран русский язык 🇷🇺','English is selected 🇺🇸')

insertPhrase('agree','✅ Համաձայն եմ!','✅ Я согласен!','✅ I agree!')
insertPhrase('disagree','❌ Համաձայն չեմ','❌ Я не согласен','❌ I disagree')
insertPhrase('cancel','🚫 Չեղարկել','🚫 Отменить','🚫 Cancel')
insertPhrase('canceled','🚫 Չեղարկված է','🚫 Отменено','🚫 Canceled')
insertPhrase('all_right','✅ Ճիշտ է','✅ Все верно',"✅ That's right")
insertPhrase('back','👈 Վերադառնալ','👈 Назад','👈 Back')
insertPhrase('skip','👉 Բաց թողնել','👉 Пропустить','👉 Skip')
insertPhrase('confirm','👍 Հաստատել','👍 Подтвердить','👍 Confirm')
insertPhrase('confirmed','👍 Հաստատված է','👍 Подтверждено','👍 Confirmed')
insertPhrase('yes','✅ Այո՛', '✅ Да', '✅ Yes')
insertPhrase('no','❌ Ոչ', '❌ Нет', '❌ No')
insertPhrase('ok', 'օկ', 'ок', 'ok')

insertPhrase('wrong_action',
             '❌Սխալ գործողություն❌\n Կրկին կարդացեք հաղորդագրությունը☝️, ստացեք /help ադմինիստրատորից կամ /start արեք և նորից փորձեք:',
             '❌Неверное действие❌\n Прочитайте сообщение еще раз☝️, получите /help от администратора или вернитесь и повторите попытку.',
             '❌Wrong action❌\n Read the message again☝️, get /help from admin or go to /start and try again.')


insertPhrase('duration','Տևողություն', 'Продолжительность', 'Duration')
insertPhrase('fee','Վճար', 'Плата', 'Fee')
insertPhrase('dram','դրամ', 'драм', 'amd')
insertPhrase('minute','րոպե', 'минут', 'minutes')

insertPhrase('today','Այսօր', 'Сегодня', 'Today')
insertPhrase('tomorrow','Վաղը', 'Завтра', 'Tomorrow')
insertPhrase('afterTomorrow','Վաղը չէ մյուս օրը', 'Послезавтра', 'The day after tomorrow')
insertPhrase('date','Ամսաթիվ', 'Дата', 'Date')

insertPhrase('start2', 'Սկիզբ', 'Начало', 'Start')
insertPhrase('end', 'Վերջ', 'Конец', 'End')
insertPhrase('day', 'Օր', 'День', 'Day')


insertPhrase('january',     'Հունվարի',   'Январь',  'January')
insertPhrase('february',    'Փետրվարի',   'Февраль', 'February')
insertPhrase('march',       'Մարտի',      'Март',    'March')
insertPhrase('april',       'Ապրիլի',     'Апрель',  'April')
insertPhrase('may',         'Մայիսի',     'Май',     'May')
insertPhrase('june',        'Հունիսի',    'Нюнь',    'June')
insertPhrase('july',        'Հուլիսի',    'Июль',    'July')
insertPhrase('august',      'Օգոստոսի',   'Август',  'August')
insertPhrase('september',   'Սեպտեմբերի', 'Сентябрь','September')
insertPhrase('october',     'Հոկտեմբերի', 'Октябрь', 'October')
insertPhrase('november',    'Նոյեմբերի',  'Ноябрь',  'November')
insertPhrase('december',    'Դեկտեմբերի', 'Декабрь', 'December')

insertPhrase('details','🧾','🧾','🧾')
insertPhrase('cancel','❌','❌','❌' )

insertPhrase('anonymous', 'անհայտ 🤷‍♀️','неизвестный 🤷‍♀️','unknown 🤷‍♀️' )





insertPhrase('start',
'''Ողջույն 🙂
Ես քո list.am-ի ավտոմատացման բոտն եմ։ Ես կարող եմ օգնել ձեզ ավտոմատացնել գործողությունները List.am կայքում:
Սկսելու համար խնդրում ենք գրանցվել:''',
'''Привет 🙂
Я ваш бот автоматизации list.am. Я могу помочь вам автоматизировать действия на сайте List.am.
Чтобы начать, пожалуйста, зарегистрируйтесь.''',
'''Hello 🙂
I am your list.am automation bot. I can help you automate actions on the List.am website.
To get started, please sign up.''')

#help
# insertPhrase('help',
#              'Եթե անելանելի վիճակում եք կամ հարցեր ունեք, կարող եք կապվել ադմինիստրատորի հետ <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>։ Նա անպայման կօգնի ձեզ🙂', 
#              'Если вы застряли или у вас есть какие-либо вопросы, вы можете связаться с администратором по адресу <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>․ Он обязательно вам поможет🙂', 
#              'If you are stuck or have any questions you can contact the admin at <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>․ He will definitely help you🙂',
#              'თუ გაჭედილი ხართ ან გაქვთ რაიმე შეკითხვა, შეგიძლიათ დაუკავშირდეთ ადმინისტრატორს მისამართზე <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>. ის აუცილებლად დაგეხმარება 🙂')

insertPhrase('signup_info',
             'List.am-ում գործողություններ կատարելու համար ինձ անհրաժեշտ է ձեր list.am էջի մուտքի գաղտնաբառը:', 
             'Для выполнения действий на list.am мне нужен пароль для входа на вашу страницу list.am.', 
             'To perform actions on list.am i need the login password of your list.am page.')

insertPhrase('change_logpass','Փոխել մուտքի տվյալները','Изменить данные для входа','Change login info')
insertPhrase('signup','Գրանցվել', 'Sign up', 'Sign up')

insertPhrase('ask_for_login',
             'Մուտքագրեք էլփոստը կամ հեռախոսը, որն օգտագործում եք List.am մուտք գործելու համար\nՕրինակ՝ «abracadabra@gmail.com» կամ «098765432»',
             'Введите адрес электронной почты или телефон, который вы используете для входа в List.am\nНапример, «abracadabra@gmail.com» или «098765432».', 
             'Type the email or phone you use to login into List.am\nFor example "abracadabra@gmail.com" or "098765432"')

insertPhrase('ask_for_password',
             'Մուտքագրեք գաղտնաբառը, որն օգտագործում եք List.am մուտք գործելու համար\nՕրինակ՝ «abracadabra»', 
             'Введите пароль, который вы используете для входа в List.am\nНапример, «абракадабра».', 
             'Type the password you use to login into List.am\nFor example "abracadabra"')

insertPhrase('successfull_login','Successfull login', 'Successfull login', 'Successfull login')
insertPhrase('error_login','Login error, try again', 'Login error, try again', 'Login error, try again')


insertPhrase('payment_successfull', 
'''Ձեր վճարումը հաջող է եղել🎉 Բաժանորդագրությունն ավարտվում է [sub_end]-ին:''',
'''Ваш платеж прошел успешно🎉 Подписка заканчивается в [sub_end].''',
'''Your payment was successfull🎉 Subscription ends at [sub_end]. ''')

# insertPhrase('billing_info', 
# 'Վճարման ամսաթիվը [date] է ([days] օր մինչև վճարումը): Վճարման գումարը [pay_amount] դրամ է:',
# 'Дата платежа [date] ([days] дней до платежа). Сумма платежа составляет [pay_amount] драм.',
# "Payment date is [date] ([days] days until payment). Payment amount is [pay_amount] dram.")

insertPhrase('pay_button', '💵 Վճարել','💵 Платить','💵 Pay')

insertPhrase('payment_image_sent', 
             'Շնորհակալություն! Ադմինը կվերանայի հաշիվ-ապրանքագիրը և կերկարաձգի ձեր բաժանորդագրությունը 🙂',
             'Спасибо! Админ рассмотрит счет и продлит подписку 🙂',
             'Thank you! The admin will review the invoice and will prolong your subscription 🙂')

insertPhrase('payment_accepted', 'Ձեր [price] դրամ վճարումը հաջող է եղել','Ваш платеж в размере [price] драма успешно завершен','Your payment of [price] dram was successful.')

insertPhrase('payment_declined', '❗️❗️❗️Ձեր վճարումը մերժվել է ադմինի կողմից', '❗️❗️❗️Ваш платеж отклонен администратором', '❗️❗️❗️Your payment was declined by the admin')

#Subscription
insertPhrase('subscription', '⭐️ Բաժանորդագրություն','⭐️ Подписка','⭐️ Subscription')


insertPhrase('sub_info_deactivated', 
             'Ձեր բաժանորդագրությունն անջատված է: Եթե ցանկանում եք բաժանորդագրվել, սեղմեք «Վճարել»',
             'Ваша подписка отключена. Если вы хотите подписаться, нажмите «Оплатить»',
             'Your subscription has been disabled. If you want to subscribe, click "Pay".')

insertPhrase('sub_info_free', 
             'Դուք ունեք [sub_end_days] օր անվճար փորձաշրջան: Բաժանորդագրությունը երկարացնելու համար սեղմեք «Վճարել»',
             'У вас есть [sub_end_days] дней бесплатной пробной версии. Для продления подписки нажмите «Оплатить»',
             'You have [sub_end_days] days of free trial. To prolong the subscription click "Pay"')

insertPhrase('sub_info_premium', 
             'Ձեր բաժանորդագրությունն ավարտվում է [sub_end_days] օրից: Բաժանորդագրությունը երկարացնելու համար սեղմեք «Վճարել»',
             'Ваша подписка закончится через [sub_end_days] дн. Для продления подписки нажмите «Оплатить»',
             'Your subscription ends in [sub_end_days] days. To prolong the subscription click "Pay"')

insertPhrase('subscription_not_enough', 
             'Ձեր բաժանորդագրությանը ([user_sub]) բավարար չէ այս գործողության համար: Այս գործողության համար բաժանորդագրության նվազագույն մակարդակը "[min_sub]" է',
             'Уровень вашей подписки ([user_sub]) недостаточен для этого действия. Минимальный уровень подписки для этого действия: "[min_sub]"',
             'Your subscription ([user_sub]) is not sufficient for this action. Minimum subscription level for this action is "[min_sub]"․')

# insertPhrase('subscription_end_close', 
# '⚠️ Զգուշացում ⚠️\nՁեր բաժանորդագրությունն ավարտվում է [days] օրից: Բաժանորդագրությունը վճարելու և երկարացնելու համար գնացեք «Վճարումներ» ընտրացանկը:',
# '⚠️ Внимание ⚠️\nВаша подписка заканчивается через [days] дней. Перейдите в меню «Оплата», чтобы оплатить и продлить подписку.',
# '⚠️ Warning ⚠️\nYour subscribtion ends in [days] days. Go to "Billing" menu to pay and prolong the subscription.')

insertPhrase('subscription_end', 
'❗️ Զգուշացում ❗️\nՁեր բաժանորդագրությունն ավարտվել է:',
'❗️ Предупреждение ❗️\nВаша подписка закончилась.',
'❗️ Warning ❗️\nYour subscribtion ended.')


insertPhrase('payment_info', 
'''Բաժանորդագրությունը երկարացնելու համար գումար ուղարկեք այս բանկային քարտին <code>5501040100593259</code>, և որպես պատասխան այս հաղորդագրության ուղարկեք հաշիվ-ապրանքագրի լուսանկարը:
6 ամիս ---- 29000 դրամ
12 ամիս --- 49000 դրամ''',

'''Для продления подписки отправьте деньги на эту банковскую карту <code>5501040100593259</code>, а в ответ на это сообщение отправьте фото счета.
6 месяцев ---- 29000 драм
12 месяцев --- 49000 драм''',

'''To prolong the subscribtion send money to this bank card <code>5501040100593259</code>, and send the photo of the invoice as a reply to this message.
6 months ---- 29000 dram
12 months --- 49000 dram''')

insertPhrase('menu','📜 Մենյու','📜 Меню','📜 Menu')


insertPhrase('wrong_format','❌ Սխալ ձևաչափ, նորից փորձեք', '❌ Неверный формат, попробуйте еще раз', '❌ Wrong format, try again')

phrasespy.close()