
# 장고에서 만들어 주는 form을 정의하는 용도

from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator   # 검증기(유효성 검증)

# [ 유효성 검증 1 ]
# 클래스 내에서 validators를 넣던지(1), clean함수를 넣던지(2) 
# 클래스 외부에 함수를 정의(3)(4)하여 validators에 함수를 넣는다.
# 세 가지 방법으로 유효성을 검증할 수 있다.


# 3)
def my_validator(value):
    if value < 0:
        raise forms.ValidationError('나이는 음수를 사용할 수 없음')
    return value

# 4)
def my_validator2(value):
    if '!' in value:
        raise forms.ValidationError('이름에 !를 사용할 수 없음')
    return value


class PersonForm(forms.Form):       # 장고가 만들어 주는 form을 정의
    name = forms.CharField(
        label='이름',               # label은 보여질 이름을 지정, 나머지는 옵션
        max_length=20, 
        required=True,
        validators=[                # 1) 검증기 (장고가 지원하는 것을 이용)
            MaxLengthValidator(limit_value=20, message="출력될 메시지를 정의"),
            MinLengthValidator(limit_value=4),
            my_validator2   # 4) 검증기
        ]
    ) 
    
    age = forms.IntegerField(
        label='나이', 
        required=True,
        validators=[
            my_validator,   # 3) 검증기
        ]
    )


    # 2) def clean_필드명    # 파라미터 검증에 사용되는 메서드
    def clean_age(self):
        age = self.cleaned_data.get('age', 0)     # cleaned_data에서 값을 꺼내 오고, 값이 없다면 0을 써라
        if age > 150:
            raise forms.ValidationError('값이 범위를 벗어남')
        return age       # 반드시 값 반환
    

#####################################################################

# [ 유효성 검증 2 ]
# 모델을 이용한 form 사용 (모델을 상속)

from .models import Person

class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age']
    
    
    # 유효성 검증 2
    # model에서 유효성을 검증 하던지, form에서 유효성을 검증
    
    # def clean_name(self):
    #     print('name 유효성 검증')
    #     name = self.cleaned_data['name']
    #     if len(name) < 4:
    #         raise forms.ValidationError('길이 오류')
    #     return name     # 반드시 해당 값 반환
    
    # def clean_age(self):
    #     print('age 유효성 검증')
    #     age = self.cleaned_data['age']
    #     if age > 150 :
    #         raise forms.ValidationError('나이 범위 오류')
    #     return age
    
    # # 각 필드를 검증하고 clean을 검증함(검증순서: name -> age -> clean)
    # def clean(self):                # full clean (한번에 name과 age모든 필드를 검증)
    #     print('clean 호출')
    #     print(self.cleaned_data['name'])
    #     print(self.cleaned_data['age'])
    #     return self.cleaned_data    # clean 함수는 반드시 cleaned_data를 반환해야 한다.