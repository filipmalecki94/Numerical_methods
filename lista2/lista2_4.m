
function y = f(x)
	y = x/100*100-x;
endfunction

for n = 1:50
	printf(n)
	f(n)
end
