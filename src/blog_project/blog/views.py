from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm,NoForm,BuyForm,ExchangeForm
from .factory import FDICT
from django.contrib.auth.decorators import login_required
import pickle,os


# Create your views here.

from .teamlist import *

viewmoneyratio = {}



def home(request):
    global content
    content = Post.objects.all()
    content = reversed(content)
    return render(request,'home.html',{'title':'ass','cts':content})

def features(request):
    return render(request,'features.html',{'title':'koo'})

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST['shit'])
            return redirect('blog_home')        
    else:
        form = PostForm()
    return render(request,'new.html',{'title':'new','form':form})


def abbs(request):
    if request.method == "POST":
        form = NoForm(request.POST)
        if form.is_valid():
            print(request.POST['assbitch'])       
    else:
        form = NoForm()
    return render(request,'new.html',{'title':'new','form':form})
def teamhome_redirect(r):
    return redirect('teamlist')
def teamlist(request):
    teams = []
    for t in tlist:
        teams.append({
            'id':len(teams),
            'name':t.name,
            'country':t.country
        })
    
    return render(request,'teamlist.html',{'title':'list','teams':teams})

@login_required
def teamhome(request,teamnum):
    global tlist
    if teamnum > len(tlist)-1:
        return redirect('teamlist')
    team = tlist[teamnum]
    team.update()
    if 'Factory 1' in request.GET:

        print('ass1')
        team.upgrade_factory(0)
        return redirect('teamhome',teamnum=team.id)
    if 'Factory 2' in request.GET:
        print('ass2')
        team.upgrade_factory(1)
        return redirect('teamhome',teamnum=team.id)
    if 'Factory 3' in request.GET:
        print('ass3')
        team.upgrade_factory(2)
        return redirect('teamhome',teamnum=team.id)
    if 'item_buy' in request.POST:
        buyform = BuyForm(request.POST)
        if buyform.is_valid():
            print(request.POST['item_buy'])    
            team.buy(request.POST['item_buy'],int(request.POST['moneyqty']),int(request.POST['itemqty']),request.POST['moneyorigin'])
    else:
        buyform = BuyForm()
    
    if 'item_trade' in request.POST:
        tradeform = NoForm(request.POST)
        if tradeform.is_valid():
            #print(request.POST['other_team']) 
            #print(request.POST['other_team'])
            ifsuccess = team.trans(tlist[int(request.POST['other_team'])],int(request.POST['itemqty']),request.POST['item_trade'],request.POST['moneyorigin'],int(request.POST['moneyqty']))
            if not ifsuccess:
                messages.error(request,f'unable to proceed')

            #t = Team()
            #t.trans()
    else:
       
        tradeform = NoForm()
    
    if 'mymoney_origin' in request.POST:
        exchangeform = ExchangeForm(request.POST)
        if exchangeform.is_valid():
            team.exchange(request.POST['mymoney_origin'],int(request.POST['mymoney_qty']),request.POST['exchangemoney_origin'])
    else:
        exchangeform = ExchangeForm()



    return render(request,'teamhome.html',{'title':'new','team':team,'buyform':buyform,'tradeform':tradeform,'exchangeform':exchangeform})


def bidding(request):
        
    text = {
        'title':'Bidding',
        'bigtitle':'Bidding',
        'text':'Press on the button to proceed the bidding!',
        'redir':'buyall',
        'nav':'navbid',
        'button':'Buy!',
        'foo':'bar',
        'bar':'ass'
    }
    
    return render(request,'successful.html',{'text':text})
@login_required
def buyall(request):
    buyallthings()
    text = {
        'title':'Successful',
        'bigtitle':'Successful',
        'text':'The lowest bidders have gotten their money!',
        'redir':'teamlist',
        'nav':'navbid',

        'button':'Go Back!'
    }
    return render(request,'successful.html',{'text':text})



def buyallthings():
    global MAX_ITEMS
    itemlist = {}
    for name in itemtype:
        itemlist[name]=[]

    for num,t in enumerate(tlist):
        for itemnum,item in enumerate(t.items):
            if item['qty']!=0:
                name = item['name']
                item = [t.id,item['price_each'],itemnum]
                itemlist[name].append(item)
    itemlist_sorted = {}
    for name in itemtype:
        itemlist_sorted[name]=sorted(itemlist[name],key = lambda ky:ky[1])
    for name in itemtype:
        item_sorted = itemlist_sorted[name]
        for item in item_sorted:
            if MAX_ITEMS[name] > 0:
                team = tlist[item[0]]
                team_item = team.items[item[2]]
                qty = team_item['qty']
                each = team_item['price_each']
                origin = team_item['origin']
                name = team_item['name']
                if qty<=MAX_ITEMS[name]:
                    MAX_ITEMS[name]-=qty
                else:
                    diff = qty-MAX_ITEMS[name]
                    qty = MAX_ITEMS[name]
                    
                    #MAX_ITEMS[name] = 0
                    #team.items[name]+=diff
                team.money[origin]+=qty*each
                team.storage[name]-=qty
            else:
                pass
    for team in tlist:
        team.items = []

def countryv(request):
    print(countrylist)
    
    return render(request,'country.html',{'country':countrylist})
            
    
def pickle_my_class(request):
    loadall()   
    text = {
        'title':'Pickle',
        'bigtitle':'Pickle My Classes',
        'text':'Press on the button to pickle!',
        'redir':'picklepayload',
        'nav':'navpickle',
        'button':'Pickle!'
    }
    print(MAX_ITEMS)
    print(MONEY_RATIO)
    return render(request,'successful.html',{'title':'pickle','text':text})

def pickle_payload(request):
    #global MAX_ITEMS,MONEY_RATIO
    loadall()
    
    pickle.dump(tlist, open(os.path.join(BASE_DIR,'pickle/pickle.p'), "wb" ) )
    return redirect('teamlist')

def delete_pickle(request):
    #global MAX_ITEMS,MONEY_RATIO
    loadall()
    path = os.path.join(BASE_DIR,'pickle/pickle.p')
    if os.path.exists(path) and os.path.isfile(path):
        os.remove(path)
        init_teamlist()
    return redirect('teamlist')

def load(request):
    loadall()
    for team in tlist:
        team.update()
    print('ass')
    return HttpResponse('')




