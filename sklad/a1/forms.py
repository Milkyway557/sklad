from django import forms
from .models import nameOfItem,Commodity,history,Useless,Personal

class UselessForm(forms.ModelForm):
	class Meta:
		model = Useless
		fields = '__all__'
		
		widgets = {
		  'product':forms.Select(attrs={
		  	'class':'form-select form-select-lg mb-3',
		  	'name':'product',
		  	'id':'product',
		  	}),
		  'quantity':forms.NumberInput(attrs={
		  	'class':'form-control',
		    'name':'quantity',
		    'id':'quantity'
		    })
		}

class PersonalForm(forms.ModelForm):
	class Meta:
		model = Personal
		fields = '__all__'
	    
		widgets = {
		  'product':forms.Select(attrs={
		  	'class':'form-select form-select-lg mb-3',
		  	'name':'product',
		  	'id':'product',
		  	}),
		  'quantity':forms.NumberInput(attrs={
		  	'class':'form-control',
		    'name':'quantity',
		    'id':'quantity'
		    })
		}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for key,field in self.fields.items():
			field.label=""


class HistoryForm(forms.ModelForm):
	class Meta:
		model = history
		fields = '__all__'

		widgets = {
		  'product':forms.Select(attrs={
		  	'class':'form-select form-select-lg mb-3',
		  	'name':'product',
		  	'id':'product',
		  	}),
		  'quantity':forms.NumberInput(attrs={
		  	'class':'form-control',
		    'name':'quantity',
		    'id':'quantity'
		    })
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for key,field in self.fields.items():
			field.label=""


class NameOfForm(forms.ModelForm):
	class Meta:
		model = nameOfItem
		fields = '__all__'

		widgets = {
		  'nameof':forms.TextInput(attrs={
		  	'class':'form-control',
		  	'placeholder':'Maxsulot nomi'
		  	}),
		  'typeof':forms.Select(attrs={
		  	'class':'form-select form-select-lg mb-3',
		  	'aria-label':'.form-select-lg example'
		  	}),
		  'limited':forms.NumberInput(attrs={
		  	'class':'form-control',
		  	'placeholder':'Maxsulot max limitini kiriting(50,100...)'
		  	})
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for key,field in self.fields.items():
			field.label=""	

        	
class CommodityForm(forms.ModelForm):
	class Meta:
		model = Commodity
		fields = '__all__'

		widgets = {
		  'name':forms.Select(attrs={
		  	'class':'form-select form-select-lg mb-3',
		  	}),
		  'quantity':forms.NumberInput(attrs={
		  	'class':'form-control',
		  	'aria-label':'.form-select-lg example'
		  	}),
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for key,field in self.fields.items():
			field.label=""	
