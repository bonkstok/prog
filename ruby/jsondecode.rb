#json
require 'json' 
def validateFile()
	test = false
	while test != true 
	begin 
		puts "enter file name: "
		file = File.read(gets.chomp+".json")
		return file
		test = true
	rescue 
		puts "File not found! try again!!"
	end
	end
end
puts "Enter output file name:"
file_open = File.new(gets.chomp+".json", "w")

data_hash = JSON.parse(validateFile())
#JSON.dump(data_hash, file_open)
data_hash.each {|value| file_open.write(value)} 




#other examples 
#data_hash.each {|key| puts "KEY : #{key}"}
#data_hash.each do |key|
#	file_open.write(key)
#end
#file = File.read('su444v1026.json')
