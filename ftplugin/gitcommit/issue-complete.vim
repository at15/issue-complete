if !has('python3')
    echom "issue complete requires python3 binding"
    if has('python')
        echom "you are using python2 binding"
    endif
	finish
endif