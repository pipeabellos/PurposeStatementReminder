import twilio
from twilio.rest import Client
import time
import random
import os

# Replace these with your own Twilio account SID and auth token
# Your Account SID from twilio.com/console
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
# Your Auth Token from twilio.com/console
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

# Replace these with your own Twilio phone number and the phone number you want to send the message to
from_number = os.environ.get("TWILIO_SENDER_PHONE")
to_number = os.environ.get("RECEPIENTS_PHONE")

# This is the message that will be sent
messages = ["The purpose of my life is to use my persistence, ambition, curiosity, doingness, and pursuit of excellence by Researching and learning to expand my skillset to build things, building things and solve problems for me and for people that surround me, working with people that Inspire and that I admire, experimenting to create novel solutions, leading a team towards an objective that I’m excited about to bring about world in which technology is solving problems that it is uniquely good at solving while freeing up people to live to their full potential.","My goal is to make a positive impact on the world by using my skills and knowledge to create innovative solutions to important problems. I want to work with like-minded individuals who share my passion for making a difference, and I am committed to continuous learning and self-improvement in order to achieve my full potential.",
    "I am driven by a desire to create value for others and to make a positive impact on the world. I believe that by constantly learning and improving my skills, I can use my knowledge and expertise to solve important problems and create meaningful change. I am also committed to working with others who share my values and vision, and to leading by example in everything I do.", """An ideal world is one in which technology is solving problems that it is uniquely good at solving while freeing up people to live to their full potential:
    - everything is as efficient as they can be
    - no one loses time and energy in things that technology can do better than them → Technology does all of the things that it is better than humans at doing, so humans can focus on those things which they are uniquely good at
    - everyone is living their live to their full potential
    - problems that really matter are being solved
    - authenticity rules without the need of having to follow trends or modes""", """My top Characteristics:
    - Persistent
    - Ambitious
    - Learner (curious)
    - Doer
    - Excellence (everything he does, good or bad, he aims to do it the best possible way)""", """My top Behaviours:
    - Researching and learning to expand my skillset to build things
    - Building things and solving problems for me and for people that surround me
    - Working with people that Inspire and that I admire
    - Experimenting to create novel solutions
    - Leading a team towards an objective that I’m excited about"""]


while True:
    # Connect to the Twilio API
    client = Client(account_sid, auth_token)

    # Choose a random message from the list
    message = random.choice(messages)

    # Send the SMS message
    message = client.messages.create(body=message, from_=from_number, to=to_number)

    # Choose a random wait time between 1 and 4 days
    wait_time = random.randint(1, 3) * 24 * 60 * 60

    # Wait the chosen number of days before sending the next message
    time.sleep(wait_time)