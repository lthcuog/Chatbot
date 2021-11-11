## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## picture ronaldo
* greet
  - utter_greet
* ronaldo
  - utter_picture
*affirm
  - utter_goodbye

## access facebook
* greet
  - utter_greet
* facebook
  - utter_loginFace
* affirm 
  - utter_goodbye

## access zalo
* greet
  - utter_greet
* zalo
  - utter_loginZalo

## read news
* greet
  - utter_greet
* news
  - utter_read_news
