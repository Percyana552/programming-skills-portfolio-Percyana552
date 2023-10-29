
# hello world
message='hello world'
print(message)
# text data is called string

# there is no different but , it is depend on the statment
message= ' Boby\'s world'
print(message)
# we can go with double qoutes
message="Boby's world"
print(message)

#if you need to  create multi-line string and one way we can do this by use three qoutes  at beginnig and  end of our string

message= """Petras is beutifual sweetheart and she never give up on her dream doest matter what
her favorite colour is purple"""
print(message)
 # how  many  charates
message= 'hello world'
print(len(message))

#location of our string
print(message[10])

#range of charatectr is called slices
print(message[0:5])
 # method of lower  case upper is the same

message= "Hello world"
print(message.lower())

# count certain number of string but we should settle string

message="hello world"
print(message.count("h"))

# found index takes rgument also like count
message = 'hello world'
print(message.find('world'))
# if you want find  a value that doest exist in strig aways came negative number
print(message.find('Petras'))

# replace method takes two arguments 
message='hello world'
new_message=message.replace('world', 'universe')
print(new_message)
  # how can we add multiple string and we concatenate together
greets= 'hello'
name='Petras'
message= greets + ',' + name
print(message)
 #add another string
message= greets +','+ name + '. world!'
print(message)
#formatted string display in the same way of ='{},{}.welcome!'.format(greets,name)
print(message)
# f string to make our life easier
message= 'hello'
name='Petras'
message=f'{greets},{name}. welcome!'
print(message)

#use of dir
greeting='hello'
name='Petronia'
print(dir(name))