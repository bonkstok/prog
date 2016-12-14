require 'json'
print "Eter filename to write to:"
write_file = File.new(gets.chomp + ".json", "w")

print "Enter name of json file: "
json_file = File.read(gets.chomp + ".json")

data_hash = JSON.parse(json_file)
#puts data_hash.keys

i = 1
data_hash.each do |key, value|
	write_file.puts("#{i} -- Key: #{key} --\n Value: #{value}")
	i += 1
end

#data_hash["tags"].each { |tag| puts tag}
#puts data_hash["tags"][0]
write_file.close()
#json_file.close()
