require 'json'
#file_write = File.new('read_parameter', 'w')
hsh = {empty: true}
#hsh.each {|key,value| file_write.puts("key =---> #{key} =---> #{value}")}
#hsh['install_switches'].each {|key, value| puts key}
#puts hsh['install_switches'].class
json_file = File.read('sw444v1105.json')
data_hash = JSON.parse(json_file)
hash_length = data_hash['resources'].length
i = 0

for i in i...hash_length
	if data_hash['resources'][i].class == Hash
		puts (i+1) == hash_length  ? "HASH at last index data_hash['resources'] index #{i}" : "HASH at data_hash['resources'] index #{i}"
	elsif data_hash['resources'][i].class == Array
		puts (i+1) == start_length  ? "ARRAY at last index data_hash['resources'] index #{i}" : "ARRAY at data_hash['resources'] index #{i}"
	else
		puts "some weird class dude." end 
end 
#puts data_hash['resources'].length
i = 1 #reset i since the loop above incremented it.. check with puts i 
data_hash.each do |key, value|
		if data_hash[key].class == Hash
			puts "Key #{i}=---> #{key} is a HASH!"
			i += 1
		elsif data_hash[key].class == Array
			puts "Key #{i}=---> #{key} is a ARRAY!"
			i += 1
		else
			puts "Key #{key} =---> some weird class dude." end 
end 
