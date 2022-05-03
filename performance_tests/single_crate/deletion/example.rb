require 'ro_crate'


times_to_add = ARGV[0]
starting = Process.clock_gettime(Process::CLOCK_MONOTONIC)

crate = ROCrate::Crate.new

for i in 1..times_to_add.to_i do
  local_file = crate.add_file('./data/file'+i.to_s)
  person = ROCrate::Person.new(crate, '#joe'+i.to_s, {name: 'Joe Bloggs'})
  crate.add_contextual_entity(person)
  local_file.author = person
end

for i in 1..times_to_add.to_i do
  crate.delete('#joe'+i.to_s, remove_orphaned:false)
end
ending = Process.clock_gettime(Process::CLOCK_MONOTONIC)

puts(times_to_add + ' ' + (ending - starting).to_s)

File.open("deletion_rb.txt", "a") { |f| f.puts(ending - starting).to_s}
#ROCrate::Writer.new(crate).write('./an_ro_crate_directory')

