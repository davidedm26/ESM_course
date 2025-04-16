close all; clear; clc;

M = 380; N = 572; format = 'single';

fid = fopen('rumorosa.y','r'); 
y = fread(fid,[N, M],format).';
fclose(fid);

figure; imshow(y, [0 255]); title('immagine rumorosa');

z = filtra_freq(y);

fid = fopen('originale.y','r'); 
x = fread(fid,[N, M],format).';
fclose(fid);
figure; imshow(x,[0, 255]); title('immagine originale');

MSE  = mean2((x-z).^2);
PSNR = 10*log10(255^2/MSE)
