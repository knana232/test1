from django.shortcuts import render
from .forms import cal_wthkForm

info = {
    'Name': 'John Smith',
    'Age': 23,
    'Single': True,
}
'''
def wthk_asme(D,S,P,F,E):
    t = P*D/(2*S*F*E)
    return t
'''
def index(request):
    return render(request,'webapp/index.html',info)

def about(request):
    return render(request,'webapp/about.html')

def cal_wallthickness(request):
    if request.method == 'POST':
        form = cal_wthkForm(request.POST)
        if form.is_valid():
            from .calculation.wthk import wthk_asme
            D = float(request.POST['value_D'])
            S = float(request.POST['value_S'])
            P = float(request.POST['value_P'])
            F = float(request.POST['value_F'])
            E = float(request.POST['value_E'])
            T = float(request.POST['value_T'])
            u_D = float(request.POST['unit_D'])
            u_S = float(request.POST['unit_S'])
            u_P = float(request.POST['unit_P'])
            u_T = request.POST['unit_T']
            #print('U_S = ',u_S)
            #print('U_P = ',u_P)
            print('U_T = ',u_T)
            result = wthk_asme(D,S,P,F,E,T,u_D,u_S,u_P,u_T)
            
    else:
        form = cal_wthkForm()
        result = ''
    print('result = ',result)
    context = {'FORM':form,'RESULT':result}   
    return render(request,'webapp/cal_wallthickness.html',context)