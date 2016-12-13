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

file_open = File.new("ok.json", "w")

file_open.write(JSON.pretty_generate(validateFile()))