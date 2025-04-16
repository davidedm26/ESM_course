close all; clear all; clc;

x(:,:,1) = double(rgb2gray(imread('I1.png')));
x(:,:,2) = double(rgb2gray(imread('I2.png')));

for i=1:2,
    
    h = [-1 2 -1; 2 -4 2; -1 2 -1];
    y = imfilter(x(:,:,i),h,'symmetric');
    
    z = nlfilter(y,[3 3],@elab);
    
    h = hist(z(:),0:255);
    s = std(h);
    B(i) = (s > 495);
    
    if B(i)==1 
        fprintf('Immagine I%d è vera \n',i);
    else
        fprintf('Immagine I%d è falsa \n',i);
    end
end

