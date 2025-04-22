close all; clear all; clc;
x = imread('viola.jpg');
subplot(1,3,1); imshow(x); title('troppo magenta');

% color balancing
x = double(x);
y = colorbalancing(x);
subplot(1,3,2); imshow(uint8(y)); title('immagine elaborata');

w = imread('viola_originale.jpg');
subplot(1,3,3); imshow(w); title('immagine originale');
mse = mean2((double(w)-y).^2)
% l'MSE e' piu' basso se lavorate con i dati normalizzati

% segmentazione nello spazio HSV 
HSV = rgb2hsv(y);
V = HSV(:,:,3);
mask = V<=45;
figure; imshow(mask,[]); title('mappa di segmentazione');

% equalizzazione del solo sfondo nello spazio HSV
sfondo = V.*mask;
L = sum(mask(:));               % ~n.ro pixel dello sfondo
p = hist(sfondo(:), [0:max(sfondo(:))])/L;  
cdf = cumsum(p);              
y = cdf(uint8(sfondo)+1);    
z = 127*(y-min(y(:)))/(max(y(:))-min(y(:))); % fshs intervallo [0,127]
h = fspecial('gaussian',12,2);
z = imfilter(z,h,'symmetric');   % filtraggio
HSV(:,:,3) = z.*mask + V.*(1-mask);
xeq = hsv2rgb(HSV);
figure; imshow(uint8(xeq)); title('immagine equalizzata localmente')