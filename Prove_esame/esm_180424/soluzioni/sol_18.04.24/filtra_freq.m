function z = filtra_freq(y);

[M N] = size(y);
YF=fft2(y);
YF=fftshift(YF);
figure; imshow(log(1+abs(YF)), []); title('FFT dell''immagine rumorosa');

du = 1/M; dv = 1/N;
m = -1/2:du:1/2-du;
n = -1/2:dv:1/2-dv;
[k,l] = meshgrid(n,m);
figure; mesh(k,l,log(1+abs(YF))); title('rappresentazione 3D');

D0 = 0.007;
D  = sqrt(l.^2 + (k+0.1).^2);
H1 = (D <= D0);
D  = sqrt(l.^2 + (k-0.1).^2);
H2 = (D <= D0);
H=1-H1-H2;
figure; imshow(H,[]); title('filtro in frequenza');

Z = YF.*H;
figure; imshow(log(1+abs(Z)),[]); title('FFT dell''immagine filtrata');

z = real(ifft2(ifftshift(Z)));
figure; imshow(z,[0, 255]); title('immagine filtrata');
