function mappa = classify(x);

% prefiltraggio
g = fspecial('gaussian', 5, 1.2);
xf = imfilter(x, g, 'symmetric');

% Calcolo i coefficienti di variazione locali
MED = colfilt(xf,[9 9],'sliding',@mean);
STD = colfilt(xf,[9 9],'sliding',@std);
C = STD./MED;

% Calcolo la mappa
mappa = C > 0.07;

% Effettuo le operazioni morfologiche
mappa = imerode(mappa, strel('square',3));
mappa = imclose(mappa, strel('disk',3));

figure; imshow(mappa,[]); title('mappa di classificazione');