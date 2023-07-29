#https://www.codingame.com/training/easy/reverse-fizzbuzz
#REVERSE FIZZBUZZ
n=gets.to_i
t=-1
a=[]
n.times{
    x=gets.chomp.split(/[a-z]+/)*""
    t=x.to_i-_1 if x=~/[0-9]+/
    a+=[x]
}
fn,bn,fb=-1,-1,-1
fc,bc,fbc=0,0,0
n.times{
    line=a[_1]
    if line=="F"&&fc<2
        fn=fn==-1? t+_1: t+_1-fn
        fc+=1
    elsif line=="B"&&bc<2
        bn=bn==-1? t+_1: t+_1-bn
        bc+=1
    elsif line=="FB"&&fbc<2
        fb=fb==-1? t+_1: t+_1-fb
        fbc+=1
    end
}
if fn==-1&&bn==-1&&fb>0
    fc=fb
    bc=fb
end
fn=1 if fn==0
bn=1 if bn==0
fn=fb if fn<0
bn=fb if bn<0
puts [fn,bn]*" "
