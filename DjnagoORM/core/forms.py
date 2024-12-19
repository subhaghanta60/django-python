# from django import forms
# from core.models import Rating



# class RatingForm(forms.ModelForm):
#     class Meta:
#         model=Rating
#         fields = ('restaurant','user','rating')


# from django import forms
# from django.core.validators import MinValueValidator,MaxValueValidator

# class RatingForm(forms.Form):
#     rating = forms.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])


from django import forms
from core.models import Restaurant



class RestaurantForm(forms.ModelForm):
    class Meta:
        model=Restaurant
        fields = ('name','website','data_opened','latitude','longitude','restaurant_type')