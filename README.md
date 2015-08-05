# issue-complete
show hint for github/gitlab issue when editing git commit messages

sometimes we forgot a issue's number and don't want to open a browser when editing commit messages.
so it would be awesome if the editor can show the issues like github/gitlab's editor.

so we need
- cache the github/gitlab issues, in order to not exceed api rate and work offlines
- show hint in editor, maybe I should write a vim plugin (but I hardly use vim except editing commit messages)
- use electron to write a cross platform editor. ( e... it would be really slow, but there is way we can check if there is a electron instance running, and hold a long tcp connection until user finish editing in the electron editor, this could be a atom plugin i think .... )

## Install

I just start learning vim, so I just link `ftdetect` and `ftplugin` to my `~/.vim`
And when you are `git commit` using vim, you can type `:TT` and it will show a print.

## Road map

- [x] get current repo information by reading file in .git folder
- [ ] make api calls to github to get the issue list
- [ ] allow filter issues in the command
- [ ] allow search issues
- [ ] support Chinese
- [ ] cache issues and add command for fetch
- [ ] add it to auto completion when type `Fix #` it will pop up recent issues  

## Ref

- https://github.com/JarrodCTaylor/vim-plugin-starter-kit
- http://vimdoc.sourceforge.net/htmldoc/if_pyth.html  The python interface for vim
