function z = filtra(y,mask,index);

temp = y.*mask(:,:,index);
z = mean2(temp(temp>0));
