clear all; close all; clc;

x = double(imread('rice.tif'));
[M N] = size(x);
xtilde = zeros(size(x));

%I STRATEGIA%
xtilde1(1,1) = x(1,1);
xtilde1(2:M,1) = x(1:M-1,1);
xtilde1(1,2:N) = x(1,1:N-1);
m = 2:M;
n = 2:N;
deltaR = abs(x(m-1,n) - x(m-1,n-1));
deltaC = abs(x(m,n-1) - x(m-1,n-1));
mask = deltaR < deltaC;
xtilde1(m,n) = mask.*x(m,n-1) + not(mask).*x(m-1,n);
e1 = xtilde1 - x;
figure(1);subplot(121);imshow(e1,[]);title('I strategia');
MSE_I = mean2(e1.^2)

%II STRATEGIA%
a = -1:0.1:1;
m = 2:M;
n = 2:N;
xtilde2(1,1) = x(1,1);
xtilde2(2:M,1) = x(1:M-1,1);
xtilde2(1,2:N) = x(1,1:N-1);
for i = 1:length(a);
   xtilde2(m,n) = a(i)*(x(m-1,n)+x(m,n-1)) + (1-2*a(i))*x(m-1,n-1);
   e2 = xtilde2 - x;
   MSE_tmp(i) = mean2(e2.^2);
end
[MSE_II index] = min(MSE_tmp);
MSE_II
xtilde2(m,n) = a(index)*(x(m-1,n)+x(m,n-1)) + (1-2*a(index))*x(m-1,n-1);
e2 = xtilde2 - x;
figure(1);subplot(122);imshow(e2,[]);title('II strategia');






