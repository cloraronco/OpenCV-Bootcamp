echo $(git add *)
echo $(git status)
echo $(git commit -m "$1")
echo $(git status)
echo $(git push)

