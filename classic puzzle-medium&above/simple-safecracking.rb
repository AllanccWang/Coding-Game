#https://www.codingame.com/training/hard/simple-safecracking
#SIMPLE SAFECRACKING
msg = gets.chomp.split(": ")
d={'0'=>' 2 8','1'=>'8122','2'=>'0 8','3'=>'01 22','4'=>'58  ',
'5'=>'511 2','6'=>'311 ','7'=>'32 212','8'=>'211 10','9'=>'1211122'}
m=msg[0].downcase.split.join
pw=''
decode=msg[1].split("-").each{|x|
    s=x.chars.map{|c| m.include?(c)? m.index(c).to_s : ' '}.reduce(&:+)
    for notes in d.keys
        if d[notes]==s
            pw+=notes
        end
    end
}
print pw
