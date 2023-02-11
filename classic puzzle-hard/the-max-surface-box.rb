#https://www.codingame.com/training/hard/the-max-surface-box
#THE MAX SURFACE BOX
n = gets.to_i
if n==1
    puts "6 6"
    exit
end
#Maximum surface
max_surface=4*n+2
#Minimum surface
min_surface=max_surface
x,y,z=-1,-1,-1
for i in (1..(n**(1.0/3)+1).round())
    t=n
    if t%i==0
        t/=i;z=i
        for j in ((t**(1.0/2)).round()+1..1).step(-1)
            if t%j==0
                x=j;y=t/x;break
            end
        end
    end
    min_surface=[min_surface,2*(x*y+y*z+z*x)].min
end
puts [min_surface,max_surface]*" "
