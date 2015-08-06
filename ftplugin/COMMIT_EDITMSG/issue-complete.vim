if !has('python')
    echom "No python!"
	finish
endif

python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

function GitIssue()

python << endOfPython

from issue import list_all

list_all()

endOfPython

endfunction

command! Is call GitIssue()
