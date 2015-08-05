if !has('python')
  echom "No python!"
	finish
endif

function Meow()
  echom "Meow!"

python << endOfPython

print "I am printing!"

endOfPython

endfunction

command! TT call Meow()