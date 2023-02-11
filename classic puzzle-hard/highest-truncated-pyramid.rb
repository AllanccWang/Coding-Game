#https://www.codingame.com/training/hard/highest-truncated-pyramid
#HIGHEST TRUNCATED PYRAMID
n=gets.to_i
h,w=-1,-1
for i in (1..n+1)
    a=i*(i+1)/2
    f=false
    for j in (0..i+1)
        b=j*(j+1)/2
        if a-b==n
            h,w=i,j+1;f=true;break
        end
    end
    if f
        break
    end
end
for i in (w..h)
    puts "*"*i
end
