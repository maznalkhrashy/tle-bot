from pyrogram import types 




Messages = {
    'MENU':
            u'اهلا بك في بوت إدارة الحسابات .\n'
            u'\n', 
    'LOAD_FILTERS':
                    u'جاري فلترة الحسابات : \n\n'
                    u'عدد الجسابات : {} \n'
                    u'الحسابات التي تعمل : {}\n'
                    u'الحسابات المحضورة : {} \n'
                    u'تم انهاء الجلسة : {} \n'
                    u'محضور من التسجيل : {} \n\n'
                    u'تم الوصول الى : {} \n\n'
                    u'الحالة : {} \n\n',
    'CLEAR':
            u'تم تنضيف حساباتك وحذف الحسابات التي لا تعمل .\n\n'
            u'عدد حساباتك الان : {}'
                    
                    
        

}



class REPLY_MARKUP:

    def MENU_KEYBOARD(ACCOUNTS_LEN):
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text='عدد حساباتك : {}'.format(ACCOUNTS_LEN),  callback_data='NONE')
            ],
            [
                types.InlineKeyboardButton(text='اضافة حساب',  callback_data='ADD_ACCONET'),
                types.InlineKeyboardButton(text='فلترا الحسابات',  callback_data='FILTERS_ACCONET'),
                
            ],
            [
                types.InlineKeyboardButton(text='عرض الحسابات ',  callback_data='SHOW_ACCONET'),
                types.InlineKeyboardButton(text='اعدادات',  callback_data='NONE')
            ]
        ])
    def BACK_KEYBOARD():
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text='رجوع .', callback_data='BACK_HOME')
            ]
        ])

    def LOAD_KEYBAORD(num1:int = 0, num2: int = 0):
        return types.InlineKeyboardMarkup(
            [
                [types.InlineKeyboardButton(text=f'{num1}/{num2}', callback_data='lNOT')]]
        )
    def CLEAR_KEYBAORD():
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text='رجوع .', callback_data='BACK_HOME'),
                types.InlineKeyboardButton(text='تنضيف', callback_data='CLEAR')
            ]
        ])
    


    
