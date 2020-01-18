import RPi.GPIO as io
io.setmode(io.BCM)

in1_pin = 4
in2_pin = 17

io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)

while True:
  myIn = input("CW or CC: ).lower()
  if(myIn == "cw"):
    Wio.output(in1_pin, True)    
    io.output(in2_pin, False)
  elsif(myIn == "cc"):
    io.output(in1_pin, False)
    io.output(in2_pin, True)
