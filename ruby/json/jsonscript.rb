require 'json'

def printMenu()
	hsh = {
		1 => "Write parameters to file",
		2 => "Find string and write to file",
		3 => "Hash or Array inside?",
		4 => "Write value of all keys to a file",
		5 => "exit",
		}	
		hsh.each {|k,v| puts "#{k}: #{v}"}
		begin 
			puts "enter number"
			keuze = gets.chomp
			return keuze.to_i
		rescue 
			puts "Please enter a number." end
end

def parseJson(json_file)
	begin
		read_file = File.read(json_file)
		return JSON.parse(read_file)
	rescue
		puts "file not found! EXIT"
		exit end
end

def createNewFile(input=false)
	if input == false
		puts "Name of new file:"
		new_file = File.new("output/" + gets.chomp+".json", "w")
		return new_file 
	else
		new_file = File.new("output/" + input+".json", "w")
		return new_file end		
	end

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

def writeParametersToFile(json_data = false, to_file = false)
	i = 0
	hsh = {}
	if json_data == false
		puts "Enter name of json file:"
		json_data = parseJson(gets.chomp+".json")  end
	if to_file == false
		to_file =  createNewFile() end	#to_file #createNewFile()	#to_file != false ? (createNewFile()) : false
	i = 0
	hsh = {}
	for i in i...json_data['resources'].length
		#json_data['resources'][i].each {|key, value| puts value}
		json_data['resources'][i].each {|key, value| hsh[key] = value}
		hsh.each do |key,value|
			if key == 'parameters'
				if to_file != false
					value.each do |keyp,valuep|
						writeToFile("#{key} :: #{keyp} : #{valuep}", to_file) end
				else 
					next end#puts "found parameters!"end 
			else 
				next end end end#puts "nothing found" end end end

end

def findStringToFile(json_data = false,to_file = false)
#this method finds a string in a file
	if json_data == false
		puts "Enter name of json file:"
		json_data = parseJson(gets.chomp+".json") end

	puts "Enter regex to use"
	regex = gets.chomp
	if regex != "" && regex != nil # makes sure regex is not empty or nil
		puts "input_to"
		input_to = createNewFile()
		puts "output to"
		output_to = createNewFile()
		writeParametersToFile(json_data, input_to) # sends file name to method
		output_parameters = File.read(input_to) # read the file that has been filled by writeParametersToFile()

		output_parameters.each_line do |line|     
			begin
			if line == "" || line == nil 
				next
			elsif line =~ /#{regex}/ #search in every line for regex
				#writeToFile(line, output_to) end end
					output_to.puts(line) end  
			rescue 
				puts "error, encoding!" end end
	else 
		puts "Whats the need for this method, if you dont supply a regex..?" end
end

def arrayOrHash (arr_or_hash)
	arr_or_hash = parseJson(arr_or_hash)	
	puts getKeys(arr_or_hash)
	#arr_or_hash.each {|key,value| puts "#{key} is of class #{key.class}"}
	puts arr_or_hash.class
	puts "For which key would you like to know the inside?"
	key_to_search = gets.chomp
	arr_or_hash = key_to_search != "" ?  arr_or_hash[key_to_search] : arr_or_hash
	i = 0
	if arr_or_hash.class == Hash   
		i = 0
		arr_or_hash.each do |key,value|   # since hashes work with key => value we need to make sure we dont access them by index #
			
			if arr_or_hash[key].class == Hash
				puts "Key #{i} #{key}\t=---> is a HASH!"
				i += 1
			elsif arr_or_hash[key].class == Array
				puts "Key #{i} #{key}\t=---> is an ARRAY!"
				i += 1
			else 
				puts "Neither a hash or an array --> #{i} == #{arr_or_hash[i].class} ."
				i += 1 end end

	elsif arr_or_hash.class == Array
	 	for i in i...arr_or_hash.length # since arrays work with indexes, we need to pass in an integer.. 
			if arr_or_hash[i].class == Hash
				puts (i+1) == arr_or_hash.length  ? "HASH at last index #{i}" : "HASH at index #{i}"
				i+=1
			elsif arr_or_hash[i].class == Array
				puts (i+1) == arr_or_hash.length  ? "HASH at last index #{i}" : "ARRAY at index #{i}"
				i+=1
			else
				puts "Neither a hash or an array --> #{i} == #{arr_or_hash[i].class} ."
				i += 1 end
	 end
	else 
		puts "Sorry, #{key_to_search} =---> class is neither Hash or Array.. Exit." end
end 

def writeAllKeysToAfile(json_file)
	json_file = parseJson(json_file)
	#json_file.each {|key,value| puts key}
	json_file.each do |key,value|
		to_write = createNewFile(key)
		to_write.puts(value) end
end

while true do
	keuze = printMenu()
		if keuze == 1
			writeParametersToFile(false,false)
			next 
		elsif keuze == 2
			findStringToFile()
			next 
		elsif keuze == 3
			puts "Name of json file:"
			arrayOrHash(gets.chomp+".json")
			next 
		elsif keuze == 4
			puts "Name of json file:"
			writeAllKeysToAfile(gets.chomp+".json")
			next 	
		elsif keuze == 5
			puts "Exiting, bye"
			exit end
end	


