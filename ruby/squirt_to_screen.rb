#json
require 'json' 
def validateFile()
	test = false
	while test != true 
	begin # try 
		puts "enter file name: "
		file = File.read(gets.chomp+".json")
		return file
		test = true
	rescue #catch if fail
		puts "File not found! try again!!"
	end
	end
end

data_hash = JSON.parse(validateFile())
#JSON.dump(data_hash, file_open)
data_hash.each {|value| puts value} 
