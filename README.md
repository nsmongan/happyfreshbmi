# happyfreshbmi
HappyFresh Technical Test to create a BMI calculator


How to Use:

Call the API with this syntax:

curl -X 'GET' 'https://api.cyllenia.com/api/bmicalculator/?height=[height]&weight=[weight]' -H 'accept: application/json'

where [height] = height in cm and [weight] = weight in kg

example: curl -X 'GET' 'https://api.cyllenia.com/api/bmicalculator/?height=172&weight=84' -H 'accept: application/json'



Security in place:
- Bandit Gitlab-CI SAST
- Anti DDoS provided by Cloudflare
