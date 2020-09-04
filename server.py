from flask import Flask, render_template
import math
app = Flask(__name__)

# Radar functions
# TODO: make this method actually work!
def point_on_circle(center, radius, angle):
  return {
    'x': center['x'],
    'y': center['y']
  }

app.jinja_env.globals.update(point_on_circle=point_on_circle)

CENTER = { 'x': 50, 'y': 50 }
MAX_RADIUS = 30
DATA = {
  'viewbox': '0 0 100 100',
  'center': CENTER,
  'max_radius': MAX_RADIUS,
  'quarters': [point_on_circle(CENTER, MAX_RADIUS, angle) for angle in [0, math.pi / 2, math.pi, 3 * math.pi / 2]]
}

@app.route('/radar')
def radar():
  return render_template('radar.html', data = DATA)

if __name__ == '__main__':
   app.run(debug = True)
