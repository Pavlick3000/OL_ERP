from django import forms
from .models import NomencBook, ProductionType

class NomencBookAdminForm(forms.ModelForm):
    type_of_reproduction = forms.ModelChoiceField(
        queryset=ProductionType.objects.all(),
        to_field_name="reproduction",  # Указывает, что будет сохраняться значение из поля reproduction
        label="Вид воспроизводства",
        required=False,
        widget=forms.Select
    )

    class Meta:
        model = NomencBook
        fields = '__all__'

    # def clean(self):
    #     cleaned_data = super().clean()
    #     Production_Type = cleaned_data.get('type_of_reproduction')
    #
    #     if Production_Type:
    #         # Сохраняем значение поля reproduction
    #         cleaned_data['type_of_reproduction'] = Production_Type.reproduction
    #     return cleaned_data