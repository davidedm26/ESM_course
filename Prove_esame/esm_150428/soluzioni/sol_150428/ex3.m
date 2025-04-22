clear all; close all; clc;

x = double(imread('mare.png'));
figure; subplot(2,2,1); imshow(x,[]); title('immagine originale');

[M,N] = size(x);

% punto 1
% Calcolo e visualizzazione della funzione di autocorrelazione
X = fft2(x);
R = real(ifft2(abs(X).^2));
[Nr,Nc] = size(R);
R = fftshift(R);
n = (1:Nc)-Nc/2-1;
m = (1:Nr)-Nr/2-1;
subplot(2,2,2); mesh(n,m,R); title('autocorrelazione');

% punto 2
% Individuzione del secondo picco della funzione di autocorrelazione
L = nlfilter(R, [5 5], @(x) max(x(:))) == R;
p = sort(R(L));
mappa = (R.*L == p(end-1));
[i,j] = find(mappa);
tn = n(j); tm = m(i);

% punto 3
T = [1 0 0; 0 1 0; tn(1) tm(1) 1];
tform = maketform('affine',T);
t = imtransform(x,tform,'Xdata',[1 Nr],'Ydata',[1 Nc]);
differenza = x-t;
mask=(differenza==0);
subplot(2,2,3); imshow(t,[]); title('immagine traslata');
subplot(2,2,4); imshow(mask); title('differenza');