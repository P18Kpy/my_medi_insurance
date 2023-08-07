
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from .forms import predict
import joblib



def home(request):
    model = joblib.load('insurance_model.sav')
    if request.method == 'POST':
        form = predict(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            bmi = form.cleaned_data['bmi']
            children = form.cleaned_data['children']
            smoker = int(form.cleaned_data['smoker'])
            sex = int(form.cleaned_data['sex'])
            region = int(form.cleaned_data['region'])

            result = model.predict([[age, bmi, sex, children, smoker, region]])
            print("----------------------------------------------","successful")
            return render(request, "home.html", {"output": result})
        else:
            
            print("--------------------------","error")
            for error in form.errors:
                print("---",error)
            return render(request, "home.html", {'form': form})
    else:
        form = predict()
        return render(request, "home.html", {'form': form})
    
    """# your_app_name/views.py
from django.shortcuts import render
from django.http import JsonResponse
import joblib

def predict_insurance_cost(request):
    # Load the trained medical insurance prediction model (replace 'path_to_model_file' with the actual path to your saved model file)
    model = joblib.load('path_to_model_file')

    if request.method == 'POST':
        # Get the input data for prediction from the user (assuming the input is a JSON object with keys for the six characteristics)
        input_data = {
            'characteristic1': request.POST.get('characteristic1'),
            'characteristic2': request.POST.get('characteristic2'),
            'characteristic3': request.POST.get('characteristic3'),
            'characteristic4': request.POST.get('characteristic4'),
            'characteristic5': request.POST.get('characteristic5'),
            'characteristic6': request.POST.get('characteristic6'),
        }

        # Perform any necessary data preprocessing on input_data

        # Make predictions using the loaded model
        prediction = model.predict([list(input_data.values())])

        # Return the prediction as a JSON response
        return JsonResponse({'prediction': prediction[0]})

    return render(request, 'your_template.html')  # Replace 'your_template.html' with your actual template file

                        print(request.POST)
                    form=predict(request.POST)
                    forms=predict()
                    if form.is_valid():
                        age=form.cleaned_data['age']
                        
                        bmi=form.cleaned_data['bmi']
                        children=form.cleaned_data['children']
                        smoker = form.cleaned_data['smoker']
            
                        region =form.cleaned_data['region']   """