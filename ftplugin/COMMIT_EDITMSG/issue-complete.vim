if !has('python')
  echom "No python!"
	finish
endif

python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

function GitIssue()
  echom "Show me the issue"

python << endOfPython

print "I am printing!"

from issue import hi

hi()

endOfPython

endfunction

command! Is call GitIssue()
