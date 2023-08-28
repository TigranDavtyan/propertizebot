from subscriptions.subscriptions import USER_SUB_TYPE

class State:
    states = {}
    @staticmethod
    def get(state):
        if type(state) is int:
            return State.states.get(state)
        return State.states.get(state.ID)
    
    def __hash__(self) -> int:
        return self.ID.__hash__()
    
    def __eq__(self, __value: object) -> bool:
        if type(__value) == int:
            return self.ID == __value
        elif type(__value) == State:
            return self.ID == __value.ID
        else:
            raise ValueError('Value type must be State or int.')
    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)
    
    def __init__(self, id, next = -1, min_subscription = USER_SUB_TYPE.FREE):
        self.ID = id
        self.NEXT = next
        self.ACTION = None
        self.min_subscription = min_subscription
        State.states[self.ID] = self

    async def __call__(self, *kwarg, **args):
        return await self.ACTION(*kwarg, **args)

    def __str__(self):
        return str(self.ID)

    def setAction(self, action):
        self.ACTION = action

class GENERAL:
    NOT_AVAILABLE = State(-2)
    ERROR = State(-1)
    START = State(0)

    class LANGUAGE:
        CHOOSE = State(2, 4)
        FINISH = State(4)

class ADMIN:
    MENU = State(1000)
    
    ADD_6MONTHS = State(1010)
    ADD_12MONTHS = State(1020)
    DECLINE_PAYMENT = State(1030)

    BROADCAST = State(1050, 1052)
    BROADCAST_HANDLE = State(1052, 1054)
    BROADCAST_CONFIRM = State(1054)

    ACTIVATE_PREMIUM = State(1060, 1062)
    ACTIVATE_PREMIUM_HANDLE = State(1062)

class USER:
    MAIN_MENU = State(10)

    class SIGNUP:
        INFO = State(20)
        
        LOGIN = State(30, 32)
        HANDLE_LOGIN = State(32, 34)
        HANDLE_PASSWORD = State(34)
        
        SUCCESS = State(50)
        ERROR = State(60)

    class REFERRAL:
        INFO = State(100)
        GET_BOUNS = State(110)
  
    class SUBSCRIPTION:
        INFO = State(200)
        PAY_INFO = State(210, 220)
        INVOICE = State(220)
    
    class ACTIONS:
        RENEW = State(300)
