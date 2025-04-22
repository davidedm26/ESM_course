function y = denoise(x, mappa)

% immagini filtrate con finestre di dimensioni diverse
y3 = imfilter(x,ones(3)/9,'symmetric');
y9 = imfilter(x,ones(9)/81,'symmetric');

y = y3.*mappa + y9.*(1-mappa);

