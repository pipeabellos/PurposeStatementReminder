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
messages = [
  "The purpose of my life is to use my persistence, ambition, curiosity, doingness, and pursuit of excellence by Researching and learning to expand my skillset to build things, building things and solve problems for me and for people that surround me, working with people that Inspire and that I admire, experimenting to create novel solutions, leading a team towards an objective that I’m excited about to bring about world in which technology is solving problems that it is uniquely good at solving while freeing up people to live to their full potential.",
  "My goal is to make a positive impact on the world by using my skills and knowledge to create innovative solutions to important problems. I want to work with like-minded individuals who share my passion for making a difference, and I am committed to continuous learning and self-improvement in order to achieve my full potential.",
  "I am driven by a desire to create value for others and to make a positive impact on the world. I believe that by constantly learning and improving my skills, I can use my knowledge and expertise to solve important problems and create meaningful change. I am also committed to working with others who share my values and vision, and to leading by example in everything I do.",
  """An ideal world is one in which technology is solving problems that it is uniquely good at solving while freeing up people to live to their full potential:
    - everything is as efficient as they can be
    - no one loses time and energy in things that technology can do better than them → Technology does all of the things that it is better than humans at doing, so humans can focus on those things which they are uniquely good at
    - everyone is living their live to their full potential
    - problems that really matter are being solved
    - authenticity rules without the need of having to follow trends or modes""",
  """My top Characteristics:
    - Persistent
    - Ambitious
    - Learner (curious)
    - Doer
    - Excellence (everything he does, good or bad, he aims to do it the best possible way)""",
  """My top Behaviours:
    - Researching and learning to expand my skillset to build things
    - Building things and solving problems for me and for people that surround me
    - Working with people that Inspire and that I admirge
    - Experimenting to create novel solutions
    - Leading a team towards an objective that I’m excited about"""
, """PIPITO:
Needy/Inferior Persona
*Body:* Little, contracted, fetal position. Down face. He’s a victim.
*Voice:* Soft voice, without energy
Hides in a corner.
Great things to share with the world and finds heroism in withholding them. Afraid to share them.

Very uncomfortable. Doesn’t like showoffs. Hates them. Feels uncomfortable with people who simply show their work. Feels threatened.
1. *What’s the most important thing:* Feel recognized. People say good things, value him. Extrnal validation and value.
2. *What are you most proud about how you’ve served Felipe:* Has enabled Felipe to feel like a superman. Has made other made other people think you’re perfect.
3. *When did you 1st appear:* 6 years old. Learning to play instruments (singing violin, tennis, learning all of these things).
	Story: *17 years old. Lied about a Hummer to say it was your Dad’s to be perceived as wealthy.*
4. *Who did you learn your style from:* My mother. Mom was protective of you—she was with you, you were the center of her life.
5. *What are you most afraid of:* Flaws. People knowing your flaws. Knowing that he’s just another person.
6. *In your heart of hearts what do you most want:* Recognition. Fame.
7. *What is your gift/essence quality:* Lying. Deception. He’ll get things done""", """*Unique Genius: Determined Man of Service*

Vision + Determination + Service.

You shine most brightly with clear goal posts, people to serve, and a determination to serve them powerfully by finding the best possible solution. This genius is clear to those who have worked with you, they voice an admiration for your creative problem-solving and ability to find elegant and powerful solutions to big problems.""",
"""Biggest Strengths 💪
- *Sincerity:* You are sincere. Earnest. Authentic. Genuinely you. Those closest to you know and trust that you will be transparently and authentically you. In doing so, they experience you as present, empathetic, and a good listener. This sincerity create trust and connection, as well as the inherent satisfaction of being authentically you.
- *Determination:* Some call it resilience, perseverance, or dedication. Ultimately, it is determination. When you make up your mind, you are committed. Resolute. Firm. Determined to see whatever it is through to its end, you give your all until you get there.
- *Service:* You are a man of Service. You get a great degree of satisfaction from helping others. Be it friends, family, those who you work for, with, or work for you,  you desire to be of service to them. To feel the satisfaction that comes from seeing their lives better by your hand.
- *Curiosity:* You wonder. You are deeply inquisitive. Inquisitive about the world, technology, and about yourself and how to be better. This curiosity and wonder is a driving force in your life.
- *Excellence:* You have always had high standards for yourself. Be it academics, sports, how you hold yourself or who you associate with, you strive to be the best. This desire led you to rise quickly when you worked for others, and to enter the arena of entrepreneurship in an attempt to win its spoils for yourself.
- *Vision:* You dream of the future. Of what a better future looks like, and how to get there. This future-optimism is a driving force in your life. You believe deeply in the power of a brighter future. You seek ways to create it. When you find ways that you believe in, you become determined to create them, quickly seeking and envisioning possible paths to their realization.""", """Blindspots
- *Superman: *Tendency to isolate and do it all yourself.
- *External Validation Addict:* Over the years, your Excellence and tendency toward Service have made you come to not only appreciate, but also rely on external reinforcement from others.
- *Stubborn & Perfect:* Desire to maintain an image of perfectionism.
- *Waiting to Lead:* You are a man of vision. Yet at time, it feels like you still wait for permission to be the fully empowered leader that lives inside of you.""", "When with others, be sincerely and candidly you.", "being vulnerable when you are struggling.", "Your determination is a superpower. Use it in times of self-doubt. Acknowledge that you are a resolute and determined leader, and find the next way through.", "Ask yourself: as a leader, how can I be in service to all of my partners? My investors? Employees? Customers? Cofounder? Myself? Allow service to be a Northstar.","My purpose is to use my persistence, ambition, and curiosity to build and solve problems, and to pursue excellence in everything I do.",
"I am a learner, doer, and tech enthusiast, and I enjoy working with inspiring people to create novel solutions.",
"I am empathetic, caring, and a good listener, but I can also be stubborn and easily distractable.",
"I strive to be organized and structured, and I prioritize research, learning, and exercise in my daily routine.",
"I am an early adopter of new ideas and technologies, and I enjoy sharing my projects with the world and receiving feedback.",
"I visualize my future and imagine better possibilities through journaling and meditation, and I make time to connect with people I care about.",
"My vision for the world is one in which technology is used to solve problems and free up people to live their lives to their full potential.",
"In this ideal world, efficiency is a top priority, and everyone is able to focus on their unique strengths and passions.",
"Authenticity is valued above all else, and important problems are being solved.",
"My goal is to contribute to this vision by building and solving problems through technology, and by leading and inspiring others to do the same.",
"I believe that with persistence, ambition, and a focus on excellence, we can bring about positive change in the world.",
"I am committed to using my skills and abilities to make a positive impact and help others live their best lives.",
"I know that I have strengths and weaknesses, and I am constantly working to improve and grow as a person.",
"I believe in the power of collaboration and teamwork, and I strive to bring out the best in others.",
"I am open-minded and have strong opinions that are weakly held, meaning that I am willing to listen to different perspectives and adapt my viewpoints when necessary.",
"I understand the importance of balance in life, and I work to find a healthy balance between my personal and professional commitments.",
"I am passionate about using technology to solve problems and make life easier for people, and I am always looking for new ways to do so.",
"I believe that with hard work, dedication, and a positive attitude, anything is possible.",
"I am determined to make the most of my life and to use my skills and talents to make a difference in the world.",
"I am committed to living my purpose and making a positive impact on those around me.","Remember to tap into your sincerity when interacting with others. It helps build trust and connection.",
"Use your determination to see things through to the end. You have the resilience and perseverance to get there.",
"Your desire to be of service to others is a big strength. It brings satisfaction to both you and those you help.",
"Your curiosity drives you to learn and grow. Keep asking questions and seeking out new knowledge.",
"Don't let your pursuit of excellence hold you back. It's important to strive for the best, but also know when to ask for help and learn from others.",
"Your vision for the future is a powerful driving force. Use it to create a brighter future for yourself and others.",
"Be aware of your tendency to isolate and try to do everything yourself. It's important to ask for help and allow your team to thrive.",
"Don't rely too heavily on external validation. Trust in your own internal validation and make tough decisions based on your values and principles.",
"Be mindful of your tendency to over-focus on the details. While it's important to pay attention to details, don't lose sight of the big picture.",
"Use your strong communication skills to clearly convey your thoughts and ideas to others.",
"Remember to balance your focus on your own growth with supporting the growth of those around you.",
"Use your natural leadership skills to guide and motivate your team.",
"Be open to feedback and use it as an opportunity to grow and improve.",
"Don't let your perfectionism hold you back. It's important to strive for excellence, but also know when to move forward and not get bogged down in the details.",
"Remember to take breaks and prioritize self-care. It helps you perform at your best and avoid burnout.",
"Use your adaptability to thrive in changing situations and pivot when needed.",
"Don't be afraid to take risks and try new things. It's an important part of growth and success.",
"Remember to set clear goals and priorities. It helps you stay focused and achieve your objectives.",
"Use your natural curiosity to seek out new opportunities and challenges.",
"Remember to stay true to your values and principles. It helps guide your decisions and actions.",
"Use your determination to overcome obstacles and setbacks. You have the resilience and perseverance to keep pushing forward.",
"Remember to stay present and focused in the moment. It helps you perform at your best.",
"Use your natural charisma to inspire and motivate those around you.",
"Don't be afraid to ask for help when you need it. It's important to have a strong support system.",
"Use your strong communication skills to effectively connect with others.",
"Remember to celebrate your wins and accomplishments. It helps keep you motivated and energized.",
"Use your adaptability to thrive in changing situations and pivot when needed.",
"Don't be afraid to take risks and try new things. It's an important part of growth and success.",
"Remember to set clear goals and priorities. It helps you stay focused and achieve your objectives.",
"Use your natural curiosity to seek out new opportunities and challenges.",
"Remember to stay true to your values and principles. It helps guide your decisions and actions.",
"Use your determination to overcome obstacles and setbacks. You have the resilience and perseverance to keep pushing forward.",
"Remember to stay present and focused in the moment. It helps you perform at your best.",
"Use your natural charisma to inspire and motivate those around you.",
"Don't be afraid to ask for help when you need it. It's important to have a strong support system.",
"Use your strong communication skills to effectively connect with others.",
"Remember to celebrate your wins and accomplishments. It helps keep you motivated and energized.",
"Use your adaptability to thrive in changing situations and pivot when needed.",
"Don't be afraid to take risks and try new things. It's an important part of growth and success.",
"Remember to set clear goals and priorities. It helps you stay focused and achieve your objectives.",
"Use your natural curiosity to seek out new opportunities and challenges.",
"Remember to stay true to your values and principles. It helps guide your decisions and actions.",
"Use your determination to overcome obstacles and setbacks. You have the resilience and perseverance to keep pushing forward.",
"Remember to balance your focus on your own growth with supporting the growth of those around you.",
"Use your natural leadership skills to guide and motivate your team.",
"Be open to feedback and use it as an opportunity to grow and improve.",
"Don't let your perfectionism hold you back. It's important to strive for excellence, but also know when to move forward and not get bogged down in the details.",
"Remember to take breaks and prioritize self-care. It helps you perform at your best and avoid burnout.",
"Use your adaptability to thrive in changing situations and pivot when needed."
]

while True:
  # Connect to the Twilio API
  client = Client(account_sid, auth_token)

  # Choose a random message from the list
  message = random.choice(messages)

  # Send the SMS message
  message = client.messages.create(body=message,
                                   from_=from_number,
                                   to=to_number)

  # Choose a random wait time between 1 and 4 days
  wait_time = random.randint(0.5, 2) * 24 * 60 * 60

  # Wait the chosen number of days before sending the next message
  time.sleep(wait_time)
