if !has('python')
    echom "No python!"
	finish
endif

python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

function GetIssue()

let res = []

" TODO: put all the listed issues to the res
python << endOfPython

import vim
from issue import list_open_issues
from issue import add_to_vim_list

issues = add_to_vim_list('res', list_open_issues())

endOfPython

return res

endfunction

function UpdateIssue()

python << endOfPython

from issue import update_issues

update_issues()

endOfPython

endfunction

function IssueComplete(findstart, base)
     if a:findstart
	    " locate the start of the word
	    let start = col('.') - 1
	    return start
	  else
	    " TODO:Do the match"
	    return GetIssue()
	  endif
endfunction

setlocal omnifunc=IssueComplete
command! UpdateIssue call UpdateIssue()
