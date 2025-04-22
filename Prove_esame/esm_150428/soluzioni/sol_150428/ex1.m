% esercizio 1
clear all; close all; clc;
x1 = double(imread('disk1.gif'));
x2 = double(imread('disk2.gif'));

%punto 1
h  = [0 1 0; 1 -4 1; 0 1 0];
y1 = imfilter(x1,h,'symmetric').^2;
y2 = imfilter(x2,h,'symmetric').^2;

%punto 2
y1m = colfilt(y1,[5 5],'sliding',@mean);
y2m = colfilt(y2,[5 5],'sliding',@mean);
y1s = colfilt(y1,[5 5],'sliding',@std);
y2s = colfilt(y2,[5 5],'sliding',@std);
a1  = y1m.*(y1s.^2);
a2  = y2m.*(y2s.^2);

%punto 3 
a1 = a1./(a1+a2+eps);
a2 = 1-a1;

%punto 4
xf = a1.*x1+a2.*x2;

%show
figure(1);
subplot(2,3,  1  ); imshow(x1, [0 255]); title('x_1');
subplot(2,3,  2  ); imshow(x2, [0 255]); title('x_2');
subplot(2,3,[3,6]); imshow(xf, [0 255]); title('x_f = \alpha_1 \cdot x_1 + \alpha_2 \cdot x_2');
subplot(2,3,  4  ); imshow(a1, [0   1]); title('\alpha_1');
subplot(2,3,  5  ); imshow(a2, [0   1]); title('\alpha_2');
