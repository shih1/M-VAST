red = [255 0 0];
green = [0 255 0];
blue  = [0 0 255];
yellow =  [255 255 0];
black = [0 0 0];
white = [255 255 255];

I = imread('acheck_bw_hq_1.png');
imshow(I);

n_row = 1200;
n_col = 1600;

for i = 1:n_row
    for j = 1:n_col

        if I(i,j,:) == 0
            I2(i,j,:) = blue;
        else
            I2(i,j,:) = yellow;
        end
    end
end

figure()
imshow(I2)


imwrite(I2,'acheck_by_hq_1.png')
