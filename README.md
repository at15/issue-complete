# issue-complete
show hint for github/gitlab issue when editing git commit messages

sometimes we forgot a issue's number and don't want to open a browser when editing commit messages.
so it would be awesome if the editor can show the issues like github/gitlab's editor. 

so we need 
- cache the github/gitlab issues, in order to not exceed api rate and work offlines
- show hint in editor, maybe I should write a vim plugin (but I hardly use vim except editing commit messages)
- use electron to write a cross platform editor. ( e... it would be really slow, but there is way we can check if there is a electron instance running, and hold a long tcp connection until user finish editing in the electron editor, this could be a atom plugin i think .... )

I think I prefer the vim one ... 
