
n = 50; %n pixels
p = 12;%p rows 
q = 16;%q columns 

red = [255 0 0];
green = [0 255 0];
blue  = [0 0 255];
yellow =  [255 255 0];


I = checkerboard(n,p,q)<0.5;
imshow(I);

imwrite(imcomplement(I),'checker_bw_.png')

I2 = zeros(2*n*p, 2*n*q,3);

n_row = 1200;
n_col = 1600;

for i = 1:n_row
    for j = 1:n_col

        if I(i,j) == 0
            I2(i,j,:) = red;
        else
            I2(i,j,:) = green;
        end
    end
end

   
imshow(I2)
imwrite(I2,'checker_rg_.png');

I3 = zeros(2*n*p, 2*n*q,3);


for i = 1:n_row
    for j = 1:n_col

        if I(i,j) == 0
            I3(i,j,:) = blue;
        else
            I3(i,j,:) = yellow;
        end
    end
end

imshow(I3)
imwrite(I3,'checker_by_.png');


