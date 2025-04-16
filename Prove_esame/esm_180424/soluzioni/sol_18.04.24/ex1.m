close all; clear; clc;

x = imread('test.png');
figure; imshow(x, [0 255]); title('immagine originale');
x = double(x);

[M N] = size(x);
y = x + 30*randn(M,N);
figure; imshow(y, [0 255]); title('immagine rumorosa');

% strategia 1
z = filtro_dir(y);
MSE1  = mean2((x-z).^2)
figure; imshow(z, [0 255]); title('immagine filtrata, strategia 1');

% strategia 2
z = filtro_dir2(x,y);
MSE2  = mean2((x-z).^2)
figure; imshow(z, [0 255]); title('immagine filtrata, strategia 2');

% strategia 3
xhat = imfilter(y,ones(3)/9,'symmetric');
z = filtro_dir2(xhat,y);
MSE3  = mean2((x-z).^2)
figure; imshow(z, [0 255]); title('immagine filtrata, strategia 3');

