class USER_SUB_TYPE:
    level_names = {0:'sub_free', 1:'sub_premium', 2:'sub_business'}
    
    @staticmethod
    def get(level: int):
        return USER_SUB_TYPE.level_names[level]

    FREE = 0
    PREMIUM = 1
    BUSINESS = 2