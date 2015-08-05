# Doc

## Vim

### vimsrc 

http://vim.wikia.com/wiki/Vimrc

type `:version` in vim to see the path

`~/.vim/vimrc` is my current one

type `:e $MYVIMRC` to edit it. (but you have to create it first

### omini completion

`ctrl + x` + `ctrl + o` and it will show the auto complete

### plugin

just put a `test.vim` in `~/.vim/plugin` and it will work

create a symbol link for dev

`ln -s ~/github/issue-complete/ftplugin/COMMIT_EDITMSG/issue-complete.vim ~/.vim/ftplugin/COMMIT_EDITMSG`
`ln -s ~/github/issue-complete/ftplugin/COMMIT_EDITMSG/issue.py ~/.vim/ftplugin/COMMIT_EDITMSG`

using ftdetect http://learnvimscriptthehardway.stevelosh.com/chapters/44.html
