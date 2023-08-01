from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator

# [ 유효성 검증 2 (model에서) ]
# forms.py 에서 말고 model 작성 시 유효성 검증 함께

def validate_name_length(value):
    print('name 유효성 검증')
    if len(value) < 4:
        raise ValidationError('길이 오류')
    return value    # 반드시 해당 값 반환

def validate_age_length(value):
    print('age 유효성 검증')
    if not 0 < value < 150 :
        raise ValidationError('나이 범위 오류')
    return value
    

class Person(models.Model):
    name = models.CharField(
        max_length=20,
        null=False,
        validators=[    # 검증기 등록
            validate_name_length,
            MaxLengthValidator(limit_value=20, message="최대 길이 오류")
        ]     
    )
    
    age = models.IntegerField(
        null=False,
        validators=[
            validate_age_length,
        ]
    )
    
    def __str__(self):
        return f"Person [id={self.id}, name={self.name}, age={self.age}]"