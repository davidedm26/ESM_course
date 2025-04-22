function y = colorbalancing(x);

x = x/255;
m = 1 - x(:,:,2);
x(:,:,2) = 1 - m.^(3.5);
y = x*255;
end
