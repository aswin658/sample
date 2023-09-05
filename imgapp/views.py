
from django.shortcuts import render,redirect,get_object_or_404
from imgapp.models import studentdetails



# Create your views here.

def addstudent(request):
    return render(request,'studentinfo.html')

def student_details(request):
    if request.method=='POST':
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        phone_number=request.POST['phone_number']
        email=request.POST['email']
        course=request.POST['course']
        address=request.POST['address']
        image=request.FILES.get('file')
        
        
        student=studentdetails(first_name=fname,
                               last_name=lname,
                               phone_number=phone_number,
                               email=email,
                               course=course,
                               address=address,
                               image=image,
                               )
        
        student.save()
        print("save data")
        return redirect('show_students')
    

def show_students(request):
    students=studentdetails.objects.all()
    return render(request,'show.html',{'students':students})

def student_profile_cards(request):
    students = studentdetails.objects.all()
    return render(request, 'student_profile_cards.html', {'student': students})


#Load Edit Page....
def editpage(request,pk):
    students=studentdetails.objects.get(id=pk) #.....select * from tablename where id = 7;
    return render(request,'edit.html',{'students':students})

#Editing..
def edit_student_details(request,pk):
    if request.method=='POST':
        students = studentdetails.objects.get(id=pk)
        old=students.image
        new=request.FILES.get('file')
        if old != None and new == None:
            students.image=old
        else:
            students.image=new    
        
        students.first_name = request.POST.get('first_name')
        students.last_name = request.POST.get('last_name')
        students.phone_number = request.POST.get('phone_number')
        students.email = request.POST.get('email')
        students.course = request.POST.get('course')
        students.address = request.POST.get('address')
        
        if 'remove_image' in request.POST:
            # Delete the current image file from storage
            students.image.delete()
            
            # Set the image field to the default image's URL
            students.image = 'static/images/default.jpg'  # Update with the correct path
        
        students.save()
        return redirect('show_students' )
    return render(request, 'edit.html')

def deletepage(request, student_id):
    student = get_object_or_404(studentdetails, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('show_students')
    return render(request, 'delete_confirmation.html', {'student': student})



def student_profile(request, student_id):
    student = get_object_or_404(studentdetails, id=student_id)
    return render(request, 'student_profile_cards.html', {'student': student})


    
    



