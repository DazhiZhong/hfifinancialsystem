from .factory import FDICT
from django.contrib import messages
from .models import EnvVaribles
import pickle,os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Team():
    namedict = {
        'a1':'夸姆粒子',
        'a2':'重力矿石',
        'a3':'燃烧矿石',
        'b1':'夸姆反应堆',
        'b2':'重力反应堆',
        'b3':'燃烧反应堆',
        'c1':'夸姆机器人',
        'c2':'重力机器人',
        'c3':'燃烧机器人',
    }
    countryname = {
        'a':'大洋邦3',
        'b':'欧亚国3',
        'c':'东亚国3',
        1:'大洋邦2',
        2:'欧亚国2',
        3:'东亚国2'
    }
    factorynamedict = {
        'Factory 1':'一号加工厂',
        'Factory 2':'二号加工厂',
        'Factory 3':'三号加工厂',
        'Level 0':'小型',
        'Level 1':'中型',
        'Level 2':'大型',
        'Level 3':'超大型',
    }
    def __init__(self,name,country_of_origin= 1):
        # 队名
        self.name = name
        # 国家
        self.country = country_of_origin

        import time
        t = time.gmtime()
        self.oldtime = time.strftime('%M',t)
        # self.items 收购物品
        '''
            {
                'name':'a1',
                'qty':10,
                'origin':'a',
                'price_each':10
            },
            {
                'name':'a2',
                'qty':10,
                'origin':'a',
                'price_each':10},
        '''
        self.items = [
        ]

        # storage 仓库， 一共有多少物品
        if self.country == 1:
            self.storage = {
                'a1':50,
                'a2':50,
                'a3':50,
                'b1':0,
                'b2':0,
                'b3':0,
                'c1':0,
                'c2':0,
                'c3':0,
            }
        elif self.country == 2:
            self.storage = {
                'a1':0,
                'a2':0,
                'a3':0,
                'b1':50,
                'b2':50,
                'b3':50,
                'c1':0,
                'c2':0,
                'c3':0,
            }
        elif self.country == 3:
            self.storage = {
                'a1':0,
                'a2':0,
                'a3':0,
                'b1':0,
                'b2':0,
                'b3':0,
                'c1':50,
                'c2':50,
                'c3':50,
            }
       
        # 工厂
        self.factories = [
            ['f1','up0'],
            ['f2','up0'],
            ['f3','up0']
        ]
        self.fact = {}
        
        # 三国货币
        
        if self.country == 1:
            self.money = {
                'a':500,
                'b':0,
                'c':0
            }          
        elif self.country == 2:
            self.money = {
                'a':0,
                'b':500,
                'c':0
            }  
        elif self.country == 3:
            self.money = {
                'a':0,
                'b':0,
                'c':500
            }  
        
        self.parsefact()
    def parsefact(self):
        for factory in self.factories:
            name = f'Factory {factory[0][1]}'
            self.fact[name] = FDICT[self.country][factory[0]][factory[1]]
            level = f'Level {factory[1][2]}'
            self.fact[name]['level'] = level
        '''{'Factory 1': {'intake': {'a1': 1, 'a2': 0, 'a3': 0}, 'output': {'b1': 0, 'b2': 0, 'b3': 0}, 'level': 'Level 0'}, 'Factory 2': {'intake': {'a1': 0, 'a2': 0, 'a3': 0}, 'output': {'b1': 0, 'b2': 0, 'b3': 0}, 'level': 'Level 0'}, 'Factory 3': {'intake': {'a1': 0, 'a2': 0, 'a3': 0}, 'output': {'b1': 0, 'b2': 0, 'b3': 0}, 'level': 'Level 0'}}'''
 
        
    def trans(self,other_team,quantity,item,origin,price):
        '''
        我买你的东西，我的钱 你的item
        '''
        actual_price,into_bank = f(other_team.country,price)
        if check((self.money[origin],other_team.storage[item]),(actual_price,quantity)):
            self.money[origin]-=actual_price
            other_team.money[origin]+=actual_price
            countrylist[other_team.country-1].bank[origin]+=into_bank
            self.storage[item]+=quantity
            other_team.storage[item]-=quantity
            return True
        else: 
            return False


        
        
    def buy(self,item,price_each,quantity,origin):
        '''
        item => str
        price => int
        quantity => int
        origin => str
        '''
        if check((self.storage[item],),(quantity,)):
            self.items.append({
                'name':item,
                'qty':quantity,
                'price_each':price_each,
                'origin':origin
            })
            # if uncomment will need more code
            #self.storage[item]-=quantity
        else: print('ass')

    def upgrade_factory(self,factory_num):
        '''
        factory => ('f1','up0')
        '''
        upprice = {
            0:1001,
            1:1001
        }
        countrynumtostr = {
            1:'a',
            2:'b',
            3:'c'
        }

        now = int(self.factories[factory_num][1][2])
        if self.money[countrynumtostr[self.country]] > upprice[now]:
            self.money[countrynumtostr[self.country]] -= upprice[now]
        if now<2:
            up = f'up{str(now+1)}'
            self.factories[factory_num][1] = up
            print(up)
            self.parsefact()
    def update(self):
        import time
        self.parsefact()
        t = time.gmtime()
        nowtime = time.strftime('%M',t)
        print('tryupdate')
        if nowtime!=self.oldtime:
            nowtime = int(nowtime)
            oldtime = int(self.oldtime)
            if nowtime > oldtime:
                for iiii in range(nowtime-oldtime):
                    print('updated')
                    self.oldtime = time.strftime('%M',t)
                    self.parsefact()
                    for key,item in self.fact.items():
                        print(key,item)
                        if_enough = True
                        print('================s=')
                        for item_type,parse_num in item['intake'].items():
                            print(item_type,parse_num)
                            if self.storage[item_type] < parse_num: 
                                if_enough = False
                        if if_enough:
                            for item_type,parse_num in item['intake'].items():
                                self.storage[item_type]-=parse_num
                            for item_type,parse_num in item['output'].items():
                                self.storage[item_type]+=parse_num

            else:
                for iiii in range(nowtime+60-oldtime):
                    print('updated')
                    self.oldtime = time.strftime('%M',t)
                    self.parsefact()
                    for key,item in self.fact.items():
                        print(key,item)
                        if_enough = True
                        print('================s=')
                        for item_type,parse_num in item['intake'].items():
                            print(item_type,parse_num)
                            if self.storage[item_type] < parse_num: 
                                if_enough = False
                        if if_enough:
                            for item_type,parse_num in item['intake'].items():
                                self.storage[item_type]-=parse_num
                            for item_type,parse_num in item['output'].items():
                                self.storage[item_type]+=parse_num


    def set_id(self,id):
        self.id = id
    def exchange(self,mymoneyorigin,mymoneyqty,exchangemoneyorigin):
        if check((self.money[mymoneyorigin],),(mymoneyqty,)):
            self.money[mymoneyorigin]-=mymoneyqty
            self.money[exchangemoneyorigin]+=mymoneyqty/MONEY_RATIO[mymoneyorigin]*MONEY_RATIO[exchangemoneyorigin]
    def debt():
        pass


    
class Country():
    def __init__(self,name):
        self.name = name
    bank = {
        'a':0,
        'b':0,
        'c':0

    }
    debt = 0
    debt_to = [
        
    ]
    records = ''


    
def f(into_country,qty):
    countrynumtostr = {
        1:'a',
        2:'b',
        3:'c'
    }
    into_bank = qty*TAXES[countrynumtostr[into_country]]
    myamount = qty+into_bank
    return myamount,into_bank

def check(a,b):

    thing = True
    for num,item in enumerate(a):
        if (item-b[num])<0: thing = False

    return thing



 
MONEY_RATIO = {
    'a':30.0,
    'b':3.0,
    'c':14.0
}

TAXES = {

    'a':0.01,
    'b':0.02,
    'c':0.015
}

MAX_ITEMS = {
    'a1':100,
    'a2':100,
    'a3':100,
    'b1':100,
    'b2':100,
    'b3':100,
    'c1':100,
    'c2':100,
    'c3':100,
}


itemtype = [
    'a1',
    'a2',
    'a3',
    'b1',
    'b2',
    'b3',
    'c1',
    'c2',
    'c3',
] 

varibles = EnvVaribles.objects.first()
print(varibles.moneyratio_a)

def loadratio():
    global MONEY_RATIO
    varibles = EnvVaribles.objects.first()
    MONEY_RATIO['a'] = varibles.moneyratio_a
    MONEY_RATIO['b'] = varibles.moneyratio_b
    MONEY_RATIO['c'] = varibles.moneyratio_c
loadratio()

def loadbidding():
    global MAX_ITEMS
    for itemname in itemtype:
        print(type(itemname),itemname)
        MAX_ITEMS[itemname] = getattr(varibles,f'bidding_{itemname}')
loadbidding()

def loadall():
    loadbidding()
    loadratio()



 





Teamlist = [
    ('Team1',1),
    ('Team2',3),
    ('Team3',2),
    ('Team4',1),
    ('Team5',3),
    ('Team6',2),
    ('Team7',1),
    ('Team8',3),
    ('Team9',2),
    ('Team10',1),
    ('Team11',3),
    ('Team12',2),
    ('Team13',1),
    ('Team14',3),
]

tlist = []

def init_teamlist():
    global tlist
    path = os.path.join(BASE_DIR,'pickle/pickle.p')
    
    if os.path.exists(path) and os.path.isfile(path):
        tlist = pickle.load(open(os.path.join(BASE_DIR,'pickle/pickle.p'), "rb" ))
    else:
        for team in Teamlist:
            tlist.append(Team(*team))
            print(*team)
            tlist[len(tlist)-1].set_id(len(tlist)-1)
init_teamlist()

aaa = Country('a')
bbb = Country('b')
ccc = Country('c')
countrylist = [aaa,bbb,ccc]

print(tlist)
#import time
#time.sleep(10)
teamchoice = [(num,a.name) for num,a in enumerate(tlist)]