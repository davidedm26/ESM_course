function z = calcola(y,mask);

% definizione delle maschere
mask(:,:,1) = [ones(5,9); zeros(4,9)];
mask(:,:,2) = mask(:,:,1)';
mask(:,:,3) = flipud(mask(:,:,1));
mask(:,:,4) = fliplr(mask(:,:,2));
mask(:,:,5) = [1 zeros(1,8); ones(1,2) zeros(1,7); ones(1,3) zeros(1,6); ones(1,4) zeros(1,5); ones(1,5) zeros(1,4); ones(1,6) zeros(1,3); ones(1,7) zeros(1,2); ones(1,8) 0; ones(1,9)];
mask(:,:,6) = mask(:,:,5)';
mask(:,:,7) = flipud(mask(:,:,5));
mask(:,:,8) = flipud(mask(:,:,6));

% identificazione della maschera
for i = 1:8
    ym = y(mask(:,:,i)>0);
    varianza(i) = var(ym);
end;
[minimo_varianza, index] = min(varianza);

% filtraggio
z = mean(y(mask(:,:,index)>0));