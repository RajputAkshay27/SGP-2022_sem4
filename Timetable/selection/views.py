from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from .models import faculty, subject, priority
import xlwt
from Login.views import is_TTcommitte
# Create your views here.

def selection(request):
    name = request.user.first_name
    facultyCode = faculty.objects.all()
    subs = subject.objects.all()
    if request.method == "POST":
        semester = request.POST['sem_value'] 
        sp1 = request.POST['subSelect1']
        sp2 = request.POST['subSelect2']
        sp3 = request.POST['subSelect3']
        pp1 = request.POST['pracSelect1']
        pp2 = request.POST['pracSelect2']
        pp3 = request.POST['pracSelect3']

        
        temp = request.POST['Faculty_code_value']
        f_code = faculty.objects.get(fac_code = temp)
    
        
        
        data = priority()
        data.semester = semester
        data.fac_code = f_code
        data.Theory_Priority1 = sp1
        data.Theory_Priority2 = sp2
        data.Theory_Priority3 = sp3
        data.Practical_Priority1 = pp1
        data.Practical_Priority2 = pp2
        data.Practical_Priority3 = pp3
        
        try: 
            data.save()
            str = "Data has been saved successfully"
        except:
            str ='some error occured'
        
        if is_TTcommitte(request.user):
            return render (request, 'selection/selection.html',{"name":name,"subs":subs,'fac':facultyCode,'str':str})
        else:
            return render (request, 'selection/n_select.html',{"name":name,"subs":subs,'fac':facultyCode,'str':str})
        
    else:
        if is_TTcommitte(request.user):
            return render (request, 'selection/selection.html',{"name":name,"subs":subs,'fac':facultyCode})
        else:
            return render (request, 'selection/n_select.html',{"name":name,"subs":subs,'fac':facultyCode})

def exportExcel(request):
    if is_TTcommitte(request.user):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['semester', 'Faculty code', 'Theory Priority1', 'Practical Priority1',
                'Theory Priority2', 'Practical Priority2','Theory Priority2', 'Practical Priority2']
        
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        
        rows = priority.objects.all().values_list('semester', 'fac_code', 'Theory_Priority1', 'Practical_Priority1',
                'Theory_Priority2', 'Practical_Priority2','Theory_Priority2', 'Practical_Priority2')
        
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        
        wb.save(response)

        return response
    else:
        return HttpResponseForbidden("You don't have privelge.")