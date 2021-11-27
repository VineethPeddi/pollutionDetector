from django.shortcuts import render
from myprojectapp.models import AQIPrediction
from django import forms
from myprojectapp.miniproject import home
# Create your views here.
'''def index(request):
	return render(request,'index.html')'''
def mappage(request):
    return render(request,'website.html')
class AQIForm(forms.ModelForm):
	class Meta:
		model=AQIPrediction
		fields='__all__'


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AQIForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            t=form.cleaned_data['Average_Temperature']
            tm1=form.cleaned_data['Maximum_Temperature']
            tm=form.cleaned_data['Minimum_Temperature']
            slp=form.cleaned_data['Atmospheric_Pressure']
            h=form.cleaned_data['Average_Humidity']
            vv=form.cleaned_data['Average_Visibility']
            v=form.cleaned_data['Average_Wind_Speed']
            vm=form.cleaned_data['Maximum_Wind_Speed']	
            result=home(t,tm1,tm,slp,h,vv,v,vm)
            #result=home(1,2,2,3,4,5,6)
            str=""
            if result>0 and result<50:
                str="Value indicates it is Good"
                return render(request, 'index.html', {'form': form,'result':result,'str':str})
            elif result>51 and result<100:
                str="Value indicates it is Moderate"
                return render(request, 'index.html', {'form': form,'result':result,'str':str})
            elif result>101 and result<150:
                str="Value indicates it is Unhealthy for sensitive groups"
                return render(request, 'index.html', {'form': form,'result':result,'str':str})
            elif result>151 and result<200:
                str=" Value indicates it is Unhealthy"
                return render(request, 'index.html', {'form': form,'result':result,'str':str})
            elif result>201 and result<300:
                str="Value indicates it is very unhealthy"
                return render(request, 'index.html', {'form': form,'result':result,'str':str})
            else:
                str="Value indicates it is Hazardous"
                return render(request, 'index.html', {'form': form,'result':result,'str':str}) 

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AQIForm()

    return render(request, 'index.html', {'form': form})