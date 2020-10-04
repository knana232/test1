def wthk_asme(D,S,P,F,E,T,u_D=1,u_S=1,u_P=1,u_T='degC'):
    #0.0 DEFINITIONS:
        #D : Outside Diameter, (m=1.00, [mm=0.001, in=0.0254])
        #S : SMYS, (Pa=1.00,[MPa, in])
        #P : Design Pressure, (Pa=1.00,[MPa, in])
        #F : Design Factor, (-)
        #E : Joint Factor, (-)
        #T : Temperature, (degC=1.00, [degF, K])
    #1.0 CONSTANTS:
    decimal = 3    
    #2.0 UNIT CONVERSION:
    D = u_D*D
    S = u_S*S
    P = u_P*P

    def T_degC(Temp, u_T):
        if u_T == 'degC':
            T = Temp
        elif u_T == 'degF':
            T = (Temp-32)*5/9
        elif u_T == 'K':
            T = Temp - 273.15
        else:
            T = Temp
        return T

    def Tdrating(Temp):
        from numpy import interp
        arr_T = [121,149,177,204,232]
        arr_FT = [1,0.967,0.933,0.900,0.867]
        if T<=0 :
            result = 1
        else:
            result = interp(T,arr_T,arr_FT)

        return result

    T = T_degC(T, u_T)
    FT = Tdrating(T)
    
    #3.0 CALCULATIONS:
    t = P*D/(2*S*F*E*FT)
    #4.0 RESULTS:
        #t : min. req. wall thickness, (div m=1.00, [mm=0.001, in=0.0254])

    
    return {
        'main':{
            'Wall thickness, t:':[
                str(round(t/0.001,decimal))+' mm',
                str(round(t/0.0254,decimal))+' in'
                ],
            'Outer diameter, D:':[
                str(round(D/0.001,decimal))+' mm',
                str(round(D/0.0254,decimal))+' in'
                ],

        },
        'info':{
            'Temperature, Tp:':[
                str(round(T,decimal))+' degC',
                str(round(T*9/5+32,decimal))+' degF'
            ],
            'Temperature de-rating, T:':[
                str(round(FT,decimal)),
                '-'
            ],
        }
    }

'''
    ans = {
        'm':round(t/1.00,decimal), 
        'mm':round(t/0.001,decimal),
        'in':round(t/0.0254,decimal),
        'TempD': round(FT,decimal),
    }
'''