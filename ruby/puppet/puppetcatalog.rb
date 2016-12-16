require 'json'


def parseJson(json_file)
	read_file = File.read(json_file)
	return JSON.parse(read_file)
end

def createNewFile()
	puts "Name of new file:"
	new_file = File.new(gets.chomp+".json", "w")
	return new_file end

def readFile(to_read)
	return File.read(to_read) end

def writeToFile(data_write, output_file = false)
	if output_file == false
		output_file = createNewFile()
		output_file.puts(data_write)
	else 
		output_file.puts(data_write) end	
end

def getKeys(json_input)
	return json_input.keys 
end

def writeParametersToFile(json_data, to_file = false)
	i = 0
	hsh = {}
	write_to =  to_file #createNewFile()	#to_file != false ? (createNewFile()) : false
	for i in i...json_data['resources'].length
		#json_data['resources'][i].each {|key, value| puts value}
		json_data['resources'][i].each {|key, value| hsh[key] = value}
		hsh.each do |key,value|
			if key == 'parameters'
				if to_file != false
					value.each do |keyp,valuep|
						writeToFile("#{key} :: #{keyp} : #{valuep}", write_to) end
				else 
					puts "found parameters!"end 
			else 
				puts "nothing found"end
end end end

def findStringToFile(json_data,to_file = false)
	puts "Enter regex to use"
	regex = gets.chomp
	if regex != "" && regex != nil
		puts "input_to"
		input_to = createNewFile()
		puts "output to"
		output_to = createNewFile()
		writeParametersToFile(json_data, input_to)
		output_parameters = File.read(input_to)

		output_parameters.each_line do |line|
			if line =~ /#{regex}/
				#writeToFile(line, output_to) end end
				output_to.puts(line) end end
	else 
		puts "Whats the need for this method, if you dont supply a regex..?" end
end

puts "Enter name of json file you wish to use:"
begin
json_data = parseJson(gets.chomp+'.json')
rescue
	puts "File not found.. BYE"
	exit
end
#(pass|password)
#puts "Enter regex to use:"
findStringToFile(json_data)
