from django import forms
from .models import Post
from tinymce.widgets import TinyMCE
from .teamlist import Teamlist,teamchoice

#from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):

    shit = forms.ChoiceField(choices=[('as','as'),('bs','bs')], required=False, widget=forms.RadioSelect)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)

    class Meta:
        model = Post
        fields = ("title",'content','shit')

#teamchoice = [(a[1],a[0]) for a in Teamlist]

item_choice = [
    ('a1','夸姆粒子'),
    ('a2','重力矿石'),
    ('a3','燃烧矿石'),
    ('b1','夸姆反应堆'),
    ('b2','重力反应堆'),
    ('b3','燃烧反应堆'),
    ('c1','夸姆机器人'),
    ('c2','重力机器人'),
    ('c3','燃烧机器人'),
]
money_origin_choice = [
    ('a','大洋邦货币'),
    ('b','欧亚国货币'),
    ('c','东亚国货币'),
]
money_buy_choice = [
    ('a','大洋邦货币')
]
class NoForm(forms.Form):

    other_team = forms.ChoiceField(label=' 货品卖家 ', choices=teamchoice, required=False, widget=forms.Select,)
    item_trade = forms.ChoiceField(label='选择货物类型', choices=item_choice, required=False, widget=forms.Select,)
    itemqty = forms.IntegerField(label='货物数量',min_value = 0,initial  = 0)
    moneyorigin = forms.ChoiceField(label='货币种类', choices=money_origin_choice, required=False, widget=forms.Select,)
    moneyqty = forms.IntegerField(label='单个货物价格', min_value = 0,initial  = 0)


class ExchangeForm(forms.Form):
    mymoney_origin = forms.ChoiceField(label='换汇（原本）货币', choices=money_origin_choice, required=False, widget=forms.Select,)
    mymoney_qty = forms.IntegerField(label='货币数量', min_value = 0,initial  = 0)
    exchangemoney_origin = forms.ChoiceField(label='换汇（兑换）货币', choices=money_origin_choice, required=False, widget=forms.Select,)

    


class BuyForm(forms.Form):

    item_buy = forms.ChoiceField(label='选择货物类型', choices=item_choice, required=False, widget=forms.Select,)
    itemqty = forms.IntegerField(label='货物数量', min_value = 0,initial  = 0)
    moneyorigin = forms.ChoiceField(label='货币种类', choices=money_buy_choice, required=False, widget=forms.Select,)
    moneyqty = forms.IntegerField(label='单个货物价格',min_value = 0,initial  = 0)




    

