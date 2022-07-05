from django.shortcuts import render,redirect 
from .forms import UserUpdateForm,ProfileUpdateForm
from .models import Profile
from rest_framework import APIView
from django.contrib import messages
from .serializers import ProfileSerializer
from rest_framework import generics,status


class Profile(generics.RetrieveUpdateDestroyAPIView):
    model = Profile
    serializer_class = ProfileSerializer
    def get_object(self):
        
        return self.request.user
    
    # def profile(request):
    #  if request.method == 'POST':
    #     u_form = UserUpdateForm(request.POST,instance=request.user)
    #     p_form = ProfileUpdateForm(request.POST, request.FILES,instance= request.user.profile)
        
    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, f'Your account has been updated!')
    #         return redirect('profile')
        
    #  else:
    #      u_form = UserUpdateForm(instance=request.user)
    #      p_form = ProfileUpdateForm(instance= request.user.profile)
        
    #  context = {
    #     'u_form': u_form,
    #     'p_form': p_form,
    # }
    #  return render (request)
 