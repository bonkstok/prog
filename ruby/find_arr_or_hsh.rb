require 'json'
#file_write = File.new('read_parameter', 'w')
hsh = {empty: true} # supply your own hash to check ok?
#hsh.each {|key,value| file_write.puts("key =---> #{key} =---> #{value}")}
#puts hsh['install_switches'].class
json_file = File.read('sw444v1105.json')
data_hash = JSON.parse(json_file)
hash_length = data_hash['resources'].length
i = 0

for i in i...hash_length
	if data_hash['resources'][i].class == Hash
		puts (i+1) == hash_length  ? "HASH at last index data_hash['resources'] index #{i}" : "HASH at data_hash['resources'] index #{i}"
	elsif data_hash['resources'][i].class == Array
		puts "ARRAY at data_hash['resources'] index #{i}"
	else
		puts "some weird class dude." end 
end 

i = 1 #reset i since the loop above incremented it.. check with puts i 
data_hash.each do |key, value|
		if data_hash[key].class == Hash
			puts "Key #{i}:#{key} is a HASH!"
			i += 1
		elsif data_hash[key].class == Array
			puts "Key #{i}:#{key} is a ARRAY!"
			i += 1
		else
			puts "Key #{key} ==> some weird class dude." end 
end 
