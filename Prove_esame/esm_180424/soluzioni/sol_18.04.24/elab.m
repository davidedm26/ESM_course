function y = elab(x)

a = [1 2 4; 128 0 8; 64 32 16];
mask = (x - x(2,2))>=0;     
b = a.*mask;
y = sum(b(:));


