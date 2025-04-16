function index = identifica_maschera(y,mask)

for i = 1:8
    ym = y(mask(:,:,i)>0);
    varianza(i) = var(ym);
end;

[minimo_varianza, index] = min(varianza);