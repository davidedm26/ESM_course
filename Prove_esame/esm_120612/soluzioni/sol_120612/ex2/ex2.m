% EX. 1
clear; clc; close all;

% Carico l'immagine rumorosa
fid = fopen('mixed_noisy.y', 'r');
noisy = fread(fid, [256 256], 'float').';
fclose(fid);

% Effettuo la classificazione
map = classify(noisy);

% Denoising
filt = denoise(noisy, map);
filt_media = imfilter(noisy, ones(5,5)/25, 'symmetric');

% Carico l'immagine pulita
fid = fopen('mixed.y', 'r');
clean = fread(fid, [256 256], 'uint8').';
fclose(fid);

% Calcolo MSE globale
mse = mean2((clean-filt).^2);
PSNR1 = 10*log10(255^2/mse)
mse_media = mean2((clean-filt_media).^2);
PSNR2 = 10*log10(255^2/mse_media)

% Calcolo MSE locale
mse_omog = mean2((clean(not(map))-filt(not(map))).^2);
PSNR1_omog = 10*log10(255^2/mse_omog)
mse_not_omog = mean2((clean(map)-filt(map)).^2);
PSNR2_not_omog = 10*log10(255^2/mse_not_omog)

mse_omog_media = mean2((clean(not(map))-filt_media(not(map))).^2);
PSNR1_omog_media = 10*log10(255^2/mse_omog)
mse_not_omog_media = mean2((clean(map)-filt_media(map)).^2);
PSNR2_not_omog_media = 10*log10(255^2/mse_not_omog_media)

% Visualizzo i risultati
figure; subplot(1,3,1); imshow(clean,[0 255]); title('immagine originale');
subplot(1,3,2); imshow(filt,[0 255]); title('Filtro adattativo');
subplot(1,3,3); imshow(filt_media,[0 255]); title('Filtro media 5x5');
