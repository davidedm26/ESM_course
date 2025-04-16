function y = filtro_dir(x)

y = nlfilter(x,[9 9],@calcola);

