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

def arrayOrHash (arr_or_hash)
	if arr_or_hash.class == Hash   
		i = 1
		arr_or_hash.each do |key,value|
			if arr_or_hash[key].class == Hash
				puts "Key #{i}\t=---> #{key} is a HASH!"
				i += 1
			elsif arr_or_hash[key].class == Array
				puts "Key #{i}\t=---> #{key} is an ARRAY!"
				i += 1
			else
				puts "Key #{key} \t=---> some weird class dude." end end

	elsif arr_or_hash.class == Array
	 	i = 0	
	 	for i in i...arr_or_hash.length
			if arr_or_hash[i].class == Hash
				puts (i+1) == arr_or_hash.length  ? "HASH at last index  #{arr_or_hash.object_id.to_s} index #{i}" : "HASH at  #{arr_or_hash.object_id.to_s} index #{i}"
		elsif arr_or_hash[i].class == Array
			puts (i+1) == arr_or_hash.length  ? "ARRAY at last index  #{arr_or_hash.object_id.to_s} index #{i}" : "ARRAY at  #{arr_or_hash.object_id.to_s} index #{i}"
		else
			puts "some weird class dude." end end
	else 
		puts "Sorry, class is neither Hash or Array.. Exit." end
end 
arrayOrHash(data_hash['resources'])
#puts data_hash.class
