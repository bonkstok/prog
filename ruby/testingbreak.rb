def testing(target, method)
  (0..5).each do |x| # After 5 times y, x will ++.
    (0..10).each do |y| #
     puts "X is #{x.to_s}, Y is #{y.to_s}. sum: #{x*y}"
     if x*y == target
       if method == "break"
       		puts "<-----"
       		break  #just breaks out of the most inner loop, so it will continue with the next number in range of x
		end  
		#break if method == "break"     
       return if method == "return" #complete stop the loop /method
     end
    end 
  end
end

testing(10, "break")
#testing(10, "return")