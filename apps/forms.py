from django import forms

class NameForm(forms.Form):

    age_groups = (('10','전부 다 쩌 쩔어(10s)'), ('20','오로나민씨(20s)'),
               ('30','핫이슈(30s)'),
               ('40','다 사랑스러워(40s)'))
    age = forms.MultipleChoiceField(choices=age_groups, widget=forms.CheckboxSelectMultiple())

    gender = forms.MultipleChoiceField(choices=(("M", "M"),("F", "F")), widget=forms.CheckboxSelectMultiple())

    price_groups = (('0-15','스파이더맨(~15mil)'), ('15-30','캡틴아메리카(15~30mil)'),
               ('30-60','아이언맨(30~60mil)'),
               ('60','배트맨(60mil~)'))
    wage= forms.MultipleChoiceField(choices=price_groups, widget=forms.CheckboxSelectMultiple())


    brand_groups = (('Germany','옥토버페스트에서 살얼음잔에 담긴 시원한 맥주, 그릴에 익힌 소시지와 함께(Germany)'),
                ('Korea','전주 한옥마을을 거닐며 파전과 막걸리 한 잔(Korea)'),
               ('Japan','일본 삿포로에서 불에 살짝 구운 타타키와 시원한 사케(Japan)'),
               ('Luxury','홍콩 페닌슐라 호텔 스위트룸에서 위스키 한 잔(Luxury)'))
    brand = forms.MultipleChoiceField(choices=brand_groups, widget=forms.CheckboxSelectMultiple())

    type_groups = (('NORMAL','마음이 편안해지는 노래와 함께 도시 이곳 저곳을 드라이브(normal)'),
                ('SUV/RV','연인 또는 가족과 함께 담소를 나누며 캠핑 장소로(SUV/RV)'),
               ('SPORT','뻥 뚫린 고속도로를 시원하게 달리는(Sport)'))
    car_type = forms.MultipleChoiceField(choices=type_groups, widget=forms.CheckboxSelectMultiple())

    size_groups = (('BIG','잘 한다(big)'),
                ('MIDDLE','할 줄은 안다(middle)'),
               ('SMALL/COMPACT','잘 못한다(+ points for small / compact car)'))
    small_car = forms.MultipleChoiceField(choices=size_groups, widget=forms.CheckboxSelectMultiple())

    environment_groups = (('X','텀블러에 따라 마신다(+points for EV/Hybrid)'),
                ('O','종이컵에 따라 마신다'))
    hybrid = forms.MultipleChoiceField(choices=environment_groups, widget=forms.CheckboxSelectMultiple())


    '''
    num_of_doors = forms.CharField(label='Brand', help_text='Enter two numbers, \
    separated by comma')
    aspiration = forms.CharField(label='Wage')
    highway_mpg = forms.CharField(label='Highway mpg',help_text='Enter two numbers, \
    separated by comma' )
    city_mpg = forms.CharField(label='city_mpg',help_text='Enter two numbers, \
    separated by comma')
    horsepower = forms.CharField(label='horsepower',help_text='Enter two numbers, \
    separated by comma')
    body_style = forms.CharField(label='body style')
    '''










    # data = self.cleaned_data
    # return data
