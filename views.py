from django.shortcuts import render
from django.contrib.auth.models import User,auth




def register(request):

	if request.method=='POST':
		USER NAME=request.POST['USERNAME']
		PASSWORD=request.POST['PASSWORD']
		FIRST NAME=request.POST['FIRSTNAME']
		LAST NAME=request.POST['LASTNAME']
		EMAIL ADDRESS=request.POST['EMAILADDRESS']
		CONTACT NO=request.POST['CONTACTNO']

		user=User.objects.create_user(USERNAME=USERNAME,PASSWORD=PASSWORD,EMAILADDRESS=EMAILADDRESS,FIRSTNAME=FIRSTNAME,LASTNAME=LASTNAME,CONTACTNO=CONTACTNO)
		user.save();
		print('user created')
		return redirect('/')
else: 
		return render(request,'up.html')