#https://www.codingame.com/training/medium/quaternion-multiplication
#QUATERNION MULTIPLICATION
'''
The quaternions belong to a number system that extends the complex numbers. A quaternion is defined by the sum of scalar multiples of the constants i,j,k and 1.
More information is available at http://mathworld.wolfram.com/Quaternion.html

Consider the following properties:
jk = i
ki = j
ij = k
i² = j² = k² = -1

These properties also imply that:
kj = -i
ik = -j
ji = -k

The order of multiplication is important.

Your program must output the result of the product of a number of bracketed simplified quaternions.

Pay attention to the formatting
The coefficient is appended to the left of the constant.
If a coefficient is 1 or -1, dont include the 1 symbol.
If a coefficient or scalar term is 0, dont include it.
The terms must be displayed in order: ai + bj + ck + d.

Example Multiplication
(2i+2j)(j+1) = (2ij+2i+2j² +2j) = (2k+2i-2+2j) = (2i+2j+2k-2)
'''
q=[]
#convert (2i+2j+2k-2) to [2,2,2,-2]
gets.chomp.scan(/\((.*?)\)/){|x|
    f=x[0].scan(/(?=.)(\+|-|)([\d.]*)(\w?)/)
    s=[0,0,0,0]
    f.each{|y|
        n=y[1]=="" ? "1":y[1]
        s[0]=(y[0]+n).to_i if y.include?("i")
        s[1]=(y[0]+n).to_i if y.include?("j")
        s[2]=(y[0]+n).to_i if y.include?("k")
        s[3]=(y[0]+n).to_i if ""==y[-1]
    }
    q+=[s]
}
#counter/clockwise [i,j,k] rules
clk_wise=[[1,2],[2,0],[0,1]]
anti_clk=[[2,1],[1,0],[0,2]]
a=q[0]
(1...q.size).each{|idx|
    l=[0,0,0,0]
    for i in (0...4)
        for j in (0...4)
            if anti_clk.include?([i,j])
                l[3-[j,i].sum]+=-a[i]*q[idx][j]
            elsif clk_wise.include?([i,j])
                l[3-[j,i].sum]+=a[i]*q[idx][j]
            elsif [[0,0],[1,1],[2,2],[3,3]].include?([i,j])
                l[3]+=(i==3?1:-1)*a[i]*q[idx][j]
            # [i,j,k] product with a number
            elsif [[0,3],[1,3],[2,3]].include?([i,j])
                l[i]+=a[i]*q[idx][j]
            elsif [[3,0],[3,1],[3,2]].include?([i,j])
                l[j]+=a[i]*q[idx][j]
            end
        end
    end
    a=l
}
#format output string
ans=""
if a[0]!=0
    if a[0].abs!=1
        ans+=(a[0]<0?a[0].to_s: "#{a[0]}")+"i"
    else
        ans+=(a[0]<0?"-":"")+"i"
    end
end
if a[1]!=0
    if a[1].abs!=1
        ans+=(a[1]<0?a[1].to_s: "+#{a[1]}")+"j"
    else
        ans+=(a[1]<0?"-":"+")+"j"
    end
end
if a[2]!=0
    if a[2].abs!=1
        ans+=(a[2]<0?a[2].to_s: "+#{a[2]}")+"k"
    else
        ans+=(a[2]<0?"-":"+")+"k"
    end
end
if a[3]!=0
    if a[3].abs!=1
        ans+=a[3]<0?a[3].to_s: "+#{a[3]}"
    else
        ans+=a[3]<0?"-1":"+1"
    end
end
puts ans
