from django.shortcuts import render
from .models import Commodity,Personal,nameOfItem,history,history_added,Useless
from .forms import CommodityForm,NameOfForm,HistoryForm,PersonalForm,UselessForm
# Create your views here.

def home(request):
	return render(request, 'index.html', {})

def UserlessFunc(request):
	message = ""
	if request.method == 'POST':
		form = UselessForm(request.POST)
		if form.is_valid():

			product = form.cleaned_data['product']
			quantity = float(form.cleaned_data['quantity'])
			nameItem = nameOfItem.objects.get(nameof=product)
			
			try:
				comm = Commodity.objects.get(name=nameItem)
				if(comm.quantity>quantity):
					form.save()
					message = "Muvaffaqiyatli"
					comm.quantity-=quantity
					comm.save()
				else:
					txt = str(comm.quantity)+" "+str(comm.name.typeof)
					message = "Miqdor ziyod, omborda {} bor".format(txt)
			except:
				message = "Bunday tovar qolmagan"
	
		else:
		    message = "Xatolik"	
	form = HistoryForm()
	context = {
	  'form':form,
	  'message':message,
	}
	return render(request, 'useless.html', context)

def PersonalFunc(request):
	message = ""
	if request.method == 'POST':
		form = PersonalForm(request.POST)
		if form.is_valid():

			product = form.cleaned_data['product']
			quantity = float(form.cleaned_data['quantity'])
			nameItem = nameOfItem.objects.get(nameof=product)
			
			try:
				comm = Commodity.objects.get(name=nameItem)
				if(comm.quantity>quantity):
					form.save()
					message = "Muvaffaqiyatli"
					comm.quantity-=quantity
					comm.save()
				else:
					txt = str(comm.quantity)+" "+str(comm.name.typeof)
					message = "Miqdor ziyod, omborda {} bor".format(txt)
			except:
				message = "Bunday tovar qolmagan"
	
		else:
		    message = "Xatolik"	
	form = HistoryForm()
	context = {
	  'form':form,
	  'message':message,
	}
	return render(request, 'Personal.html', context)

def summary(request):
	histories = history.objects.all()
	addeds = history_added.objects.all()
	personals = Personal.objects.all()
	uselesses = Useless.objects.all()
	context = {
	'histories':histories,
	'addeds':addeds,
	'personals':personals,
	'uselesses':uselesses
	}
	return render(request, 'summary.html',context)

def warehouse(request):
	commodity = Commodity.objects.all()
	form1 = CommodityForm()
	context = {
	  'commodity':commodity,
	  'form1':form1,
	}
	return render(request, 'warehouse.html', context)

def NewItem(request):
	message = ""
	if request.method == 'POST':
		form = NameOfForm(request.POST)
		if form.is_valid():
			form.save()
			message = "Muvaffaqiyatli"
		else:
		    message = "Xatolik"
	form = NameOfForm()
	context = {
	  'form':form,
	  'message':message,
	}
	return render(request, 'newItem.html', context)

def AddProduct(request):
	message = ""
	if request.method == "POST":
		form = CommodityForm(request.POST)
		if form.is_valid():
			form.save()
			f2 = history_added(
				product = form.cleaned_data['name'],
				quantity = form.cleaned_data['quantity']
			)
			f2.save()
			message = "Muvaffaqiyatli"
		else:
		    message = "Xatolik"	
	form = CommodityForm()
	context = {
	'form':form,
	'message':message,
	} 
	return render(request, 'AddProduct.html', context)


def outWareHouse(request):
	message = ""
	if request.method == 'POST':
		form = HistoryForm(request.POST)
		if form.is_valid():
			product = form.cleaned_data['product']
			quantity = float(form.cleaned_data['quantity'])
			nameItem = nameOfItem.objects.get(nameof=product)
			try:
				comm = Commodity.objects.get(name=nameItem)
				if(comm.quantity>quantity):
					form.save()
					message = "Muvaffaqiyatli"
					comm.quantity-=quantity
					comm.save()
				else:
					txt = str(comm.quantity)+" "+str(comm.name.typeof)
					message = "Miqdor ziyod, omborda {} bor".format(txt)
			except:
				message = "Bunday tovar qolmagan"
	
		else:
		    message = "Xatolik"	
	form = HistoryForm()
	context = {
	  'form':form,
	  'message':message,
	}
	return render(request, 'outwarehouse.html', context)
