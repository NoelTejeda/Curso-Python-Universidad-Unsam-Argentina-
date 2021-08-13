saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61 #¿Para qué es esto?
pago_extra_mes_fin = 108     #¿Para qué es esto?
pago_extra = 1000

while saldo > 0:
    pago_mensual = 2684.11
    mes = mes + 1
    if mes <= 60:                    
       pago_mensual = pago_mensual + pago_extra_mes_comienzo #Le saqué los 1000 de los primeros 12 meses y agregué pago_extra_comienzo
    elif mes > 60 and mes < 109:
        pago_mensual = pago_mensual + pago_extra
    else:
       pago_mensual = pago_mensual + pago_extra_mes_fin      #No sabía como usarla así que la puse acá...
    if saldo > pago_mensual:
        saldo = saldo * (1+tasa/12) - pago_mensual
    else:
        saldo = round(saldo * (1+tasa/12), 2)
        pago_mensual = saldo
        saldo = saldo - pago_mensual
    total_pagado = total_pagado + pago_mensual
    print(mes, pago_mensual, round(total_pagado, 2), round(saldo, 2))
print('Total pagado', round(total_pagado, 2))
print("Meses:", mes)