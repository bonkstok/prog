#json
require 'json' 
def validateFile()
	test = false
	while test != true 
	begin 
		puts "enter file name: "
		file = File.read(gets.chomp+".json")
		test = false
		return file
		continue
		
	rescue 
		puts "File not found! try again!!"
	end
	end
end



#file = File.read('su444v1026.json')
data_hash = JSON.parse(validateFile())
data_hash.each {|value| puts value} 


#file = File.read('su444v1026.json')
