echo “Enter a String or number : ”
read string or number
if [ “$(echo $string | rev)” = “$string” ]
then
sleep 3
echo “\”$string\” IS a Palindrome”
else
echo “\”$strin\” IS NOT a Palindrome”