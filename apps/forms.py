from django import forms


class NameForm(forms.Form):

    age_groups = (('10','전부 다 쩌 쩔어(10s)'), ('20','오로나민씨(20s)'),
               ('30','핫이슈(30s)'),
               ('40','다 사랑스러워(40s)'))
    age = forms.ChoiceField(label='"머리부터 발끝까지" 뒤에 나오는 말은?', choices=age_groups, widget=forms.RadioSelect())

    gender = forms.ChoiceField(label='당신의 성별은?', choices=(('M', "M"),('F', "F")), widget=forms.RadioSelect())

    price_groups = (('0-15','스파이더맨(~15mil)'), ('15-30','캡틴아메리카(15~30mil)'),
               ('30-60','아이언맨(30~60mil)'),
               ('60','배트맨(60mil~)'))
    wage= forms.ChoiceField(label='내가 만약 하루 슈퍼 히어로의 삶을 살게 된다면 누구의 삶을 살까?', choices=price_groups, widget=forms.RadioSelect())


    brand_groups = (('Germany','옥토버페스트에서 살얼음잔에 담긴 시원한 맥주, 그릴에 익힌 소시지와 함께(Germany)'),
                ('Korea','전주 한옥마을을 거닐며 파전과 막걸리 한 잔(Korea)'),
               ('Japan','일본 삿포로에서 불에 살짝 구운 타타키와 시원한 사케(Japan)'),
               ('USA','라스베가스에서 승부수를 던지며 위스키 온더락 한 잔(USA)'),
               ('UK','런던에서 시원한 맥주와 함께 즐기는 프리미어 리그!(UK)'))
    brand = forms.ChoiceField(label='내게 순간이동 능력이 있다면, 금요일 뜨거운 밤을 보내고 싶은 곳은?', choices=brand_groups, widget=forms.RadioSelect())

    type_groups = (('NORMAL','마음이 편안해지는 노래와 함께 도시 이곳 저곳을 드라이브(normal)'),
                ('SUV/RV','연인 또는 가족과 함께 담소를 나누며 캠핑 장소로(SUV/RV)'),
               ('SPORT','뻥 뚫린 고속도로를 시원하게 달리는(Sport)'))
    car_type = forms.ChoiceField(label='차를 몰고 있는 나의 모습을 상상했을 때 가장 좋을 것 같은 드라이브 경험은?', choices=type_groups, widget=forms.RadioSelect())

    size_groups = (('BIG','잘 한다(big)'),
                ('MIDDLE','할 줄은 안다(middle)'),
               ('SMALL/COMPACT','잘 못한다(+ points for small / compact car)'))
    small_car = forms.ChoiceField(label='나는 주차를', choices=size_groups, widget=forms.RadioSelect())

    environment_groups = (('X','텀블러에 따라 마신다(+points for EV/Hybrid)'),
                ('O','종이컵에 따라 마신다'))
    hybrid = forms.ChoiceField(label='커피를 마실 때 나는', choices=environment_groups, widget=forms.RadioSelect())
