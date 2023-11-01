from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/MontyCarlo/<int:SimNum>')
def MontyCarloSim(SimNum):
    TotalSim = SimNum
    SimInCircle = 0
    for i in range(SimNum):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        radius = x**2 + y**2
        if radius <= 1:
            SimInCircle += 1
    return "<h1>Monty Carlo Simulation to estimate Pi</h1>" + "<p1>Pi is roughly equal to </p1>" + str(4*(SimInCircle/TotalSim)) + "<p1> given the number of simulations you requested which was </p1>" + str(TotalSim) + "<p1>.</p1>"

if __name__ == '__main__':
    app.run()

# To use this application simply run the program then go to the website
# http://127.0.0.1:5000/MontyCarlo/(number of simulations you want to run in
# numbers such as 1, 2, or 3) The program will reply with the value of pi it
# calculated based on the number of simulations you asked for.