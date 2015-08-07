if !has('python')
    echom "No python!"
	finish
endif

function Dummy(findstart, base)
     if a:findstart
	    " locate the start of the word
	    let line = getline('.')
	    let start = col('.') - 1
	    while start > 0 && line[start - 1] =~ '\a'
	      let start -= 1
	    endwhile
	    return start
	  else
	    " find months matching with "a:base"
	    let res = []
	    for m in split("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec")
	      if m =~ '^' . a:base
		call add(res, m)
	      endif
	    endfor
	    return res
	  endif
endfunction

setlocal omnifunc=Dummy

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
