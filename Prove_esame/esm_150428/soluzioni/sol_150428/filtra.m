function y = filtra(x);

[M,N] = size(x);
du = 1/M; dv = 1/N;
m = -1/2:du:1/2-du;
n = -1/2:dv:1/2-dv;
[l,k] = meshgrid(n,m);
X = fftshift(fft2(x,M,N));
figure; subplot(121); imagesc(log(1+abs(X))); axis image; 

H(:,:,1) = 1 - (l>-.40 & l<-.30 & k>-.03 & k< .03);
H(:,:,2) = 1 - (l>-.20 & l<-.10 & k>-.03 & k< .03);
H(:,:,3) = 1 - (l> .10 & l< .20 & k>-.03 & k< .03);
H(:,:,4) = 1 - (l> .30 & l< .40 & k>-.03 & k< .03);

H(:,:,5) = 1 - (l>-.01 & l< .01 & k> .30 & k< .40);
H(:,:,6) = 1 - (l>-.01 & l< .01 & k> .10 & k< .20);
H(:,:,7) = 1 - (l>-.01 & l< .01 & k>-.20 & k<-.10);
H(:,:,8) = 1 - (l>-.01 & l< .01 & k>-.40 & k<-.30);
G = ones(size(X));

for i=1:8,
   G = G.*H(:,:,i);
end;

Y = X.*G;
subplot(122); imagesc(log(1+abs(Y))); colormap(gray); axis image; 

% Ricostruzione
y = real(ifft2(ifftshift(Y)));

% Valutazione bontà del filtraggio
rmin = .1;
rmax = .4;
F = ((k.^2+l.^2) > rmin^2).*((k.^2+l.^2) < rmax^2);
EX = sum(sum(F.*(abs(X)).^2));
EY = sum(sum(F.*(abs(Y)).^2));
DE = 100*(1-EY/EX)
