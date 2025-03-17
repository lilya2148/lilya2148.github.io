Just a simple page


There's an issue with having two github accounts
brew install gh
gh auth login
gh auth switch

git push https://lilya2148@github.com/lilya2148/lilya2148.github.io.git
https://github.com/lilya2148/lilya2148.github.io

# working with multiple github accounts on mac
following instructions [here](https://gist.github.com/rahularity/86da20fe3858e6b311de068201d279e3)

`cd ~`
`mkdir .ssh`
`cd .ssh`
`ssh-keygen -t rsa -C "lilyarnar1@gmail.com" -f "lilya2148"`
`ssh-add -K ~/.ssh/lilya2148`
``pbcopy < ~/.ssh/lilya2148.pub``

