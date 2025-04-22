clear; close all; clc;

% Lettura immagine
x = double(rgb2gray(imread('volto.png')));
[M,N] = size(x);

y = filtra(x);

% Visualizzazione
figure;
subplot(121);imshow(x,[]);title('Originale');
subplot(122);imshow(y,[]);title('Filtrata');
