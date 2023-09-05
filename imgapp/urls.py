from imgapp import views
from django.urls import path


urlpatterns = [
    path('',views.addstudent,name='addstudent'),
    path('student_details',views.student_details,name='student_details'),
    path('show_students',views.show_students,name='show_students'),

    path('editpage/<int:pk>',views.editpage,name='editpage'),
    
    path('edit_student_details/<int:pk>',views.edit_student_details,name='edit_student_details'),

    
    path('deletepage/<int:student_id>/', views.deletepage, name='deletepage'),
    
    
    path('student_profile_cards/', views.student_profile_cards, name='student_profile_cards'),
    path('student-profile/', views.student_profile_cards, name='student_profile_cards'),
   
    path('student-profile/<int:student_id>/', views.student_profile, name='student_profile'),

   
    

]