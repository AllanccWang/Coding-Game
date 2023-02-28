#https://www.codingame.com/training/medium/longest-increasing-subsequence
#LONGEST INCREASING SUBSEQUENCE
m=[]
n=gets.to_i.times do
    m.append(gets.to_i)
end

a=[1]*n
for i in (0...n)
    for j in (i...n)
        if m[j]>m[i] && a[j]<a[i]+1
            a[j]=a[i]+1
        end
    end
end

puts a.max
